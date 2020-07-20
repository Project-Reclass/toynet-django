from emulator.api.viewSets import MiniNetViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('mininet',MiniNetViewset)
