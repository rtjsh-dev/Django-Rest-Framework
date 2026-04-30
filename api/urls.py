from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# Creating router class
router = DefaultRouter()
router.register('employees', views.EmployeeViewset, basename='employee')


urlpatterns = [
  path('students/', views.studentsView),
  path('student/<int:pk>/', views.studentsDetailView),
  # This is a class-based view and we are taking the URL pattern to treat this "Employees" as a class-based view
  # path('employees/', views.Employees.as_view()), 
  # path('employees/<int:pk>/', views.EmployeeDetail.as_view()),
  path('', include(router.urls)),

  path('blogs/', views.BlogsView.as_view()),
  path('comments/', views.CommentsView.as_view()),

  path('blogs/<int:pk>/', views.BlogDetailView.as_view()),
  path('comments/<int:pk>/', views.CommentDetailView.as_view()),
]