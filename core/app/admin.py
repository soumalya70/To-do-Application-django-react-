from django.contrib import admin
from .models import *

# Register your models here.
class Todoadmin(admin.ModelAdmin):
    list_display=['activity_name','timing','status','created_at','updated_at']
admin.site.register(Todolist,Todoadmin)