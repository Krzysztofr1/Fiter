from django import forms
from .models import SurveyData

class SurveyForm(forms.ModelForm):
    class Meta:
        model = SurveyData
        fields = ['body_mass', 'height', 'body_fat', 'cell_mass', 'fat_free_mass', 'muscle_mass']
        widgets = {
            'body_fat': forms.NumberInput(attrs={'placeholder': 'Wartość opcjonalna'}),
            'cell_mass': forms.NumberInput(attrs={'placeholder': 'Wartość opcjonalna'}),
            'fat_free_mass': forms.NumberInput(attrs={'placeholder': 'Wartość opcjonalna'}),
            'muscle_mass': forms.NumberInput(attrs={'placeholder': 'Wartość opcjonalna'}),
        }