from django.urls import path

from . import views

urlpatterns = [
    path('notes', views.NoteListView.as_view(), name='notes.list'),
    # <int:pk> means the numerical value for the note
    path('notes/<int:pk>', views.NotesDetailView.as_view(), name="notes.detail"),
    path('notes/<int:pk>/edit', views.NotesUpdateView.as_view(), name="notes.update"),
    path('notes/<int:pk>/Delete', views.NotesDeleteView.as_view(), name="notes.delete"),
    path('notes/new', views.NotesCreateView.as_view(), name="notes.new"),
]
