from django.shortcuts import render
from .models import Employees

# Create your views here.

def home(request):
    emp = Employees.objects.all()
    context = {
        'emp': emp

    }
    return render(request, 'rest/index.html', context)
