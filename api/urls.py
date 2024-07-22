from django.urls import path
from api.views import StudentListView
from api.views import ClassListView
from api.views import CourseListView
from api.views import TeacherListView
from api.views import StudentDetailView
from api.views import ClassPeriodListView
from api.views import TeacherDetailView


urlpatterns=[
    path("student/",StudentListView.as_view(),name="student_list_view"),
    path("classperiod/",ClassPeriodListView.as_view() , name="classperiod_list_view"),
    path("class/" ,ClassListView.as_view() ,name='class_list_view'),
    path("course/" ,CourseListView.as_view() ,name='course_list_view'),
    path("teachers/" , TeacherListView.as_view() ,name='teacher_list_view'),
    path("students/<int:id>/",StudentDetailView.as_view(),name='Student_detail_view'),
    path("classperiod/<int:id>/",ClassPeriodDetailView.as_view(),name="classperiod_detail_view"),
    path("teacher/<int:id>/", TeacherDetailView.as_view(), name="teacher_detail_view")

]

