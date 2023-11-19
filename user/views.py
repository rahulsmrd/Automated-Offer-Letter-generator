from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import *
from user.forms import *
# Create your views here.

def SignUp(request):
    if request.method == 'POST':
        user_form=UserCreateForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect(reverse_lazy("user:login"))
    return render(request, 'user_data/signup.html',{'Userform':UserCreateForm})

class LogIn(TemplateView):
    template_name='user_data/login.html'
