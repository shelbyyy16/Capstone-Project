from django.urls import path
from . import views
	
urlpatterns = [
    path('', views.home, name='home'),
    path('groups/', views.groups, name='groups'),
    path('expenses/', views.expenses, name='expenses'),
]