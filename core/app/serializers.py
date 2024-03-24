from rest_framework import serializers
from .models import *

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todolist
        fields = ('id','Activity_name','timing' , 'ORDER_STATUS' ,'status','created_at','updated_at')