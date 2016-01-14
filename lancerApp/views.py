from django.shortcuts import render


def home(req):
    return render(req, 'lancerApp/home.html')


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


def price(req):
    return render(req, 'lancerApp/service_table.html')

