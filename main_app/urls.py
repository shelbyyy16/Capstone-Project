from django.urls import path
from . import views
	
urlpatterns = [
    path('', views.home, name='home'),
    path('groups/', views.groups_index, name='groups_index'),
    path('expenses/', views.expenses_index, name='expenses_index'), 
    path('create_group/', views.GroupCreateView.as_view(), name='create_group'),
]