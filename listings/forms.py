from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        exclude = ['owner', 'created_at']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
