from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('task/<int:task_id>/edit/', views.edit_task_view, name='edit_task'),
    path('task/<int:task_id>/delete/', views.delete_task_view, name='delete_task'),
    path('task/add/', views.add_task_view, name='add_task'),
]
