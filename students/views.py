from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def students(request):
  students = [
    {"id":1, "Name": "Rajesh Thapa", "Age": 22}
  ]
  return HttpResponse(students)