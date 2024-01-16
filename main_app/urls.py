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
]