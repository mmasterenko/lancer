# -*- coding: utf-8 -*-

import os
import csv
from django.conf import settings
from lancerApp.models import Service


def import_service(car_id, stype, fd):
    total = 0
    new = 0
    reader = csv.reader(fd)
    skip_lines = 2
    for row in reader:
        if skip_lines > 0:
            skip_lines -= 1
            continue
        name = row[0]
        if not name:
            continue
        price = row[1].split('/')[0]  # на всякий случай, если в цене есть /
        if not price:
            continue
        price_cons = row[4] if row[4] else 0
        obj, created = Service.objects.get_or_create(car_id=car_id, type=stype, name=name, price=price, price_cons=price_cons)
        total += 1
        if created:
            new += 1
    print 'Total: %s' % total
    print 'New: %s' % new


if __name__ == '__main__':
    stype = 'wheel'
    car_id = 32
    fd = open(os.path.join(settings.BASE_DIR, 'devfiles/Lancer_x_wheel.csv'))

    import_service(car_id, stype, fd)
