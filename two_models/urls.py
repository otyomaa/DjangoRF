from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import NotesView, TagsView, CombinedView


urlpatterns = [
    path('notes/', NotesView.as_view()),
    path('notes/<int:id>/', NotesView.as_view()),
    path('tags/', TagsView.as_view()),
    path('tags/<int:id>/', TagsView.as_view()),
    path('combined/', CombinedView.as_view(), name='combined-list'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
