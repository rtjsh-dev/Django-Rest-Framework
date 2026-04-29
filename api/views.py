from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student

# Create your views here.
def studentsView(request):
  student = Student.objects.all()
  students_list = list(student.values())
  return JsonResponse(students_list, safe=False)