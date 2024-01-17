from django.forms import ModelForm
from .models import Group, Expense

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description']

class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ['group', 'title', 'type', 'description', 'amount']