$(document).ready(function() {
    $('.rating-plus').click(function() {
        changeRating(+1, $(this).attr('data-id'));
    });

    $('.rating-minus').click(function() {
        changeRating(-1, $(this).attr('data-id'));
    });

    $('.response-div input[type=button]').click(function() {
        var form = $(this).parent();
        var thread = form.parent().parent();
        $.post('/add_comment/',
                {
                    'thread_id': thread.attr('data-id'),
                    'author': form.children('[name=author]').val(),
                    'text': form.children('[name=text]').val()
                },
                function(data) {
                    var new_comment = $('<div class="comment ch-block">');
                    new_comment.append($('<span class="id">' + data['id'] + '</span>'));
                    new_comment.append($('<span class="timestamp">' + data['timestamp'] + '</span>'));
                    new_comment.append($('<div class="ch-block-header"><span class="author">автор: '
                        + data['author'] + '</span></div>'));
                    new_comment.append($('<div class="text">' + data['text'] + '</div>'));

                    $(thread.children('.comments')[0]).append(new_comment);
                }
            );
    });
});

function changeRating(delta, thread_id) {
    $('.rating-value[data-id="' + thread_id + '"]').fadeOut(200);
    $.post('/change_rating/',
            {
                'thread_id': thread_id,
                'delta': delta
            }, function (data) {
                $('.rating-value[data-id="' + thread_id + '"]').text(data.new_rating).fadeIn(400);
            }
    )
}
