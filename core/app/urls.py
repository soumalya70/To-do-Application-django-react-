from django.urls import path,include
from .views import *


urlpatterns=[
    path('',home,name='home'),
    path('tasks',tasks,name='tasks'),
    path('delete-task/<id>/',delete_task,name='delete_task'),
]