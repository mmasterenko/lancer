from .models import TechLiquids, Spares, Service


def spares_count():
    return Spares.objects.count()


def service_count():
    return Service.objects.count()


def techliquids_count():
    return TechLiquids.objects.count()

