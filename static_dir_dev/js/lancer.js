var all_cars, car_ids = [];

/*
 * {'lancer9': {'subtype':x, 'engine':x, 'transmission':x} }
 */
var current_choice = {};

function get_subtypes(cars) {
    var i, car, subtype;
    var subtypes = {};
    for(i in cars) {
        car = cars[i];
        subtype = car['subtype'];
        subtypes[subtype] = true;
    }
    return _.keys(subtypes)
}

function get_engines(cars, subtype) {
    var i, car, engine;
    var engines = {};
    for(i in cars) {
        car = cars[i];
        if(car['subtype'] == subtype){
            engine = car['engine'];
            engines[engine] = true;
        }
    }
    return _.keys(engines)
}

function get_trans(cars, subtype, engine) {
    var i, car, transmission;
    var transmissions = {};
    for(i in cars) {
        car = cars[i];
        if(car['subtype'] == subtype && car['engine'] == engine) {
            transmission = car['transmission'];
            transmissions[transmission] = true;
        }
    }
    return _.keys(transmissions)
}

function analyze_subtypes(model, subtypes) {

    console.log('analyze_subtypes: model:', model);
    console.log('analyze_subtypes: subtypes:', subtypes);

    if(_.size(subtypes) == 1) {
        // выбираем подвид
        var subtype = subtypes[0];
        // сохраняем выбранный подвид
        var obj = current_choice[model] || {};
        obj['subtype'] = subtype;
        current_choice[model] = obj;

        var engines = get_engines(all_cars[model], subtype);

        analyze_engines(model, subtype, engines);

    } else {
        // вывести меню подвидов
        // + навешать на меню коллбэки
    }
}

function analyze_engines(model, subtype, engines) {

    console.log('analyze_engines: subtype:', subtype);
    console.log('analyze_engines: engines:', engines);

    if(_.size(engines) == 1){
        var engine = engines[0];
        var transmissions = get_trans(all_cars[model], subtype, engine);

        var obj = current_choice[model] || {};
        obj['engine'] = engine;
        current_choice[model] = obj;

        analyze_trans(model, subtype, engine, transmissions)

    } else {
        // вывести меню двигателей
        // + навешать на это меню колбэки
        set_engines(model, engines)
    }

}

function analyze_trans(model, subtype, engine, transmissions) {

    console.log('analyze_trans: engine', engine);
    console.log('analyze_trans: transmissions', transmissions);

    if(_.size(transmissions) == 1){
        // это единственная машина. взять ее id.
        var transmission = transmissions[0];

        var obj = current_choice[model] || {};
        obj['transmission'] = transmission;
        current_choice[model] = obj;

        set_trans(model, subtype, engine, transmission);
    } else {
        // вывести меню трансмиссий
        // + навешать на это меню колбэки
    }
}

function set_menu(model, type, list) {
    console.log('set_menu: model:', model);
    console.log('set_menu: type:', type);
    console.log('set_menu: list:', list);

    var header = {
        'subtypes': 'Какая модель:',
        'engines': 'Какой у вас двигатель:',
        'transmissions': 'Какая у вас трансмиссия:'
    };

    var car_model = $('.car-model[data-car-model='+model+']');

    car_model.find('[data-choice-state=1]').find('.choice-header').text(header[type]);
    var choice_list = car_model.find('[data-choice-state=1]').find('.choice-list').html('');

    var li, value, raw_value;
    for(var i in list){
        raw_value = list[i];
        value = list[i] || 'другое';
        li = $('<li data-capacity="'+value+'"><a href="javascript:void(0)">'+value+'</a></li>');
        li.on('click', (function (model, type, raw_value) {
            return function (event) {
                click_menu(model, type, raw_value);
            };
        })(model, type, raw_value));
        choice_list.append(li);
    }

}

function click_menu(model, type, raw_value) {

    console.log('click_menu:', model, type, raw_value);
    console.log(current_choice);

    var subtype, engine;

    if(type == 'subtypes') {
        subtype = raw_value;
        var engines = get_engines(all_cars[model], subtype);
        analyze_engines(model, subtype, engines);
    }

    if(type == 'engines') {
        subtype = current_choice[model]['subtype'];
        engine = raw_value;
        var transmissions = get_trans(all_cars[model], subtype, engine);

        analyze_trans(model, subtype, engine, transmissions);
    }

    if(type == 'transmissions') {

    }

}

function set_engines(model, engines) {
    console.log('set_engines -> set_menu');

    set_menu(model, 'engines', engines);

}

function set_subtypes(model, subtypes) {
    console.log('set_subtypes -> set_menu');

    set_menu(model, 'subtypes', subtypes);

}

function set_trans(model, subtype, engine, transmission) {

    var i, car, id;
    var cars = all_cars[model];
    for(i in cars) {
        car = cars[i];
        if(car['subtype'] == subtype && car['engine'] == engine && car['transmission'] == transmission) {
            id = car['id'];
            car_ids.push(id);
            // добавить логику для mech auto null
        }
    }
}


$(document).ready(function(){

    $.getJSON('/api/cars', {}, function (result) {
        all_cars = result;
    });

    /*
     * {'lancer9': ['mechanic', '1.3'] }
     */
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

        //
        var model = $(this).parents('[data-car-model]').data('carModel');
        var subtypes = get_subtypes(all_cars[model]);

        analyze_subtypes(model, subtypes);

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


    /*
       всплывающее окошко: "перезвонить мне"
     */
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
