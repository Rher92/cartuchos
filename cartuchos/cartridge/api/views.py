from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.authtoken.models import Token
from rest_framework import mixins
from rest_framework import status, viewsets
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend

from .paginations.paginations import ShortCartridgeResultsPagination
from cartridge.models import Cartridges, SubFamily
from .serializers.cartridge import CartridgesSerializer, SubFamilySerializer

User = get_user_model()


class CartridgeViewSet(mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet):
    queryset = Cartridges.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = []
    pagination_class = ShortCartridgeResultsPagination
    
    def get_serializer_class(self):
        """Return serializer based on action."""
        action_mappings = {
            'family': SubFamilySerializer,
        }
        return action_mappings.get(self.action, CartridgesSerializer)
    
    @action(detail=False, methods=['GET'])
    def family(self, *args, **kwargs):
        qs = SubFamily.objects.all()
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)   
