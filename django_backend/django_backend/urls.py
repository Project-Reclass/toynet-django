"""django_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from emulator.router import router, MoudleRouter
from curriculum_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mininet/',include(router.urls)),
    path('module/',views.createModule, name='module'),
    path('module/getmodules',views.getModules, name='getmodules'),
    path('module/update/<str:pk>/',views.updateModule, name='updateModule'),
    path('module/getmodule/<str:pk>/',views.getModule, name='getmodule'),
    path('module/delete/<str:pk>/',views.deleteModule, name='deleteModule'),

    path('submodule/getsubmodules/',views.getSubModules, name='getSubModuleS'),
    path('submodule/getsubmodule/<str:pk>/',views.getSubModule, name='getSubModule'),
    path('submodule/',views.createSubModule, name='createSubModule'),
    path('submodule/update/<str:pk>/',views.updateSubModule, name='updateSubModule'),
    path('submodule/delete/<str:pk>/',views.deleteSubModule, name='deleteSubModule')
    

]
  