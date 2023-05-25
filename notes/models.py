from django.db import models
from django.contrib.auth.models import User


# Create your models here. these become databases
class Notes(models.Model):
    # these are the attributes of the table
    # name = models.typeOfInput()
    # after writing in your desired attributes
    # run 'python manage.py makemigrations'
    # then 'python manage.py migrate' to finalize it

    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    # when the user is deleted remove all the notes for that user
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
