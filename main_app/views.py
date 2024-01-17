from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Group, Expense
from .forms import GroupForm, ExpenseForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum



def home(request):
    return render(request, 'home.html')

@login_required
def groups_index(request):
    groups = Group.objects.filter(user=request.user)
    
    group_data = []
    for group in groups:
        expenses = Expense.objects.filter(group=group)
        total_owed = expenses.aggregate(Sum('divided_amount'))['divided_amount__sum'] or 0
        group_data.append({'group': group, 'total_owed': total_owed})

    return render(request, 'groups/groups_index.html', {'group_data': group_data})


@login_required
def group_details(request, group_id):
    group = Group.objects.get(id=group_id)
    expenses = Expense.objects.filter(group=group)

    group_total = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    total_owed = expenses.aggregate(Sum('divided_amount'))['divided_amount__sum'] or 0

    return render(request, 'groups/group_details.html', {
        'group': group,
        'expenses': expenses,
        'group_total': group_total,
        'total_owed': total_owed,
    })

@login_required
def expenses_index(request):
    expenses = Expense.objects.filter(group__user=request.user)
    return render(request, 'expenses/expenses_index.html', {'expenses': expenses})

@login_required
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
            return redirect('home')
        else:
            # Retrieve and display form errors
            error_message = 'Invalid sign up - try again'
            form_errors = form.errors
    else:
        form = UserCreationForm()
        form_errors = None

    context = {'form': form, 'error_message': error_message, 'form_errors': form_errors}
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
    
class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'expenses/create_expense.html'
    success_url = reverse_lazy('expenses_index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExpenseUpdate(LoginRequiredMixin, UpdateView):
    model = Expense
    form_class = ExpenseForm  
    template_name = 'expenses/create_expense.html'
    success_url = reverse_lazy('expenses_index')

    def get_object(self):
        return get_object_or_404(Expense, id=self.kwargs['expense_id'])

class ExpenseDelete(LoginRequiredMixin, DeleteView):
    model = Expense
    template_name = 'expenses/confirm_delete_expense.html'
    success_url = reverse_lazy('expenses_index')

    def get_object(self):
        return get_object_or_404(Expense, id=self.kwargs['expense_id'])
