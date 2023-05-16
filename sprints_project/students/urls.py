from django.urls import path, include
from .import views
from .views import StudentList
from .views import StudentCreate
# from django.contrib import admin
# from django.conf.urls import url
# from django.shortcuts import HttpResponse

urlpatterns = [
   path('welcome/',views.Welcome, name='welcome'),
   path('show/',views.Show, name='show'),
   path('list/',views.list_view,name="list"),
   path('list2/', StudentList.as_view(),name="list2"),
   path('create/',StudentCreate.as_view()),
   path('home1/',views.home_view,name="home"),
   path('home2/',views.home_view2,name="home2"),
   #path('home3/',views.home,name='home'),



]