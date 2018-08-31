from django.shortcuts import render

# Create your views here.

from django_filters import rest_framework
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Institute, District, Exam, Course, CourseUnit
from rest_framework import viewsets
from .serializer import InstituteSerializer, DistrictSerializer, ExamSerializer, CourseSerializer, \
    InstituteDetailSerializer, CourseUnitSerializer


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer


class InstituteViewSet(viewsets.ModelViewSet):
    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer
    filter_backends = (rest_framework.DjangoFilterBackend, SearchFilter)
    filter_fields = ('district',)
    search_fields = ('name', 'district__name')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = InstituteDetailSerializer(instance)
        return Response(serializer.data)


class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseUnitViewSet(viewsets.ModelViewSet):
    queryset = CourseUnit.objects.all()
    serializer_class = CourseUnitSerializer

