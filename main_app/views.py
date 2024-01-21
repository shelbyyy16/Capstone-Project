from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Group, Expense
from .forms import GroupForm, ExpenseForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Sum, Q




def home(request):
    return render(request, 'home.html')

@login_required
def groups_index(request):

    groups = Group.objects.filter(Q(user=request.user) | Q(members=request.user)).distinct()

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

    #This is a method that gets called when the form submitted by the user is valid.
    def form_valid(self, form):

    # It assigns the user who is currently logged in (self.request.user) to the user field of the form instance.
        form.instance.user = self.request.user

    #Retrieves the cleaned data from the 'members' field of the form.(comma-separated string of usernames)   
        members_str = form.cleaned_data['members']

    #Splits the string of usernames into a list, removing leading and trailing whitespaces from each username.
        members_list = [username.strip() for username in members_str.split(',') if username.strip()]

    #Fetches a queryset of User objects whose usernames match those in the members_list.    
        members_queryset = User.objects.filter(username__in=members_list)

    # Save the form instance before setting many-to-many relationship
        response = super().form_valid(form)

    #After saving the form instance, it sets the many-to-many relationship for the 'members' field of the Group model.
        form.instance.members.set(members_queryset)
   
        return response

    #method is used to pass additional keyword arguments to the form(This is used to identify the current logged in user)
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
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

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['group'].queryset = self.request.user.group_set.all()
        return form

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
