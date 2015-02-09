from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from models import UserForm, Post, PostForm
from django.contrib.auth.models import User
from django.contrib.auth import logout, get_user, get_user_model
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    context = {
        'title': 'home',
        'user': request.user.username,
    }
    return render_to_response('index.html', context, context_instance=RequestContext(request))
    #return render(request, 'index.html', context)

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

def user_edit(request):
    if request.method == 'POST':
        form = 3
        if form.is_valid():
            q=1
            return HttpResponseRedirect('/user/edit')
    else:
        cur_user = request.user
        cur_user = User.objects.get(username=cur_user.username)
        #data = {cur_user.}
        form = UserForm(instance=cur_user)
        context = {'form': form, 'title': 'edit user'}
        return render(request, 'user.html', context)

def register_success(request):
    context = {'title': 'user stuff', 'user': request.user}
    return render(request, 'registered.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def post(request):
    # see if user is not anonymous
    cur_user = request.user
    if cur_user.is_anonymous():
        return HttpResponseRedirect('/login')
    #cur_user = User.objects.get(id=2)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.userid_id = cur_user.id
            f.save()
            return HttpResponseRedirect('/')
    else:
        form = PostForm()
    context={'title': 'create post', 'user': request.user, 'form': form}
    return render(request, 'post.html', context)

