from django.contrib import admin

from . import models


# Register your models here.
class NotesAdmin(admin.ModelAdmin):
    # Shows 'title' from notes model on admin page
    list_display = ('title',)


admin.site.register(models.Notes, NotesAdmin)
