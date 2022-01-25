from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from cartuchos.users.api.views import UserViewSet
from cartuchos.clients.api.view import ClientsViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("clients", ClientsViewSet)


app_name = "api"
urlpatterns = router.urls
