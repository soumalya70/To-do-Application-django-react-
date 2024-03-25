from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages
from .forms import *
from rest_framework import viewsets,generics,status
from django.core.serializers import json
from .serializers import TodoSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


# def home(request):
#     return render(request,"index.html")
# def tasks(request):
#     context={'tasks':Todolist.objects.all()}
#     json_data=json.Serializer().serialize([context])
#     return render(request,'index.html',json_data)
# class TodolistAPIView(generics.ListAPIView):
#     queryset = Todolist.objects.all().order_by('created_at')
#     serializer_class = TodoSerializer
# def create_task(request):
#     context={'form': MyForm, 'tasks':Todolist.objects.all()}
#     if request.method == 'POST':
#         form=MyForm(request.POST)
#         activity_name = request.POST.get('activity_name')
#         if form.is_valid():
#             timing=form.cleaned_data['timing']
#             task_obj = Todolist(activity_name=activity_name, timing=timing)
#             task_obj.save()
#             messages.success(request,"Task added successfully")
#             return redirect("/")

#     return render(request, 'task.html')    
    
# def delete_task(request,id):
#     task_obj = Todolist.objects.get(id=id)
#     if task_obj:
#         task_obj.delete()

@api_view(['GET', 'POST'])
def todolist_api(request):
    if request.method == 'GET':
        tasks = Todolist.objects.all().order_by('created_at')
        serializer = TodoSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def delete_task(request, id):
    try:
        task = Todolist.objects.get(id=id)
    except Todolist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TodoSerializer(task)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
