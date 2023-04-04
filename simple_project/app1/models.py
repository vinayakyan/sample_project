from django.db import models


class Student(models.Model):
    roll = models.PositiveIntegerField()
    name = models.CharField(max_length=20)
    marks = models.FloatField()
