from django.shortcuts import render
from .forms import ContactoForm

# Create your views here.

def index(request):
    data = {
        'form' : ContactoForm()
    }
    
    if request.method == 'POST' : 
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid(): 
            formulario.save() 
            data["mensaje"] = "Contacto Guardado"
        else: 
            data["form"] = formulario
    return render(request, "polls/index.html" , data)

def viviendasmobile(request):
    return render(request, "polls/viviendasmobile.html")

def industriasmobile(request):
    return render(request, "polls/industriasmobile.html")

def edificiosmobile(request):
    return render(request, "polls/edificiosmobile.html")
