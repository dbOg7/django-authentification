from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.shortcuts import render, redirect

def registerView(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')
        
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})


class HomeViews(TemplateView):
    template_name: "home.html"
