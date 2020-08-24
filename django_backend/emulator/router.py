from emulator.api.viewSets import MiniNetViewset, ModuleViewset, SubmoduleViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('mininet',MiniNetViewset)

MoudleRouter = routers.DefaultRouter()
MoudleRouter.register('module',ModuleViewset)


