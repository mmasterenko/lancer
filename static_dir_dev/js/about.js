$(document).ready(function() {

    $('#video-display').prettyEmbed({
        videoID: 'zsAQZ9IF8Hg',
        playerControls: false,
        playerInfo: false,
        showInfo: false,
        showControls: true,
        previewSize: 'hd',
        //customPreviewImage: 'http://127.0.0.1:8003/static/images/actions/6784385.j88ul0qym1.W958.jpg',
        showRelated: false,
        colorScheme: 'light'
    });


    $(".fancybox").fancybox({
        openEffect	: 'elastic',
        closeEffect	: 'elastic',
        helpers: {
            title: {
                type: 'inside'
            }
        },
        beforeLoad: function() {
            var el, id = $(this.element).data('title-id');

            if (id) {
                el = $('#' + id);

                if (el.length) {
                    this.title = el.html();
                }
            }
        }
    });

});

