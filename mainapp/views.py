import json

from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context

from mainapp.models import Board, Thread


def main_processor(request):
    return {
        'boards': Board.objects.all(),
    }


def home(request):
    return render(request, 'home.html', {})


def board(request, shortcut):
    board = Board.objects.get(shortcut=shortcut)
    threads = Thread.objects.filter(board=board)
    return render(request, 'board.html', {'board': board, 'threads': threads})


def change_rating(request):
    # ajax POST request
    thread_id = request.POST['thread_id']
    delta = int(request.POST['delta'])
    t = Thread.objects.get(id=thread_id)
    t.rating += delta
    t.save()

    return HttpResponse(json.dumps({
        'new_rating': t.rating,
    }), mimetype='application/json')


def add_comment(request):
    # ajax POST request
    comment = Thread()
    comment.parent = Thread.objects.get(id=int(request.POST['thread_id']))
    comment.text = request.POST['text'].strip()
    author = request.POST['author'].strip()
    if author:
        comment.author = author
    comment.save()

    return HttpResponse(json.dumps({
        'id': '{0:06}'.format(comment.id),
        'timestamp': Template('{{dt}}').render(Context({'dt': comment.timestamp})),
        'author': comment.author,
        'text': comment.text,
    }), mimetype='application/json')
