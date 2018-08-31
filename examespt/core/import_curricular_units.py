import pandas as pd
from django.core.exceptions import ObjectDoesNotExist

from .models import Course, Institute, CourseUnit


def import_cu(filename, course):
    df = pd.read_excel(filename)
    course = Course.objects.filter(name=course).get()

    for i, line in df.iterrows():
        year = line['Ano'][:1]
        semester = line['Ano'][8:]
        try:
            CourseUnit.objects.filter(name=line['Unidade Curricular']).get()
        except ObjectDoesNotExist:
            CourseUnit.objects.create(name=line['Unidade Curricular'], year=year, semester=semester, course=course)


