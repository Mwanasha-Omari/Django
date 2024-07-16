from rest_framework import serializers
from student.models import Student
from teacher.models import Teacher
from classperiod.models import ClassPeriod
# from class.models import Class
from course.models import Course






class StudentSerializer(serializers.modelserializer):
    class Meta:
        model=Student
        fields="__all__"


class ClassPeriodSerializer(serializers.modelserializer):
    class Meta:
        model=ClassPeriod
        fields="__all__"

class TeacherSerializer(serializers.modelserializer):
    class Meta:
        model=Teacher
        fields="__all__"

class  CourseSerializer(serializers.modelserializer):
    class Meta:
        model= Course
        fields="__all__"

# class  ClassSerializer(serializers.modelserializer):
#     class Meta:
#         model= Class
#         fields="__all__"        

     

