from django.urls import path
from .import views

urlpatterns = [
    path('', views.AppView),
    path('list/', views.List, name='book-list'),
    path('update/<str:pk>/', views.Update, name='book-update'),
    path('delete/<str:pk>/', views.Delete, name='book-delete')
]
