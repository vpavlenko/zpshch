from django.db import models

# Create your models here.


class Board(models.Model):
    title = models.CharField(max_length=200)
    shortcut = models.CharField(max_length=10)

    def __str__(self):
        return '{0} (/{1}/)'.format(self.title, self.shortcut)


class Thread(models.Model):
    # class for both threads and comments
    title = models.CharField(max_length=200, blank=True)  # only for threads
    text = models.TextField()
    author = models.CharField(max_length=200, blank=True, default='аноним')
    board = models.ForeignKey(Board, blank=True, null=True)  # only for threads
    parent = models.ForeignKey('self', blank=True, null=True)  # only for comments
    timestamp = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return '(to {0}): {1}'.format(self.board if self.board else self.parent.id, self.text[:100])