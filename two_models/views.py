from rest_framework import filters, generics
from .models import Notes, Tags
from .serializers import NotesSerializer, TagsSerializer, CombinedSerializer
from django.db.models import Prefetch


class NotesView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    """ Используем все объекты Notes, применяем фильтры поиска и сортировки """
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['Title']
    ordering_fields = ['Created_Ad']
    lookup_field = 'id'

    def perform_create(self, serializer):
        serializer.save()


class TagsView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    """ Используем все объекты Tags, применяем фильтры поиска и сортировки """
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    searching_fields = ['Tag_Name']
    ordering_fields = ['Description']
    lookup_field = 'id'

    def perform_create(self, serializer):
        serializer.save()


class CombinedView(generics.ListAPIView):
    """ Получение комбинированных данных заметок и тегов """
    serializer_class = CombinedSerializer

    def get_queryset(self):
        """ Получение списка заметок и связанных с ним тегов """
        return Notes.objects.prefetch_related(
            Prefetch('tags', queryset=Tags.objects.only('Tag_Name'))
        ).all()

