from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import Student
from .serializers import StudentSerializer
from teacher.models import Teacher
from .serializers import TeacherSerializer
from classperiod.models import ClassPeriod
from .serializers import ClassPeriodSerializer
# from class.models import Class
from .serializers import ClassSerializer
from course.models import Course




class StudentListView(APIView):
    def get(self,request):
        students=Student.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data)
    
class TeacherListView(APIView):
    def get(self,request):
        teachers=Teacher.objects.all()
        serializer=TeacherSerializer(teachers,many=True)
        return Response(serializer.data)

class ClassPeriodListView(APIView):
    def get(self,request):
        classperiods=ClassPeriod.objects.all()
        serializer=ClassPeriodSerializer(classperiods,many=True)
        return Response(serializer.data)

# class ClassListView(APIView):
#     def get(self,request):
#         classes = Class.objects.all()
#         serializer=ClassSerializer(classes,many=True)
#         return Response(serializer.data)   

class CourseListView(APIView):
    def get(self,request):
        courses = Course.objects.all()
        serializer=Course(courses,many=True)
        return Response(serializer.data)     

                     


    



