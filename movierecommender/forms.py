from django import forms
from .models import Movie

class formulario(forms.ModelForm):

    class Meta:
        model = Movie
        fields =['genres']
