from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from ketapp.models import UserForm, UserEditForm, Post, PostForm
from ket2.settings import POST_DISPLAY_LIMIT

@login_required
def index(request):
    '''Display recent posts and site info/announcements.'''
    posts = Post.objects.order_by('-last_edited').all()[:POST_DISPLAY_LIMIT]
    context = {
        'title': 'home',
        'user': request.user.username,
        'posts': posts,
    }
    return render_to_response('index.html', context,
                              context_instance=RequestContext(request))

def user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/user/success')
    else:
        form = UserForm()
    context = {'title': 'user stuff', 'form': form}
    return render(request, 'ket_forms/user.html', context)

def user_edit(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/user/edit')
    else:
        cur_user = request.user
        cur_user = User.objects.get(username=cur_user.username)
        form = UserEditForm(instance=cur_user)
    context = {'form': form, 'title': 'edit user'}
    return render(request, 'ket_forms/user_edit.html', context)

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
    context = {'title': 'create post', 'user': request.user, 'form': form}
    return render(request, 'ket_forms/post.html', context)
