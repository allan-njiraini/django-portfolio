from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request, template_name='index.html')