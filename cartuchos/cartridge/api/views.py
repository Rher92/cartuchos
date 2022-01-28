from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.authtoken.models import Token
from rest_framework import mixins
from rest_framework import status, viewsets
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend


from cartridge.models import Cartridges
from .serializers.cartridge import CartridgesSerializer

User = get_user_model()


class CartridgeViewSet(mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet):
    serializer_class = CartridgesSerializer
    queryset = Cartridges.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = []
    
