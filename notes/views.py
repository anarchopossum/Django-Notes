from django.shortcuts import render
from django.http import Http404
# with these imports we can use CRUD (create, Read, Update, Delete)
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView

# Imports we have created using models.py and forms.py
from .models import Notes
from .forms import NotesForm

class NotesDeleteView(DetailView):
    model = Notes
    success_url = '/smart/notes'
    # this template name is required else the delete request cannot complete.
    template_name = 'notes/notes_delete.html'


class NotesUpdateView(UpdateView):
    model = Notes
    # this comes from forms.py
    form_class = NotesForm
    # Once the Note is created, it will redirect to the notes list.
    success_url = '/smart/notes'


class NotesCreateView(CreateView):
    model = Notes
    # this comes from forms.py
    form_class = NotesForm
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

