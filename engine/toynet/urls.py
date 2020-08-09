from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('session/create', views.createToyNetSession, name='toynet-create'),
    path('session/show/<int:pk>/', views.showToyNetSession, name='toynet-show'),
]