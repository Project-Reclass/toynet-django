
from .viewsets import MininetInstanceViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('instance', MininetInstanceViewset)