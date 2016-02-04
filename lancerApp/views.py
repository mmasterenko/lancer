from django.shortcuts import render
from .models import GeneralInfo, News, Actions


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


def service(req):
    return render(req, 'lancerApp/service.html')


def price(req, service_type=None):
    return render(req, 'lancerApp/service_table.html')

