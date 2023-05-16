from django.db import models

# Create your models here.
class Student(models.Model):
	f_name = models.CharField(max_length=255)
	l_name = models.CharField(max_length=255)
	gender = models.CharField(max_length=2)
	age = models.IntegerField()
	birth_date = models.DateField()

class Course(models.Model):
	name = models.CharField(max_length=255)
	num_students = models.IntegerField()
	
class Post(models.Model):
    Male = 'M'
    FeMale = 'F'
    GENDER_CHOICES = (
        (Male, 'Male'),
        (FeMale, 'Female'),
    )

    username = models.CharField(max_length=20, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default=Male)
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
    	return f"{self.username}"