from django.shortcuts import render
from django.http import Http404


from .models import Notes


# Create your views here.


def list(request):
    # grab all items from the database this database was generated in Models
    # then after the migration commands passed
    # generated database configs are in /migrations/
    # then once finalized through the second migration command it's finally added to the DB
    # From here all_notes grabs from the database.
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})


# This next def will help display the contents of the notes
# to see the notes refer to the GitHub comments on when this section was generated
def detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note does not exist.")
    return render(request, 'notes/notes_detail.html', {'note': note})
