from django.shortcuts import render
from django.http import Http404
from django.views.generic import DetailView, ListView, CreateView


from .models import Notes


class NotesCreateView(CreateView):
    model = Notes
    # These will be the fields that will be used to input a new note
    fields = ['title', 'text']
    # Once the Note is created, it will redirect to the notes list.
    success_url = '/smart/notes'


class NoteListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
# No need to add 404 information for classes

