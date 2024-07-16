from django.db import models

from django.db import models

class ClassPeriod(models.Model):
  start_time= models.IntegerField()
  end_time= models.IntegerField()
  course=models.TextField()
  class_teacher= models.TextField()
  class_room= models.TextField()
  day_of_the_week= models.TextField()
  def __str__(self):
    return f"{self.s_time}"




