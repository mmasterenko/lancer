from django.shortcuts import render
from .models import GeneralInfo, News, Actions, Service


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
    S = None
    services = Service.objects.filter(type=service_type)
    services = [{
                    'self': S,
                    'id': S.id,
                    'name': S.name,
                    'price': S.price,
                    'price_materials': sum([
                                            sum([spare.price for spare in S.spares.all()]),
                                            sum([tl.price for tl in S.techliq.all()]),
                                            S.price_cons if S.price_cons else 0
                                        ])
                } for S in services]
    context = {
        'services': services,
        'service_type': service_type,
        'service_type_name': S.type_name if S else '',
        'car_model': S.car.name if S else ''
    }
    return render(req, 'lancerApp/price_table.html', context=context)

