from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from student.models import Student
from .serializers import StudentSerializer
from teacher.models import Teacher
from .serializers import TeacherSerializer
from classperiod.models import ClassPeriod
from .serializers import ClassPeriodSerializer
# from .serializers import Class
# from .serializers import ClassSerializer
from course.models import Course
from .serializers import Course







class StudentListView(APIView):
    
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class StudentDetailView(APIView):
        def get(self,request,id):
            student=Student.objects.get(id=id)
            serializer=StudentSerializer(student)
            return Response(serializer.data)
        def put(self,request,id):
            student=Student.objects.get(id=id)
            serializer=StudentSerializer(student,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.data,status=status.HTTP_400_BAD_RREQUEST)
            
        def delete(self,request,id):
             student=Student.objects.get(id=id)
             student.delete()
             return Response(status=status.HTTP_202_ACCEPTED)

    
class TeacherListView(APIView):
    def get(self,request):
        teachers=Teacher.objects.all()
        serializer=TeacherSerializer(teachers,many=True)
        return Response(serializer.data)
    
class TeacherDetailView(APIView):
    def get(self,request,id):
            teacher =Teacher.objects.get(id=id)
            serializer=TeacherSerializer(teacher)
            return Response(serializer.data)
    
    def put(self,request,id):
            teacher=Teacher.objects.get(id=id)
            serializer=TeacherSerializer(teacher,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.data,status=status.HTTP_400_BAD_RREQUEST)
            
    def delete(self,request,id):
             student=Teacher.objects.get(id=id)
             student.delete()
             return Response(status=status.HTTP_202_ACCEPTED)
    
class ClassPeriodDetailView(APIView):
    def get(self,request,id):
            classperiod =ClassPeriodDetailView.objects.get(id=id)
            serializer=ClassPeriodSerializer(classperiod)
            return Response(serializer.data)
    
    def put(self,request,id):
            classperiod=ClassPeriod.objects.get(id=id)
            serializer=ClassPeriodSerializer(classperiod,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.data,status=status.HTTP_400_BAD_RREQUEST)
            
    def delete(self,request,id):
             student=ClassPeriod.objects.get(id=id)
             student.delete()
             return Response(status=status.HTTP_202_ACCEPTED)    


class ClassPeriodListView(APIView):
    def get(self,request):
        classperiods=ClassPeriod.objects.all()
        serializer=ClassPeriodSerializer(classperiods,many=True)
        return Response(serializer.data)

class ClassListView(APIView):
    def get(self,request):
        classes = Class.objects.all()
        serializer=ClassSerializer(classes,many=True)
        return Response(serializer.data)   

class CourseListView(APIView):
    def get(self,request):
        courses = Course.objects.all()
        serializer=Course(courses,many=True)
        return Response(serializer.data)     

                     


    









