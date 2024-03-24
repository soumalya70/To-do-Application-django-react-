from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages
from .forms import *
from rest_framework import viewsets
from .serializers import TodoSerializer
# Create your views here.


def home(request):
    return render(request,"index.html")
def tasks(request):
    context={'tasks':Todolist.objects.all()}
    return render(request,'task.html',context)
def create_task(request):
    context={'form': MyForm, 'tasks':Todolist.objects.all()}
    if request.method == 'POST':
        form=MyForm(request.POST)
        activity_name = request.POST.get('activity_name')
        if form.is_valid():
            timing=form.cleaned_data['timing']
            task_obj = Todolist(activity_name=activity_name, timing=timing)
            task_obj.save()
            messages.success(request,"Task added successfully")
            return redirect("/")

    return render(request, 'task.html')    
    
def delete_task(request,id):
    task_obj = Todolist.objects.get(id=id)
    if task_obj:
        task_obj.delete()