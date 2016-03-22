# -*- coding: utf-8 -*-

import os
import csv
from django.conf import settings
from django.db import IntegrityError
from lancerApp.models import Service, Spares, TechLiquids


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


def import_spares(stype, fd):
    total = 0
    new = 0
    errors = 0
    reader = csv.reader(fd)
    skip_lines = 2
    for row in reader:
        if skip_lines > 0:
            skip_lines -= 1
            continue
        name = row[2]
        price = row[3].split('/')[0]  # на всякий случай, если в цене есть /
        price = price if price else 0
        if not name:
            continue
        try:
            obj, created = Spares.objects.get_or_create(name=name, price=price, service_type=stype)
        except Exception:
            created = False
            errors += 1
        total += 1
        if created:
            new += 1
    print 'Total: %s' % total
    print 'New: %s' % new
    print 'Errors: %s' % errors


def import_techliq(fd):
    total = 0
    new = 0
    errors = 0
    reader = csv.reader(fd)
    skip_lines = 2
    for row in reader:
        if skip_lines > 0:
            skip_lines -= 1
            continue
        name = row[5]
        price = row[6].split('/')[0]  # на всякий случай, если в цене есть /
        price = price if price else 0
        if not name:
            continue
        try:
            obj, created = TechLiquids.objects.get_or_create(name=name, price=price)
        except Exception:
            created = False
            errors += 1
        total += 1
        if created:
            new += 1
    print 'Total: %s' % total
    print 'New: %s' % new
    print 'Errors: %s' % errors


def import_bulk(template, test=True):
    L = ['oil', 'brake', 'chassis', 'wheel', 'transmiss', 'engine', 'other']
    for stype in L:
        filename = template.format(stype)
        print filename
        if not test:
            f = open(filename)
            import_techliq(f)


if __name__ == '__main__':
    stype = 'wheel'
    car_id = 32
    fd = open(os.path.join(settings.BASE_DIR, 'devfiles/Lancer_x_wheel.csv'))
    # import_service(car_id, stype, fd)
