from django.shortcuts import render
from django.shortcuts import HttpResponse
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView


class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'


class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/login.html'
    extra_context = {}


# due to the classes generated above, we do not need this def anymore.

# def home(request):
#     # If you just return an HTTP response, it will return what you added
#     # to access this after running the server: localhost/home
#     # return HttpResponse("Hello Word!")
#
#     # the {} is a way to pass down information from the View to the template
#     return render(request, 'home/welcome.html', {'today': datetime.today()})


# if not logged in to will 404 without arguments.
# In this case we are redirecting we redirect it to admin
# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request, 'home/authorized.html', {})
