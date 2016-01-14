$(document).ready(function(){
    /*
 * {'lancer9': ['mechanic', '1.3'] }
 * */
    var choosedEngine = {};

    /*
     * urls:
     * {'lancer9':  ['/repair', '/tech', ]
     *  'lancer10': ['/repair', '/tech', ]
     * }
     * */
    var service_urls = {};

    $('[data-car-model]').each(function(){
        var model = $(this).data('carModel');
        var urls = [];
        $(this).find('[data-choice-state=2] .sub-list a').each(function(){urls.push($(this).attr('href'))});
        service_urls[model] = urls;
    });

    // кнопка: ВЫБРАТЬ
    $('.car-model button').on('click', function(){
        var choiceContainer = $(this).parents('.choice-container');
        choiceContainer.children().each(function(){$(this).removeClass('active')});
        choiceContainer.find('[data-choice-state=1]').addClass('active');
    });

    // ссылка: "< Назад"
    $('.car-model .choice .back a').on('click', function(){
        var choiceContainer = $(this).parents('.choice-container');
        choiceContainer.children().each(function(){$(this).removeClass('active')});
        $(this).parents('.choice').prev().addClass('active');
    });

    // ссылка: коробка передач: механическая и автоматическая
    $('.car-model .choice .transmission>a').on('click', function(){
        $(this).next().toggleClass('active');
        var e = $(this).parent().siblings().find('.sub-list').removeClass('active');
    });

    // ссылка: объем двигателя
    $('.car-model .choice[data-choice-state=1] .sub-list a').on('click', function(){
        var choiceContainer = $(this).parents('.choice-container');
        choiceContainer.children().each(function(){$(this).removeClass('active')});
        choiceContainer.find('[data-choice-state=2]').addClass('active');

        var model = $(this).parents('[data-car-model]').data('carModel');
        var transType = $(this).parents('[data-trans-type]').data('transType');
        var capacity = $(this).parents('[data-capacity]').data('capacity');
        choosedEngine[model] = [transType, capacity];
        var url = '/' + model + '/' + transType + '/' + capacity;
        choiceContainer.find('[data-choice-state=2] .sub-list a').each(function($index){
            var basic_url = service_urls[model][$index];
            $(this).attr('href', basic_url + url);
        });

    });


    $('#header .callme > a').on('click', function(){
        $('#callme').toggle('fade', 400);
    });

    $('#callme div a').on('click', function(){
        // отправить сообщение
    });

    $('#callme a.close').on('click', function(){
        $('#callme').toggle('fade', 500);
    });

});
