from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('lesson/', include('lesson.urls')),
    path('toynet/', include('toynet.urls')),
    path('article/', include('article.urls')),
    path('quiz/', include('quiz.urls')),
]