from django.urls import path
from . import views
	
urlpatterns = [
    path('', views.home, name='home'),
    path('groups/', views.groups_index, name='index'),
    path('expenses/', views.expenses_index, name='index'),
]