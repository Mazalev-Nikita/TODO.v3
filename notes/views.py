from rest_framework.generics import ListCreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from notes.models import Note
from notes.serializers import NoteSerializer
from notes.permissions import OnlyAuthorEdit


class NoteListCreate(ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    ordering = ["importance", "complete_date"]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["importance", "complete_date"]


class NoteUpdate(UpdateAPIView):
    permission_classes = [IsAuthenticated & OnlyAuthorEdit]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteDestroy(DestroyAPIView):
    permission_classes = [IsAuthenticated & OnlyAuthorEdit]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


