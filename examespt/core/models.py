from django.db import models

# Create your models here.


class BaseClass(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class District(BaseClass):
    pass


class Season(BaseClass):
    pass


class Institute(BaseClass):
    district = models.ForeignKey(District)


class Course(BaseClass):
    institute = models.ForeignKey(Institute, related_name='courses')

    def __str__(self):
        return self.institute.name + ' - ' + self.name


class CourseUnit(BaseClass):
    course = models.ForeignKey(Course, related_name='courseunits')
    semester = models.PositiveSmallIntegerField()
    year = models.SmallIntegerField()


class Exam(BaseClass):
    courseunit = models.ForeignKey(CourseUnit)
    season = models.ForeignKey(Season)
    year = models.SmallIntegerField()


class Question(models.Model):
    exam = models.ForeignKey(Exam)
    text = models.CharField(max_length=100, blank=False, null=False)
    number = models.SmallIntegerField(blank=False, null=False)
