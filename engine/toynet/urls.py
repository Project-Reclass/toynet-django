from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('config/show/<int:pk>/', views.showToyNetConfig, name='toynetconfig-show'),
    path('session/create', views.createToyNetSession, name='toynetsession-create'),
    path('session/show/<int:pk>/', views.showToyNetSession, name='toynetsession-show'),
]