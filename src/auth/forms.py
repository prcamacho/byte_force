from django import forms


class FormClienteAuth(forms.Form):
    dni=forms.IntegerField(label='DNI')

