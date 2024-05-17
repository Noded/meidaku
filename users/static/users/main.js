$(document).ready(function($) {
    $('.open-modal-button').click(function() {
        var targetId = $(this).data('target');
        $('#' + targetId).fadeIn();
        return false;
    });

    $('a.open-modal-button').click(function() {
        var targetId = $(this).data('target');
        $('#' + targetId).fadeIn();
        return false;
    });

    $('.popup-close').click(function() {
        $(this).parents('.popup-fade').fadeOut();
        return false;
    });

    $(document).keydown(function(e) {
        if (e.keyCode === 27) {
            e.stopPropagation();
            $('.popup-fade').fadeOut();
        }
    });

    $('.popup-fade').click(function(e) {
        if ($(e.target).closest('.popup').length == 0) {
            $(this).fadeOut();
        }
    });
});

$(document).ready(function($) {
    $('#welcom').fadeIn();

    $('.popup-close').click(function() {
        $(this).parents('.popup-fade').fadeOut();
        return false;
    });

    $(document).keydown(function(e) {
        if (e.keyCode === 27) {
            e.stopPropagation();
            $('.popup-fade').fadeOut();
        }
    });

    $('.popup-fade').click(function(e) {
        if ($(e.target).closest('.popup').length == 0) {
            $(this).fadeOut();
        }
    });
});


$(document).ready(function () {
    let hiddenRow = $(".expandable");
    let expandBtn = $(".expand-btn");

    $(".expand-btn").click(function () {
        hiddenRow.slideToggle(function () {
            if (hiddenRow.is(":visible")) {
                expandBtn.html("скрыть сценарии работы");
            } else {
                expandBtn.html("показать сценарии работы");
            }
        });
    });
});