from django.urls import path
from . import views


urlpatterns = [
    path('', views.form, name='home'),
    path('update/<str:pk>/', views.Update, name='update-form'),
    path('delete/<str:pk>/', views.Delete, name='delete-item')

]
