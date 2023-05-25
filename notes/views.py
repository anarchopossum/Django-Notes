from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView, DetailView, ListView, UpdateView


from .models import Notes
from .forms import NotesForm


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

