from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from models import UserForm

# Create your views here.
def index(request):
    context = {
        'title': 'home',
        'logged_in': True,
    }
    return render(request, 'index.html', context)

def user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
    else:
        form = UserForm()
    context = {'title': 'user stuff', 'form': form}
    return render(request, 'user.html', context)
