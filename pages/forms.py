from django import forms
from .models import CodingGame

class CodingGameForm(forms.ModelForm):
    class Meta:
        model = CodingGame
        fields = ['title', 'description', 'difficulty', 'time_estimated', 'code_snippet', 'image', 'is_enabled']
