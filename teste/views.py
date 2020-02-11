from django.shortcuts import render
from django.http import HttpResponse
from .models import contato
from .forms import contatoForm


def contato(request):
    if request.method == 'POST':
        form = contatoForm(request.POST)
        if form.is_valid():
            form.save()
            print("Form VALIDO")

    
    form = contatoForm()
    return render(request, 'teste/cadastro.html', {'form': form})