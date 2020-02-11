from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.forms import ClienteForm, testeClienteForm
from core.models import Cliente
import requests

def home(request):
    cep = {}
    if 'inputcep' in request.GET:
        inputcep = request.GET['inputcep']
        url = 'https://viacep.com.br/ws/%s/json/' %inputcep
        response = requests.get(url)
        cep = response.json()
    return render(request, 'core/home.html', {'cep': cep})

def cliente(request):
    cep = {}
    if 'inputcep' in request.GET:
        inputcep = request.GET['inputcep']
        url = 'https://viacep.com.br/ws/%s/json/' %inputcep
        response = requests.get(url)
        cep = response.json()

    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            print('form validado')
               
    
    form = ClienteForm()
    context = {
        'cep': cep,
        'form': form
    }
    return render(request,'core/cliente.html', context)


def show(request):
    clientes = Cliente.objects.all()
    return render(request,'core/show.html')


def edit(request, id):
    cliente = Cliente.objects.get(id=id)
    return render(request,'core/edit.html', {'cliente': cliente})


def update(request, id):
    cliente = Cliente.objects.get(id=id)    
    form = ClienteForm(request.POST, instance = cliente)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, 'core/edit.html', {'cliente':cliente})


def destroy(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('/show')