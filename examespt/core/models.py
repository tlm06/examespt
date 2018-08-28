from django.db import models

# Create your models here.


class BaseClass(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class District(BaseClass):
    pass


class University(BaseClass):
    location = models.ForeignKey(District)


class Institute(BaseClass):
    university = models.ForeignKey(University, null=True)


class Course(BaseClass):
    institute = models.ForeignKey(Institute)


class Exam(BaseClass):
    course = models.ForeignKey(Course)
    semester = models.PositiveSmallIntegerField()


class Question(models.Model):
    exam = models.ForeignKey(Exam)
    text = models.CharField(max_length=100)
