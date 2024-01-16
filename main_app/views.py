from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Group
from .forms import GroupForm



def home(request):
    return render(request, 'home.html')

def groups_index(request):
    groups = Group.objects.all()
    return render(request, 'groups/groups_index.html', {'groups': groups})

def expenses_index(request):
    expenses = Expense.objects.all()
    return render(request, 'expenses/expenses_index.html', {'expenses': expenses})

class GroupCreateView(CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'groups/create_group.html'
    success_url = reverse_lazy('groups_index')