from django.shortcuts import render
from .models import Search 

# Create your views here.
def home(request):
    return render(request,'base.html')