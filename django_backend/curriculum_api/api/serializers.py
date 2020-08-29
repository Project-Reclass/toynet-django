from rest_framework import serializers 
from curriculum_api.models import Module, Submodule_lesson, Submodule_article, Submodule_emulator, Curriculum

class ModuleSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Module
            fields = ['name','id','curriculum_id']

class SubmoduleLessonSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Submodule_lesson
            fields = ["name","module_id",'curriculum_id']

class SubmoduleArticleSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Submodule_article
            fields = ["name","id","module_id",'curriculum_id']

class SubmoduleEmulatorSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Submodule_emulator
            fields = ["name","id","module_id",'curriculum_id']

class CurriculumSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Curriculum
            fields = ["name","id"]