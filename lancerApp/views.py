# -*- coding: utf-8 -*-

from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import JsonResponse
from .models import GeneralInfo, News, Actions, Service, Stuff, Car, CarGroupOrder, CAR_TYPE, SERVICE_TYPE
from collections import OrderedDict


def home(req):
    service_types = [{'code': code, 'name': name} for code, name in SERVICE_TYPE]
    context = {
        'news': News.objects.order_by('-date', '-id')[:3],
        'info': GeneralInfo.objects.first(),
        'actions': Actions.objects.order_by('-id'),
        'service_types': service_types
    }
    return render(req, 'lancerApp/home.html', context)


def about(req):
    pagntr = Paginator(Stuff.objects.all(), 4)
    context = {
        'staff_rows': [pagntr.page(N).object_list for N in pagntr.page_range],
        'about_company': GeneralInfo.objects.first().about
    }
    return render(req, 'lancerApp/about.html', context=context)


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
        context = {
            'service': S,
            'spares': S.spares.all(),
            'techliqs': S.techliq.all()
        }
        return render(req, 'lancerApp/service_table.html', context=context)
    else:
        return render(req, 'lancerApp/service.html')


def price(req, service_type=None):
    if service_type:
        services = Service.objects.filter(type=service_type).order_by('car')
    else:
        services = Service.objects.order_by('car')
    carModels = OrderedDict()
    for S in services:
        try:
            name = S.car.name
        except AttributeError:
            name = u'<а/м не указан>'
        carModels.setdefault(name, []).append(S)
    car_models = [{'name': name, 'services': servicelist} for name, servicelist in carModels.items()]
    context = {
        'car_models': car_models,
        'service_type': service_type,
        'service_type_name': Service.type2name(service_type) if service_type else u'Все',
    }
    return render(req, 'lancerApp/price_table.html', context=context)


class CarTypeGroup:
    def __init__(self, obj_list):
        self.result = {}

        self.get_subtypes(obj_list)
        self.get_engines(obj_list)
        self.get_transmission(obj_list)
        self.get_transmission_2(obj_list)

    def get_result(self):
        return self.result

    def get_subtypes(self, obj_list):
        for obj in obj_list:
            subtype = obj.subtype
            subtype = subtype if subtype else 'all'
            self.result[subtype] = {}

    def get_engines(self, obj_list):
        for obj in obj_list:
            subtype = obj.subtype
            engine = obj.engine
            subtype = subtype if subtype else 'all'
            engine = engine if engine else 'all'
            self.result[subtype][engine] = {}

    def get_transmission(self, obj_list):
        for obj in obj_list:
            subtype = obj.subtype
            engine = obj.engine
            transmission = obj.transmission
            subtype = subtype if subtype else 'all'
            engine = engine if engine else 'all'
            transmission = transmission if transmission else 'all'
            self.result[subtype][engine][transmission] = [obj.id]

    def get_transmission_2(self, obj_list):
        for obj in obj_list:
            subtype = obj.subtype
            engine = obj.engine
            transmission = obj.transmission
            subtype = subtype if subtype else 'all'
            engine = engine if engine else 'all'
            transmission = transmission if transmission else 'all'
            try:
                if transmission in ('auto', 'mech'):
                    all_trans = self.result[subtype][engine]['all']
                    self.result[subtype][engine][transmission].extend(all_trans)
            except KeyError:
                pass


def api_cars(req):
    result = {}
    cars = Car.objects.all()
    for t in CAR_TYPE:
        car_type = t[0]
        result[car_type] = list(cars.filter(type=car_type).values())
    return JsonResponse(result)
