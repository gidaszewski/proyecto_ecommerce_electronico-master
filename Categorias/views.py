from django.shortcuts import render

# Create your views here.

def categorias(request):
    return render(request, 'Categorias/categorias.html')