from django.urls import path
from . import views

urlpatterns = [
    path('session/create/', views.createToyNetSession, name='toynetsession-create'),
    path('session/show/<int:pk>/', views.showToyNetSession, name='toynetsession-show'),
    path('session/visualize/<int:pk>', views.visualizeToyNetSession, name='toynetsession-visualize'),
    path('session/modify/<int:pk>/', views.modifyToyNetSession, name='toynetsession-modify'),
]