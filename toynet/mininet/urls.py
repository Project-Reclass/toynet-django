from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('showall/', views.mininetShowall, name='mininet-showall'),
    path('<int:pk>/', views.mininetShow),
]
