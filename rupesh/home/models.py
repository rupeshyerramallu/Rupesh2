from django.db import models
from datetime import datetime


class student(models.Model):
    student_id = models.CharField(max_length=6)
    student_name = models.CharField(max_length=50)

    def __str__(self):
        return self.student_id