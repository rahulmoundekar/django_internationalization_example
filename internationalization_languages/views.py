from django.shortcuts import render
from django.utils import translation


# Create your views here.
def home(request):
        return render(request, "index.html")
