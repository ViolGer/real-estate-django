from django import forms
from .models import Property
from property_collections.models import PropertyCollection

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        exclude = ['owner', 'created_at']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class CollectionForm(forms.ModelForm):
    class Meta:
        model = PropertyCollection
        fields = ['name', 'description']
        widgets = {'name':
                   forms.TextInput(attrs={'class': 'form-control'}),
                   'description':
                   forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
                   }