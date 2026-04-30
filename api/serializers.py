from rest_framework import serializers
from students.models import Student
from employees.models import Employee

# Same like Django form
class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = "__all__" # All the fields from the model "Student"
    

class EmployeeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Employee
    fields = "__all__"

