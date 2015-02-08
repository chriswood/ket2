from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from models import UserForm
from django.contrib.auth.models import User, Post
from django.contrib.auth import logout
#from django.contrib.auth.decorators import login_required


def index(request):
    context = {
        'title': 'home',
        'user': request.user.username,
    }
    return render(request, 'index.html', context)

def user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/user/success')
    else:
        form = UserForm()
    context = {'title': 'user stuff', 'form': form}
    return render(request, 'user.html', context)

def register_success(request):
    context = {'title': 'user stuff', 'user': request.user}
    return render(request, 'registered.html', context)

def logout_view():
    logout(request)

def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/user/success')
    else:
        form = PostForm()
    context={'title': 'create post', 'user': request.user}
    return render(request, 'post.html', context)

