from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User  
from .models import Group, Expense

class GroupForm(ModelForm):
    members = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Group
        fields = ['name', 'description', 'members']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['members'].label = 'Group Members'

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

    def save(self, commit=True):
        expense = super().save(commit=False)
        members_count = expense.group.members.count()
        expense.divided_amount = expense.amount / members_count if members_count > 0 else 0
        if commit:
            expense.save()
        return expense