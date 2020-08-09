from .viewsets import ToyNetConfigViewset, ToyNetSessionViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('toynetconfig', ToyNetConfigViewset)
router.register('toynetsession', ToyNetSessionViewset)
