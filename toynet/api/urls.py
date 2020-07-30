from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('mininet/', include('mininet.urls')),
]