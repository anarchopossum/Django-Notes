from django import forms

from .models import Notes


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        # Widgets can inject CSS
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'text': forms.Textarea(attrs={'class': 'form-control my-5'})
        }
        # Labels can overwrite names within fields
        labels = {
            'text': "Write your thoughts here"

        }
    # Here we pass the title and clean the data so lets say if a link was placed here,
    # it won't take you to lets say google.com
    # We have also added an If to later get a catch to raise any errors and fail the Note creation/edit
    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            # raise ValidationError('We only accept notes about Django!')
            pass
        return title
