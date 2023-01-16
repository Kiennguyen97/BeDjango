from django.urls import path
from . import views

urlpatterns = [
    path('polls/', views.index, name='index'),
    path('polls/ham1/', views.ham1, name='ham1'),
]