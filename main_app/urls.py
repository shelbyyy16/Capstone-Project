from django.urls import path
from . import views
	
urlpatterns = [
    path('', views.home, name='home'),
    path('groups/', views.groups_index, name='groups_index'),
    path('create_group/', views.GroupCreateView.as_view(), name='create_group'),
    path('groups/<int:group_id>/', views.group_details, name='group_details'),
    path('groups/<int:group_id>/update/', views.GroupUpdate.as_view(), name='group_update'),
    path('groups/<int:group_id>/delete/', views.GroupDelete.as_view(), name='group_delete'),
    path('expenses/', views.expenses_index, name='expenses_index'), 
    path('create_expense/', views.ExpenseCreateView.as_view(), name='create_expense'),
    path('expenses/<int:expense_id>/', views.expense_details, name='expense_details'),
    path('expenses/<int:expense_id>/update/', views.ExpenseUpdate.as_view(), name='expense_update'),
    path('expenses/<int:expense_id>/delete/', views.ExpenseDelete.as_view(), name='expense_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]