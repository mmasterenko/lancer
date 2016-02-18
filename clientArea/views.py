from django.shortcuts import render


def visits(req):
    return render(req, 'clientArea/pages/index.html')


def pages(req, page_name):
    return render(req, 'clientArea/pages/' + page_name)
