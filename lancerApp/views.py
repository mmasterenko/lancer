from django.shortcuts import render


def makeup(req):
    return render(req, 'lancerApp/makeup.html')


def home(req):
    return render(req, 'lancerApp/home.html')

