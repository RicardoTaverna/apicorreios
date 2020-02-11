from django import forms
from core.models import Cliente

class ClienteForm(forms.ModelForm):
    cep = forms.CharField(widget=forms.TextInput(attrs={'value': '{{ cep.cep }}' }))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    
    class Meta:
        model = Cliente
        fields = "__all__"

    

class testeClienteForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address_1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'value': '{{ cep.logradouro }}'})
    )
    address_2 = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'})
    )
    city = forms.CharField()