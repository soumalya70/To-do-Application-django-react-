from django.forms import TimeInput
from django import forms
from .models import *
class TimeWithoutAMPMInput(TimeInput):
    format = '%H:%M'

class MyForm(forms.ModelForm):
    class Meta:
        model=Todolist
        timing = forms.TimeField(widget=TimeWithoutAMPMInput())
        fields=['activity_name','timing','status']
    

