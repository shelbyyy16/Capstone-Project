from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Group, Expense
from .forms import GroupForm



def home(request):
    return render(request, 'home.html')

def groups_index(request):
    groups = Group.objects.all()
    return render(request, 'groups/groups_index.html', {'groups': groups})

def group_details(request, group_id):
    group = Group.objects.get(id=group_id)
    expenses = Expense.objects.filter(group=group)
    return render(request, 'groups/group_details.html', {'group': group, 'expenses': expenses})

def expenses_index(request):
    expenses = Expense.objects.all()
    return render(request, 'expenses/expenses_index.html', {'expenses': expenses})

class GroupCreateView(CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'groups/create_group.html'
    success_url = reverse_lazy('groups_index')

class GroupUpdate(UpdateView):
    model = Group
    fields = ['name', 'description', 'members']
    template_name = 'groups/create_group.html'
    success_url = reverse_lazy('groups_index')

    def get_object(self):
       
        return get_object_or_404(Group, id=self.kwargs['group_id'])

class GroupDelete(DeleteView):
    model = Group
    success_url = reverse_lazy('groups_index')
    template_name = 'groups/confirm_delete_group.html'

    def get_object(self):
       
        return get_object_or_404(Group, id=self.kwargs['group_id'])
