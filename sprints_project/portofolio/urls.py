from django.urls import path 
from .import views
from .views import StudentList

urlpatterns = [

path("cv/",views.cv, name='cv'),
path("course/",views.course),
path('student/', StudentList.as_view()),
path('home/',views.home,name='home'),
path('home_list/',views.home_list,name='home_list'),
]