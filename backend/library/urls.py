# events/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='library'),
    path('<int:pk>/', views.library_detail, name='library_detail'),  # new detail view
]
