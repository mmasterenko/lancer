# -*- coding: utf-8 -*-

from collections import OrderedDict
from smspilot import Sender
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import GeneralInfo, News, Actions, Service, Stuff, Car, CAR_TYPE, SERVICE_TYPE, Diagnostic
from .forms import MailForm


@ensure_csrf_cookie
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


def contact(request):
    if request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            gi_record = GeneralInfo.objects.first()
            subject = gi_record.subject
            sender = gi_record.sender
            recipient = gi_record.recipient
            recipients = [recipient]

            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            From = form.cleaned_data['email']
            message = u'Имя: %s \n' % name
            message += u'E-mail: %s \n' % From
            message += u'Телефон: %s \n\n' % (phone if phone else u'не указан')
            message += form.cleaned_data['message']

            send_mail(subject, message, sender, recipients)

            return HttpResponseRedirect(reverse('mail_result', kwargs={'result': 'success'}))
        else:
            return HttpResponseRedirect(reverse('mail_result', kwargs={'result': 'error'}))
    return render(request, 'lancerApp/contact.html')


def mail_result(req, result=None):
    return render(req, 'lancerApp/mail_result.html', {'success': result == 'success'})


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


def price_diagnostic(request, service_type='to'):
    cars_id = request.GET.get('cars')
    diagnostics = Diagnostic.objects.select_related('car').all()
    if cars_id:
        diagnostics = diagnostics.filter(car__id__in=cars_id.split(','))

    car_diag = OrderedDict()
    for D in diagnostics:
        try:
            name = D.car.name
        except AttributeError:
            name = u'<а/м не указан>'
        car_diag.setdefault(name, []).append(D)

    car_diagnostics = [{'name': name, 'diagnostics': D_list} for name, D_list in car_diag.items()]

    context = {
        'car_diagnostics': car_diagnostics,
        'service_type_name': Service.type2name(service_type)
    }
    return render(request, 'lancerApp/price_diagnostic.html', context=context)


def price(request, service_type=None):
    if service_type == 'to':
        return price_diagnostic(request, 'to')

    if service_type:
        services = Service.objects.filter(type=service_type).order_by('car')
    else:
        services = Service.objects.order_by('car')

    cars_id = request.GET.get('cars')
    if cars_id:
        services = services.filter(car__id__in=cars_id.split(','))

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
    return render(request, 'lancerApp/price_table.html', context=context)


def api_cars(req):
    result = {}
    cars = Car.objects.all()
    for t in CAR_TYPE:
        car_type = t[0]
        result[car_type] = list(cars.filter(type=car_type).values())
    return JsonResponse(result)


def api_callme(request):
    phone = request.POST.get('phone')

    gi_record = GeneralInfo.objects.first()
    is_smsing = gi_record.is_smsing
    sms_phone = str(gi_record.sms_phone)
    apikey = gi_record.apikey

    if is_smsing:
        if not sms_phone or not apikey:
            return HttpResponse('some settings wrong')
        to = sms_phone.translate(None, '-+.() ')
        msg = u'%s попросил перезвонить (лансер-сервис)' % phone

        pilot = Sender(apikey)
        pilot.addSMS(1, to, msg)
        result = pilot.send()

        return HttpResponse('ok')
    else:
        return HttpResponse('sms disabled')
