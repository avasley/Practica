from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.

layout = """
    <h1> Examen final [LP3] | RVZ </h1>
    <hr/>
    <ul>
        <li>
            <a href="/Cursos"> Cursos</a>
        </li>
        <li>
            <a href="/Crearcurso"> Crear Curso</a>
        </li>
        <li>
            <a href="/Carreras"> Carreras</a>
        </li>
        <li>
            <a href="/Crearcarrera"> Crear Carreras</a>
        </li>
    </ul>
    <hr/>
"""

def Cursos(request):
    mensaje = "Listado de Cursos"
    return render(request, 'Cursos.html')

def Crearcurso(request):
    mensaje = "Agregar Cursos"
    return render(request, 'Crearcurso.html')

def Carreras(request):
    mensaje = "Listado de Carreras"
    return render(request, 'Carreras.html')

def Crearcarrera(request):
    mensaje = "Agregar Carreras"
    return render(request, 'Crearcarrera.html')
