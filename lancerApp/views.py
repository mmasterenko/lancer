from django.shortcuts import render
from .models import GeneralInfo, News, Actions, Service
from collections import OrderedDict


def home(req):
    context = {
        'news': News.objects.order_by('-date', '-id')[:3],
        'info': GeneralInfo.objects.first(),
        'actions': Actions.objects.order_by('-id')
    }
    return render(req, 'lancerApp/home.html', context)


def about(req):
    return render(req, 'lancerApp/about.html')


def map_page(req):
    return render(req, 'lancerApp/map.html')


def news(req):
    return render(req, 'lancerApp/news.html')


def contact(req):
    return render(req, 'lancerApp/contact.html')


def partners(req):
    return render(req, 'lancerApp/partners.html')


def service(req, service_id=None):
    if service_id:
        S = Service.objects.get(pk=service_id)
        context = {'car_model': S.car.name,
                   'service': S,
                   'service_name': S.name,
                   'price_cons': S.price_cons,
                   'spares': S.spares.all(),
                   'techliqs': S.techliq.all()
                   }
        return render(req, 'lancerApp/service_table.html', context=context)
    else:
        return render(req, 'lancerApp/service.html')


def price(req, service_type=None):
    carModels = OrderedDict()
    for S in Service.objects.filter(type=service_type).order_by('car'):
        carModels.setdefault(S.car.name, []).append(S)
    car_models = [{'name': name, 'services': servicelist} for name, servicelist in carModels.items()]
    context = {
        'car_models': car_models,
        'service_type': service_type,
        'service_type_name': Service.type2name(service_type),
    }
    return render(req, 'lancerApp/price_table.html', context=context)

