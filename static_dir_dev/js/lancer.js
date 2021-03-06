var all_cars, car_ids = {};
var service_urls = {};

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

    console.log('analyze_subtypes: model, subtypes:', model, subtypes);

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

        set_menu(model, 'subtypes', subtypes);

    }
}

function analyze_engines(model, subtype, engines) {

    console.log('analyze_engines: subtype, engines:', subtype, engines);

    if(_.size(engines) == 1){
        var engine = engines[0];
        var transmissions = get_trans(all_cars[model], subtype, engine);

        var obj = current_choice[model] || {};
        obj['engine'] = engine;
        current_choice[model] = obj;

        analyze_trans(model, subtype, engine, transmissions)

    } else {

        set_menu(model, 'engines', engines);

    }

}

function analyze_trans(model, subtype, engine, transmissions) {

    console.log('analyze_trans: engine, transmissions:', engine, transmissions);

    if(_.size(transmissions) == 1){
        // это единственная машина. взять ее id.
        var transmission = transmissions[0];

        var obj = current_choice[model] || {};
        obj['transmission'] = transmission;
        current_choice[model] = obj;

        set_trans(model, subtype, engine, transmission);
    } else {

        set_menu(model, 'transmissions', transmissions);

    }
}

function set_menu(model, type, list) {
    console.log('set_menu: model, type, list:', model, type, list);

    list.sort()
    list.reverse()

    var header = {
        'subtypes': 'Выберете модель:',
        'engines': 'Выберете двигатель:',
        'transmissions': 'Какая у вас трансмиссия:'
    };

    var trans = {
        'auto': 'автоматическая',
        'mech': 'механическая'
    };

    var car_model = $('.car-model[data-car-model='+model+']');

    car_model.find('[data-choice-state=1]').find('.choice-header').text(header[type]);
    var choice_list = car_model.find('[data-choice-state=1]').find('.choice-list').html('');

    var li, value, raw_value, null_replace_trans;

    list = _.map(list, function(x){if(x == 'null'){return null} return x});

    var is_null_trans = (type == 'transmissions') && !_.every(list);

    if(is_null_trans) {

        if(_.size(list) == 2) {
            var not_null_trans = _.max(list, Boolean);
            if(not_null_trans == 'mech') null_replace_trans = 'auto';
            if(not_null_trans == 'auto') null_replace_trans = 'mech';
        }

        // удаляем null трансмиссию из списка
        if(_.size(list) == 3) {
            list = _.filter(list);
        }

    }

    for(var i in list){

        raw_value = list[i];
        value = list[i] || 'другое';

        if(type == 'transmissions') {
            if(!raw_value) raw_value = null_replace_trans;
            value = trans[raw_value];
        }

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

    console.log('click_menu: model, type, raw_value:', model, type, raw_value);
    console.log('click_menu: current_choice:', current_choice);

    var subtype, engine, transmission, obj;

    if(type == 'subtypes') {
        subtype = raw_value;

        obj = current_choice[model] || {};
        obj['subtype'] = subtype;
        current_choice[model] = obj;

        var engines = get_engines(all_cars[model], subtype);

        analyze_engines(model, subtype, engines);
    }

    if(type == 'engines') {
        subtype = current_choice[model]['subtype'];
        engine = raw_value;

        obj = current_choice[model] || {};
        obj['engine'] = engine;
        current_choice[model] = obj;

        var transmissions = get_trans(all_cars[model], subtype, engine);

        analyze_trans(model, subtype, engine, transmissions);
    }

    if(type == 'transmissions') {
        subtype = current_choice[model]['subtype'];
        engine = current_choice[model]['engine'];
        transmission = raw_value;

        obj = current_choice[model] || {};
        obj['transmission'] = transmission;
        current_choice[model] = obj;

        set_trans(model, subtype, engine, transmission);
    }

}

/*
 * - выбирает id машин имея полную конфигурацию
 * - переключаемся на меню видов услуг (в URL уже присутствуют выбранные машины)
 */
function set_trans(model, subtype, engine, transmission) {

    console.log('set_trans: current_choice:', current_choice);

    var car, id;
    var cars = all_cars[model];
    var is_subtype, is_engine, is_trans;

    for(var i in cars) {
        car = cars[i];
        id = car['id'];

        is_subtype = !car['subtype'] || car['subtype'] == subtype;
        is_engine = !car['engine'] || car['engine'] == engine;
        is_trans = !car['transmission'] || car['transmission'] == transmission;

        if(is_subtype && is_engine && is_trans) {

            var arr = car_ids[model] || [];
            arr.push(id);
            car_ids[model] = arr;
        }
    }

    var car_model = $('.car-model[data-car-model='+model+']');

    // делаем активным меню выбора услуг
    var choiceContainer = car_model.find('.choice-container');
    choiceContainer.children().each(function(){$(this).removeClass('active')});
    choiceContainer.find('[data-choice-state=2]').addClass('active');

    var ids = car_ids[model];

    var url = 'cars=' + ids.toString();
    choiceContainer.find('[data-choice-state=2] .sub-list a').each(function($index){
        var basic_url = service_urls[model][$index];
        $(this).attr('href', basic_url + '?' + url);
    });

}


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function phone_validate(number) {
    var c = 0;
    var digits = '0123456789';
    for(var i in number) {
        if (digits.indexOf(number[i]) > -1) c++;
    }
    if ((c < 7) || (c > 13)) return false;

    var re_phone = /^(?:\+[0-9]|8)?[ \(-\.]?(?:[0-9]{3,5})?[ \)-\.]?[0-9\.-]+$/i;
    return re_phone.test(number);
}


$(document).ready(function(){

    $.getJSON('/api/cars', {}, function (result) {
        all_cars = result;
    });

    /*
     * запоминаем оригинальные URL услуг
     *
     * service_urls:
     * {'lancer9':  ['/repair', '/tech', ]
     *  'lancer10': ['/repair', '/tech', ]
     * }
     * */
    $('[data-car-model]').each(function(){
        var model = $(this).data('carModel');
        var urls = [];
        $(this).find('[data-choice-state=2] .sub-list a').each(function(){urls.push($(this).attr('href'))});
        service_urls[model] = urls;
    });

    // кнопка: ВЫБРАТЬ
    $('.car-model button').on('click', function(){

        var model = $(this).parents('[data-car-model]').data('carModel');

        if(_.size(all_cars[model]) == 0) {
            var to_services = confirm('К сожалению, для данной модели пока не представлены услуги. Хотите просмотреть весь список услуг ?')
            if(to_services) {
                window.location = '/price/';
            } else {
                return
            }
        }

        var choiceContainer = $(this).parents('.choice-container');
        choiceContainer.children().each(function(){$(this).removeClass('active')});
        choiceContainer.find('[data-choice-state=1]').addClass('active');

        var subtypes = get_subtypes(all_cars[model]);

        analyze_subtypes(model, subtypes);

    });

    // ссылка: "< Назад"
    $('.car-model .choice .back a').on('click', function(){
        var choiceContainer = $(this).parents('.choice-container');
        choiceContainer.children().each(function(){$(this).removeClass('active')});
        choiceContainer.find('[data-choice-state=0]').addClass('active');
        var model = choiceContainer.parent('.car-model').data('carModel');
        car_ids[model] = [];
    });

    /*
       всплывающее окошко: "перезвонить мне"
     */
    $('#header .callme > a').on('click', function(){
        $('#callme').toggle(400);
        $('#phone').focus();
    });

    var send_message = function () {
        // отправить сообщение
        var phoneEl = $('#phone');
        var phone = phoneEl.val();
        phoneEl.val('');
        var csrftoken = getCookie('csrftoken');
        var data = {'phone': phone};

        if(phone_validate(phone)) {
            $.ajax({
                type: 'POST',
                url: '/api/callme/',
                data: data,
                headers: {'X-CSRFToken': csrftoken}
            });
            $('#callme').hide(500);
        } else {
            alert('Введен некорректный номер телефона');
        }

    };

    $('#callme div a').on('click', send_message);
    $('#phone').keypress(function (e) {
        if(e.which == 13){
            send_message();
        }
    });

    $('#callme a.close').on('click', function(){
        $('#callme').toggle(500);
        $('#phone').val('');
    });

});
