from django.urls import path,include
from .views import *


urlpatterns=[
    # path('',home,name='home'),
    path('tasks',todolist_api,name='tasks'),
    path('delete-task/<int:id>/',delete_task,name='delete_task'),
]