from django.shortcuts import render


def visits(req):
    return render(req, 'clientArea/pages/index.html')
