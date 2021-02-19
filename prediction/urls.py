from django.urls import path
from . import views

urlpatterns = [
    path('breast-predict/', views.index, name='predicting-stock'),
]
