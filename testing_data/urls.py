# testing_data/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_test_result, name='add_test_result'),
    path('list/', views.test_result_list, name='test_result_list'),
]