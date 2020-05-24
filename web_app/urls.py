"""Defines URL patterns for web_app."""

from django.urls import path
from . import views

app_name = 'web_app'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Graph pages
    path('graph/', views.graph, name='graph'),
    path('graph-d-rates/', views.graph_d_rates, name='graph_d_rates'),
]
