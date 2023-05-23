from django.shortcuts import render
from django.shortcuts import HttpResponse
from datetime import datetime

# Create your views here.
def home(request):
    # If you just return an HTTP response, it will return what you added
    # to access this after running the server: localhost/home
    # return HttpResponse("Hello Word!")

    # the {} is a way to pass down information from the View to the template
    return render(request, 'home/welcome.html', {'today': datetime.today()})