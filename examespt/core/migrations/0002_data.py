import csv
import os

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db import migrations


BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def data(apps, schema_editor):
    data_districts(apps)
    data_universities(apps)
    data_institutes(apps)
    data_season(apps)


def data_districts(apps):
    District = apps.get_model('core', 'District')

    with open(os.path.join(BASE_DIR, 'data/districts.csv')) as district_data:
        data = csv.reader(district_data)
        for district in data:
            District.objects.create(name=district[0])


def data_season(apps):
    Season = apps.get_model('core', 'Season')

    data_season = [
        (1, "Época Normal"),
        (2, "Época Recurso"),
        (3, "Época Especial"),
    ]

    for id, name in data_season:
        Season.objects.create(id=id, name=name)


def data_universities(apps):
    University = apps.get_model('core', 'University')
    District = apps.get_model('core', 'District')
    with open(os.path.join(BASE_DIR, 'data/institute_course.csv')) as institute_course_data:
        data = csv.reader(institute_course_data)
        for univ, course in data:
            with open(os.path.join(BASE_DIR, 'data/districts.csv')) as district_data:
                d_data = csv.reader(district_data)
                for district in d_data:
                    if district[0] in univ:
                        dist_obj = District.objects.filter(name=district[0]).get()
                        split = univ.split('-')
                        if len(split) == 2:
                            try:
                                University.objects.get(name=split[0])
                            except ObjectDoesNotExist:
                                University.objects.create(name=split[0], location=dist_obj)


def data_institutes(apps):
    University = apps.get_model('core', 'University')
    Institute = apps.get_model('core', 'Institute')
    with open(os.path.join(BASE_DIR, 'data/institute_course.csv')) as institute_course_data:
        data = csv.reader(institute_course_data)
        for univ, course in data:
            split = univ.split('-')
            if len(split) == 2:
                try:
                    un_obj = University.objects.get(name=split[0])
                except ObjectDoesNotExist:
                    un_obj = None
                try:
                    Institute.objects.get(name=split[1])
                except ObjectDoesNotExist:
                    Institute.objects.create(name=split[1], university=un_obj)
            elif len(split) == 1:
                try:
                    Institute.objects.get(name=split[0])
                except ObjectDoesNotExist:
                    Institute.objects.create(name=split[0], university=None)


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(data, migrations.RunPython.noop)
    ]
