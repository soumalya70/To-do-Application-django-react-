from django.urls import path,include
from .views import *


urlpatterns=[
    path('',tasks,name='tasks'),
    path('delete-task/<id>/',delete_task,name='delete_task'),
]