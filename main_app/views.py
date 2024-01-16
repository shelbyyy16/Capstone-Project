from django.shortcuts import render, redirect
from .models import Group, Expense
from .forms import GroupForm



def home(request):
    return render(request, 'home.html')

def groups_index(request):
    groups = Group.objects.all()
    return render(request, 'groups/groups_index.html', {'groups': groups})

def expenses_index(request):
    expenses = Expense.objects.all()
    return render(request, 'expenses/expenses_index.html', {'expenses': expenses})

def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            new_group = form.save()
            return redirect('groups_index')  
    else:
        form = GroupForm()

    return render(request, 'create_group.html', {'form': form})