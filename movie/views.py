from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse('<h1>Hola mundo, lo logré</h1>')
    #return render(request, 'home.html')
    return render(request , 'home.html', {'name': 'Isabella Ocampo S'})
    
def about(request):
    return HttpResponse('<h1>Hola, estoy en La subpagina about</h1>')
