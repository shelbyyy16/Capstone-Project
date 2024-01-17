from django import forms
from django.forms import ModelForm
from .models import Group, Expense

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ['group', 'title', 'type', 'description', 'amount']

        widgets = {
            'group': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }