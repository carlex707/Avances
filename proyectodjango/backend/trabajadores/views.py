from django.shortcuts import render
from .models import Empleado
#def home(request):

    #return render(request, 'index.html')

def home(request):
    qempleados = Empleado.objects.all()
    context = {
        'empleados': qempleados
    }
    return render(request, 'index.html', context)

