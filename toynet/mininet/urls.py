from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('show/', views.mininetShow, name='mininet-show'),
]