from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET','POST'])

# Create your views here.
def studentsView(request):
  # Manual Serialization
  # student = Student.objects.all()
  # students_list = list(student.values())
  # return JsonResponse(students_list, safe=False)
  if request.method == "GET":
    # Get all the data from students table
    student = Student.objects.all()
    serializer = StudentSerializer(student, many=True) #many = True for many student table
    return Response(serializer.data, status=status.HTTP_200_OK)
  elif request.method == "POST":
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def studentsDetailView(request, pk):
  try:
    student = Student.objects.get(pk=pk)
  except Student.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == "GET":
    serializer = StudentSerializer(student)
    return Response(serializer.data, status=status.HTTP_200_OK)

  elif request.method == "PUT":
    serializer = StudentSerializer(student, data=request.data) # Passing student as a parameter will mean to update the student table
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    
    else:
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

  elif request.method == "DELETE":
    student.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
    
    