from django.urls import path
from . import views

urlpatterns = [
  path('students/', views.studentsView),
  path('student/<int:pk>/', views.studentsDetailView),
  path('employees/', views.Employees.as_view()), # This is a class-based view and we are taking the URL pattern to treat this "Employees" as a class-based view
  path('employees/<int:pk>/', views.EmployeeDetail.as_view()),
]