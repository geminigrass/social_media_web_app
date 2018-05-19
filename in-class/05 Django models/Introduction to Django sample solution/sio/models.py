from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
    andrew_id = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.andrew_id


class Course(models.Model):
    course_id = models.CharField(max_length=50)
    course_name = models.CharField(max_length=50)
    instructor = models.CharField(max_length=50)

    def __unicode__(self):
        return self.course_id