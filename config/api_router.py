from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from cartuchos.users.api.views import UserViewSet
from cartuchos.clients.api.view import ClientsViewSet
from cartuchos.cartridge.api.views import CartridgeViewSet
from cartuchos.note.api.views import NoteViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("clients", ClientsViewSet)
router.register("cartridges", CartridgeViewSet)
router.register("notes", NoteViewSet)


app_name = "api"
urlpatterns = router.urls
