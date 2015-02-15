from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from ketapp.models import UserForm, UserEditForm, Post, PostForm
from ket2.settings import POST_DISPLAY_LIMIT
import json


@login_required
def index(request, p_count=None):
    '''Display recent posts and site info/announcements.'''
    p_limit = p_count if p_count else POST_DISPLAY_LIMIT
    posts = Post.objects.filter(deleted=False).order_by('-last_edited').all()[:p_limit]
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
    context = {
        'title': 'create post',
        'user': request.user,
        'form': form,
        'button_text': 'create post',
        'verb': 'create'}
    return render(request, 'ket_forms/post.html', context)

@csrf_exempt
def post_delete(request):
    ''' ajax call '''
    #Post.objects.filter(id=post_id).update(deleted=True)
    post_id = request.POST['post_id']
    try:
        obj = Post.objects.get(id=post_id)
        obj.deleted=True
        obj.save()
        return_dict = {'success': True, 'message': 'post deleted'}
    except Post.DoesNotExist:
        return_dict = {'success': False, 'message': 'post not found'}
    json_data = json.dumps(return_dict)
    return HttpResponse(json_data, content_type='application/javascript')

@login_required
def post_edit(request, p_id=None):
    ''' View checks to make sure post belongs to current user. '''
    user_id = request.user.id
    if request.method == 'POST':
        p_id = request.POST['p_id']
        post = Post.objects.get(id=p_id)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    elif p_id:
        post = Post.objects.get(id=p_id)
        if user_id == post.userid.id:
            form = PostForm(instance=post)
        else:
            raise PermissionDenied
    context = {
        'form': form,
        'title': 'edit post',
        'user': request.user,
        'button_text': 'save changes',
        'verb': 'edit',
        'p_id': p_id,
    }
    return render(request, 'ket_forms/post.html', context)
