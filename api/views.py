from django.shortcuts import render
from django.http import JsonResponse, Http404
from students.models import Student
from .serializers import StudentSerializer,EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employees.models import Employee


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

# Class-Based Views  
class Employees(APIView):
  def get(self, request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

  def post(self, request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
class EmployeeDetail(APIView):
  def get_object(self , pk):
    try:
      return Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
      raise Http404
    
  def get(self, request, pk):
    employee = self.get_object(pk)
    serializer = EmployeeSerializer(employee)
    return Response(serializer.data, status=status.HTTP_200_OK)

  def put(self, request, pk):
    employee = self.get_object(pk)
    serializer = EmployeeSerializer(employee, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, pk):
    employee = self.get_object(pk)
    employee.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)