from django.urls import path
from . import views

urlpatterns = [
    path('', views.Api),
    path('list/', views.List, name='team-list'),
    path('update/<str:pk>/', views.Update, name='team-update')
]
