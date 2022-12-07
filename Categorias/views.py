from django.shortcuts import render
from Categorias.models import *

# Create your views here.

def categorias(request):
    categorias=TCategorias.objects.all()
    return render(request,'Categorias/categorias.html', {"categorias":categorias})