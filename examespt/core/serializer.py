from .models import Institute, District, Exam, Course, CourseUnit
from rest_framework import serializers


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('id', 'name')


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ('id', 'name', 'course')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name')


class CourseUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseUnit
        fields = ('id', 'name', 'course', 'semester', 'year')


class CourseDetailSerializer(serializers.ModelSerializer):
    institute = serializers.StringRelatedField()
    courseunits = CourseUnitSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'name', 'institute', 'courseunits')


class InstituteSerializer(serializers.ModelSerializer):
    district = serializers.StringRelatedField()

    class Meta:
        model = Institute
        fields = ('id', 'name', 'district')


class InstituteDetailSerializer(serializers.ModelSerializer):
    district = serializers.StringRelatedField()
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Institute
        fields = ('id', 'name', 'district', 'courses')
