from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from .serializers import CreateNoteModelSerializer
from note.models import Notes


class NoteViewSet(mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    queryset = Notes.objects.all()
    
    def get_serializer_class(self):
        """Return serializer based on action."""
        action_mappings = {
            'create': CreateNoteModelSerializer,
        }
        return action_mappings.get(self.action, CreateNoteModelSerializer)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response('OK', status=status.HTTP_201_CREATED)
