from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Group, Expense
from decimal import Decimal

class GroupForm(ModelForm):
    members = forms.CharField(
        max_length=100, required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add members (comma-separated)'}),
    )

    class Meta:
        model = Group
        fields = ['name', 'description']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['members'].label = 'Group Members'
        self.user = user

    def filter_members(self, query):
        return User.objects.exclude(id=self.user.id).filter(username__icontains=query)


class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ['group', 'title', 'type', 'description', 'amount']

        widgets = {
            'group': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}), 
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['group'].queryset = user.group_set.all()

    def save(self, commit=True):
        expense = super().save(commit=False)
        members_count = expense.group.members.count()
        expense.divided_amount = Decimal(expense.amount) / members_count if members_count > 0 else Decimal(0)
        if commit:
            expense.save()
        return expense