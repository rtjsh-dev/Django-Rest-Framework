from django.http import HttpResponse

def home(request):
  return HttpResponse('<h2>This is homepage.</h2>')