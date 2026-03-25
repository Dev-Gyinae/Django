from django import forms
from .models import item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = item
        fields = ['name', 'description', 'price', 'image', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border'}),
            'description': forms.Textarea(attrs={'class': 'w-full px-4 py-3 rounded-xl border'}),
            'price': forms.NumberInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border'}),
            'image': forms.ClearableFileInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border'}),
            'category': forms.Select(attrs={'class': 'w-full px-4 py-3 rounded-xl border'}),
        } 

class EditItemForm(forms.ModelForm):
    class Meta:
        model = item
        fields = ['name', 'description', 'price', 'image', 'is_sold']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border'}),
            'description': forms.Textarea(attrs={'class': 'w-full px-4 py-3 rounded-xl border'}),
            'price': forms.NumberInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border'}),
            'image': forms.ClearableFileInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border'}),

        } 