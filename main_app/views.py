from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Group, Expense
from .forms import GroupForm, ExpenseForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



def home(request):
    return render(request, 'home.html')

@login_required
def groups_index(request):
    groups = Group.objects.filter(user=request.user)
    return render(request, 'groups/groups_index.html', {'groups': groups})

@login_required
def group_details(request, group_id):
    group = Group.objects.get(id=group_id)
    expenses = Expense.objects.filter(group=group)
    return render(request, 'groups/group_details.html', {'group': group, 'expenses': expenses})

def expenses_index(request):
    expenses = Expense.objects.all()
    return render(request, 'expenses/expenses_index.html', {'expenses': expenses})

def expense_details(request, expense_id):
    expense = Expense.objects.get(id=expense_id)
    return render(request, 'expenses/expense_details.html', {'expense': expense})

def signup(request):
  error_message = ''

  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    
    else:
      error_message = 'Invalid sign up - try again'

  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'groups/create_group.html'
    success_url = reverse_lazy('groups_index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class GroupUpdate(LoginRequiredMixin, UpdateView):
    model = Group
    fields = ['name', 'description', 'members']
    template_name = 'groups/create_group.html'
    success_url = reverse_lazy('groups_index')

    def get_object(self):
       
        return get_object_or_404(Group, id=self.kwargs['group_id'])

class GroupDelete(LoginRequiredMixin, DeleteView):
    model = Group
    success_url = reverse_lazy('groups_index')
    template_name = 'groups/confirm_delete_group.html'

    def get_object(self):
       
        return get_object_or_404(Group, id=self.kwargs['group_id'])
    
class ExpenseCreateView(CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'expenses/create_expense.html'
    success_url = reverse_lazy('expenses_index')


class ExpenseUpdate(UpdateView):
    model = Expense
    form_class = ExpenseForm  
    template_name = 'expenses/create_expense.html'
    success_url = reverse_lazy('expenses_index')

    def get_object(self):
        return get_object_or_404(Expense, id=self.kwargs['expense_id'])

class ExpenseDelete(DeleteView):
    model = Expense
    template_name = 'expenses/confirm_delete_expense.html'
    success_url = reverse_lazy('expenses_index')

    def get_object(self):
        return get_object_or_404(Expense, id=self.kwargs['expense_id'])
