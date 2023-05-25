from typing import List
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import Http404
# with these imports we can use CRUD (create, Read, Update, Delete)
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
# Login Auth, Check NotesListView for more info
from django.contrib.auth.mixins import LoginRequiredMixin

# Imports we have created using models.py and forms.py
from .models import Notes
from .forms import NotesForm

class NotesDeleteView(LoginRequiredMixin, DeleteView):
    model = Notes
    success_url = '/smart/notes'
    # this template name is required else the delete request cannot complete.
    template_name = 'notes/notes_delete.html'
    login_url = "/admin"


class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model = Notes
    # this comes from forms.py
    form_class = NotesForm
    # Once the Note is created, it will redirect to the notes list.
    success_url = '/smart/notes'
    login_url = "/admin"


class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    # this comes from forms.py
    form_class = NotesForm
    # Once the Note is created, it will redirect to the notes list.
    success_url = '/smart/notes'
    login_url = "login"

    def form_valid(self, form):
        # Don't save the object yet
        self.object = form.save(commit=False)
        # Grab the current user and add it to the object
        self.object.user = self.request.user
        # Now save the Note
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NoteListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    # If User is not Logged in, Redirect
    login_url = "login"

    # Using a site like CCBV.co.uk. this method is used and over written to only show the users notes only
    def get_queryset(self):
        return self.request.user.notes.all()


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
# No need to add 404 information for classes

