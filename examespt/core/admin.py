from django.contrib import admin

# Register your models here.
from examespt.core.models import District, Institute, Course, Exam


class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class InstituteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class ExamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(District, DistrictAdmin)
admin.site.register(Institute, InstituteAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Exam, ExamAdmin)
