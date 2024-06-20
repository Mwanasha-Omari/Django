from django.db import models

# Create your models here.
class Teacher(models.Model):
    firstname= models.CharField(max_length=20)
    lastname= models.CharField(max_length=20)
    email= models.EmailField()
    teachers_id= models.PositiveSmallIntegerField()
    phonenumber=models.CharField(max_length=20)
    subject_specialization=models.CharField(max_length=28)
    years_of_experience=models.IntegerField()
    office_hours= models.IntegerField()
    biography=models.TextField(max_length=50)
    course_taught=models.CharField(max_length=20)
    def __str__(self):
        return f"{self.firstname} {self.lastname}"