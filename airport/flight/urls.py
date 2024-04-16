from django.urls import path

from . import views

app_name = 'flight'

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail')    
]