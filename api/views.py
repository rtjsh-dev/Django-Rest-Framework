from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def studentView(request):
  students = {
    'id': 1,
    'Name': "Rajesh Thapa",
    'Class': "Computer Science"
  }
  return JsonResponse(students)