from django.db import models
from django.db.models.functions import Now

# Create your models here.

class Todolist(models.Model):
    activity_name=models.CharField(max_length=100)
    timing = models.TimeField(db_default=Now())
    ORDER_STATUS=((0,'Started'),(1,'Finished'))
    status=models.SmallIntegerField(choices=ORDER_STATUS,default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def get_time_without_am_pm(self):
        return self.timing.strftime('%H:%M')
    def __str__(self):
        return self.activity_name