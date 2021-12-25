from django.contrib import admin
from django.urls import path
from restapp import views
urlpatterns = [
    path('',views.home),
    path('student/',views.studentjson),
    path('student/<str:pk>',views.students_details)

]