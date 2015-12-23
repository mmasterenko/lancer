/*
 * {'lancer9': ['mechanic', '1.3'] }
 * */
var choosedEngine = {};

$(document).ready(function(){

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

        choiceContainer.find('[data-choice-state=2] .sub-list a').each(function(){
            var href = $(this).attr('href');
            $(this).attr('href', href + url);
        });
    });
});
