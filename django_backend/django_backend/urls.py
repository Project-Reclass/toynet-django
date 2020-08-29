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

    path('curriculum/get/',views.getCurriculums, name='getCurriculums'),
    path('curriculum/get/<str:pk>/',views.getCurriculum, name='getCurriculum'),
    path('curriculum/create/',views.createCurriculum, name='createSubModuleEmulator'),
    path('curriculum/update/<str:pk>/',views.updateCurriculum, name='updateCurriculum'),
    path('curriculum/<str:pk>/',views.deleteCurriculum, name='deleteCurriculum'),
    
    path('module/<str:pk>/',views.createModule, name='module'),
    path('module/getmodules',views.getModules, name='getmodules'),
    path('module/update/<str:pk>/',views.updateModule, name='updateModule'),
    path('module/getmodule/<str:pk>/',views.getModule, name='getmodule'),
    path('module/delete/<str:pk>/',views.deleteModule, name='deleteModule'),

    path('submodule/lessons/get/',views.getSubModuleLessons, name='getSubModulelessons'),
    path('submodule/lessons/get/<str:pk>/',views.getSubModuleLessons, name='getSubModulelesson'),
    path('submodule/lessons/<str:pk>/',views.createSubModuleLesson, name='createSubModulelesson'),
    path('submodule/lessons/update/<str:pk>/',views.updateSubModuleLesson, name='updateSubModulelesson'),
    path('submodule/lessons/delete/<str:pk>/',views.deleteSubModuleLesson, name='deleteSubModulelesson'),
    
    path('submodule/articles/get/',views.getSubModuleArticles, name='getSubModuleArticles'),
    path('submodule/articles/get/<str:pk>/',views.getSubModuleArticle, name='getSubModuleArticle'),
    path('submodule/articles/<str:pk>/',views.createSubModuleArticle, name='createSubModuleArticle'),
    path('submodule/articles/update/<str:pk>/',views.updateSubModuleArticle, name='updateSubModuleArticle'),
    path('submodule/articles/delete/<str:pk>/',views.deleteSubModuleArticle, name='deleteSubModuleArticle'),

    path('submodule/emulator/get/',views.getSubModuleEmulator, name='getSubModuleEmulator'),
    path('submodule/emulator/get/<str:pk>/',views.getSubModuleEmulator, name='getSubModuleEmulator'),
    path('submodule/emulator/<str:pk>/',views.createSubModuleEmulator, name='createSubModuleEmulator'),
    path('submodule/emulator/update/<str:pk>/',views.updateSubModuleEmulator, name='updateSubModuleEmulator'),
    path('submodule/emulator/<str:pk>/',views.deleteSubModuleEmulator, name='deleteSubModuleEmulator')
]
  