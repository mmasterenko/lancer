from lancerApp.models import Service


def update_services():
    services = Service.objects.all()
    for service in services:
        service.car_name = service.car.name
        print '%s\t\t%s' % (service.car_name, service.name)
        service.save()
