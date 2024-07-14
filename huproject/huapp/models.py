from django.db import models


class StudentData(models.Model):
    name = models.CharField(max_length=100)
    standard = models.CharField(max_length=100)
    section = models.CharField(max_length=100)


class TeachertData(models.Model):
    name = models.CharField(max_length=100)
    ClassTeacherOF = models.CharField(max_length=100)
    Salary = models.CharField(max_length=100)
