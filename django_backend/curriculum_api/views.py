from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from .api.serializers import ModuleSerializer, SubmoduleLessonSerializer, SubmoduleArticleSerializer, SubmoduleEmulatorSerializer , CurriculumSerializer
from .models import Module, Submodule_lesson, Submodule_article, Submodule_emulator, Curriculum
import json


@api_view(['GET'])
def getModules(request):
    modules = Module.objects.all()
    serializer = ModuleSerializer(modules,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getModule(request,pk):
    module = Module.objects.get(id=pk)
    serializer = ModuleSerializer(module)
    return Response(serializer.data)

@api_view(['POST'])
def updateModule(request,pk):
    module = Module.objects.get(id=pk)
    serializer = ModuleSerializer(instance=module,data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def createModule(request,pk):
    data = json.loads(request.body)
    data['curriculum_id'] = pk
    print(data)
    serializer = ModuleSerializer(data=data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteModule(request,pk):
    module = Module.objects.get(id=pk)
    module.delete()
    return Response('module deleted!')




@api_view(['GET'])
def getSubModuleLessons(request):
    submoduleLessons = Submodule_lesson.objects.all()
    serializer = SubmoduleLessonSerializer(submoduleLessons,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSubModuleLesson(request,pk):
    submoduleLesson = Submodule_lesson.objects.get(id=pk)
    serializer = SubmoduleLessonSerializer(submoduleLesson)
    return Response(serializer.data)

@api_view(['POST'])
def updateSubModuleLesson(request,pk):
    submoduleLesson = Submodule_lesson.objects.get(id=pk)
    serializer = SubmoduleLessonSerializer(instance=submoduleLesson,data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def createSubModuleLesson(request,pk):
    data = json.loads(request.body)
    data['module_id'] = pk
    data['curriculum_id'] = Module.objects.get(id=pk).curriculum_id
    print(data)
    serializer = SubmoduleLessonSerializer(data=data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteSubModuleLesson(request,pk):
    submodule = Submodule_lesson.objects.get(id=pk)
    submodule.delete()
    return Response('lesson deleted!')


@api_view(['GET'])
def getSubModuleArticles(request):
    submoduleArticles = Submodule_lesson.objects.all()
    serializer = SubmoduleArticleSerializer(submoduleArticles,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSubModuleArticle(request,pk):
    submoduleArticle = Submodule_article.objects.get(id=pk)
    serializer = SubmoduleArticleSerializer(submoduleArticle)
    return Response(serializer.data)

@api_view(['POST'])
def updateSubModuleArticle(request,pk):
    submoduleArticle = Submodule_article.objects.get(id=pk)
    serializer = SubmoduleArticleSerializer(instance=submoduleArticle,data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def createSubModuleArticle(request,pk):
    data = json.loads(request.body)
    data['module_id'] = pk
    data['curriculum_id'] = Module.objects.get(id=pk).curriculum_id
    Request.data.module_id = pk
    serializer = SubmoduleArticleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteSubModuleArticle(request,pk):
    submoduleArticle = Submodule_article.objects.get(id=pk)
    submoduleArticle.delete()
    return Response('article deleted!')


@api_view(['GET'])
def getSubModuleEmulators(request):
    submoduleLessons = Submodule_emulator.objects.all()
    serializer = SubmoduleEmulatorSerializer(submoduleLessons,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSubModuleEmulator(request,pk):
    submoduleEmulator = Submodule_emulator.objects.get(id=pk)
    serializer = SubmoduleEmulatorSerializer(submoduleEmulator)
    return Response(serializer.data)

@api_view(['POST'])
def updateSubModuleEmulator(request,pk):
    submoduleEmulator = Submodule_emulator.objects.get(id=pk)
    serializer = SubmoduleEmulatorSerializer(instance=submoduleEmulator,data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def createSubModuleEmulator(request,pk):
    data = json.loads(request.body)
    data['module_id'] = pk
    Request.data.module_id = pk
    serializer = SubmoduleEmulatorSerializer(data=data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteSubModuleEmulator(request,pk):
    submoduleEmulator = Submodule_emulator.objects.get(id=pk)
    submoduleEmulator.delete()
    return Response('emulator deleted!')

@api_view(['GET'])
def getCurriculums(request):
    curriculums = Curriculum.objects.all()
    serializer = CurriculumSerializer(curriculums,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCurriculum(request,pk):
    curriculum = Curriculum.objects.get(id=pk)
    serializer = CurriculumSerializer(curriculum)
    return Response(serializer.data)

@api_view(['POST'])
def updateCurriculum(request,pk):
    curriculum = Submodule_emulator.objects.get(id=pk)
    serializer = CurriculumSerializer(instance=curriculum,data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def createCurriculum(request):
    serializer = CurriculumSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteCurriculum(request,pk):
    curriculum = Submodule_emulator.objects.get(id=pk)
    curriculum.delete()
    return Response('curriculum deleted!')

# Create your views here.
