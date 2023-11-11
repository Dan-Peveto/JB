from django.db import models
import datetime

# Pathways del (SCA / CAD / Cyber)
class Pathway(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Student Model
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)
    pathway = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# The Jobs!
class Job(models.Model):
    job_title = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    salary = models.CharField(max_length=50, default='Not Posted')
    location = models.CharField(max_length=50, default='Seattle')
    description = models.TextField(max_length=500, default='See Post')
    link = models.URLField()
    pathway = models.ForeignKey(Pathway, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'{self.job_title} {self.company}'

# Jobs applied for
class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_applied = models.DateField(default=datetime.datetime.today)
    status = models.CharField(max_length=50, default='', blank=True)

    def __str__(self):
        return f'{self.job}'