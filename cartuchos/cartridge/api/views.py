from unicodedata import name
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.authtoken.models import Token
from rest_framework import mixins
from rest_framework import status, viewsets
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend

from .paginations.paginations import ShortCartridgeResultsPagination
from cartridge.models import Cartridges, SubFamily, Family
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
    
    def filter_queryset(self, queryset):
        """
        Given a queryset, filter it with whichever filter backend is in use.
        You are unlikely to want to override this method, although you may need
        to call it either from a list view, or from a custom `get_object`
        method if you want to apply the configured filtering backend to the
        default queryset.
        """
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset
 
    def customized_filter(self, request):
        qs = self.get_queryset()
        fin = request.query_params.get('family_intern__name', None)
        fn = request.query_params.get('family__name', None)
        
        if (hasattr(fin, 'lower') and fin.lower() != 'todos'):
            qs = qs.filter(family_intern__name=fin)
        if (hasattr(fn, 'lower') and fn.lower() != 'todos'):
            qs = qs.filter(family__name=fn)
            
        return qs
        
 
    def list(self, request, *args, **kwargs):
        qs = self.customized_filter(request)
        queryset = self.filter_queryset(qs)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['GET'])
    def subfamily(self, *args, **kwargs):
        qs = SubFamily.objects.all()
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)   
    
    @action(detail=False, methods=['GET'])
    def subfamily_name(self, *args, **kwargs):
        qs = SubFamily.objects.all()
        _return = ['TODOS']
        for item in qs:
            _return.append(item.name)
        return Response(_return)   
    
    @action(detail=False, methods=['GET'])
    def family_name(self, *args, **kwargs):
        qs = Family.objects.all()
        _return = ['TODOS']
        for item in qs:
            _return.append(item.name)
        return Response(_return)   
