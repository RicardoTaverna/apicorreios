from django import forms
from .models import contato

class contatoForm(forms.ModelForm):

    class Meta:
        model = contato
        fields = '__all__'