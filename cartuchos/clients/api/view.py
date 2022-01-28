from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.authtoken.models import Token
from rest_framework import mixins
from rest_framework import status, viewsets
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend



from clients.models import Cliente
from .serializers.serializers import ClientAllSerializer, ClientShortSerializer, ClientLargeSerializer

User = get_user_model()


class ClientsViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = ClientAllSerializer
    queryset = Cliente.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['cifrc', 'nombre_razon_social__nombre']

    def get_serializer_class(self):
        """Return serializer based on action."""
        action_mappings = {
            'short': ClientShortSerializer,
            'list': ClientShortSerializer,
            'retrieve': ClientLargeSerializer,
        }
        return action_mappings.get(self.action, ClientAllSerializer)

    @action(detail=False, methods=['GET'])
    def short(self, *args, **kwargs):
        # import pdb; pdb.set_trace()
        if param := self.request.query_params.get('cifrc'):
            queryset = Cliente.objects.filter(cifrc__icontains=param)
        elif param := self.request.query_params.get('nombre_razon_social__nombre'):
            queryset = Cliente.objects.filter(nombre_razon_social__nombre__icontains=param)
        else: 
            queryset = Cliente.objects.all()
                
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)