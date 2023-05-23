from django.shortcuts import render
from django.shortcuts import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    # If you just return an HTTP response, it will return what you added
    # to access this after running the server: localhost/home
    # return HttpResponse("Hello Word!")

    # the {} is a way to pass down information from the View to the template
    return render(request, 'home/welcome.html', {'today': datetime.today()})

# if not logged in to will 404 without arguments.
# In this case we are redirecting we redirect it to admin
@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'home/authorized.html', {})