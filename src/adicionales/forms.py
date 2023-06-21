from django import forms
from .models import Adicional

class FormAdicional(forms.ModelForm):
    class Meta:
        model=Adicional
        fields=['nombre','descripcion','precio']