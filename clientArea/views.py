# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.core.urlresolvers import reverse
from .models import CustomUser, Visit


def visits(request):
    if request.user.is_authenticated() and isinstance(request.user, CustomUser):
        context = {
            'visits': Visit.objects.filter(customer=request.user),
            'user': request.user
        }
        return render(request, 'clientArea/pages/index.html', context=context)
    else:
        return HttpResponseRedirect(reverse('login'))


def login_view(request):
    if request.method == 'POST':
        car_number = request.POST['login']
        password = request.POST['password']
        user = authenticate(car_number=car_number, password=password)
        if user and isinstance(user, CustomUser):
            login(request, user)
        else:
            return HttpResponseForbidden(u'Неверный логин или пароль')
        if request.user.is_authenticated() and isinstance(request.user, CustomUser):
            return HttpResponseRedirect(reverse('visits'))
        else:
            return render(request, 'clientArea/pages/login.html')
    else:
        return render(request, 'clientArea/pages/login.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


# def pages(req, page_name):
#     return render(req, 'clientArea/pages/' + page_name)
