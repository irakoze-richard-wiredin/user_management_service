(function($) {
    'use strict';
    $(function() {
        $("#gallery-close").click(function(){
            $(".gallery").css("display", "none");
        });

        $('[data-type="tile-show"]').on('click', function(event) {
            var dataSide = $(this).data('side');

            highlightMarker(dataSide);

            highShowSelectedImage(dataSide);
            
            $('#gallery-modal').css("display", "block");
        });


        $('[data-type="gallery-marker"]').on('click', function(event) {
            var dataSide = $(this).data('side');

            highlightMarker(dataSide);

            highShowSelectedImage(dataSide);
        });
    });
})(jQuery);



function highlightMarker(dataSide) {
    $('[data-type="gallery-marker"]').removeClass('badge-default');
    $('[data-type="gallery-marker"]').addClass('badge-mute');

    $('[data-type="gallery-marker"][data-side="' + dataSide + '"]').removeClass('badge-mute');
    $('[data-type="gallery-marker"][data-side="' + dataSide + '"]').addClass('badge-default');
}


function highShowSelectedImage(dataSide) {
    $('.gallery-image').hide();
    $('.gallery-image[data-side="' + dataSide + '"]').show();
}