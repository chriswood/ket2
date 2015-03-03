
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.files.base import ContentFile
from ketapp.models import UserForm, UserEditForm, Post, PostForm, CommentForm
from ketapp.models import Comment
from ket2.settings import POST_DISPLAY_LIMIT
from ket2.utils import handle_uploaded_image
import json
import urllib2


@login_required
def index(request, p_count=None):
    '''Display recent posts and site info/announcements.'''
    p_limit = p_count if p_count else POST_DISPLAY_LIMIT
    posts = Post.objects.select_related('comment').order_by('-last_edited').all()[:p_limit]

    context = {
        'title': 'home',
        'user': request.user.username,
        'posts': posts,
        'form': CommentForm(auto_id=False),
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

@login_required
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
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            ob = form.save(commit=False)
            ob.userid_id = cur_user.id
            t = handle_uploaded_image(request.FILES['photo'])
            ob.photo.save(t[0],t[1])
            return HttpResponseRedirect('/')

    else:
        form = PostForm()
    context = {
        'title': 'create post',
        'user': request.user,
        'form': form,
        'button_text': 'create post',
        'verb': 'create'
    }
    return render(request, 'ket_forms/post.html', context)

@csrf_exempt
def post_delete(request):
    ''' ajax call '''
    #Post.objects.filter(id=post_id).update(deleted=True)
    post_id = request.POST['post_id']
    try:
        obj = Post.objects.get(id=post_id)
        obj.delete()
        #obj.save()
        return_dict = {'success': True, 'message': 'post deleted'}
    except Post.DoesNotExist:
        return_dict = {'success': False, 'message': 'post not found'}
    json_data = json.dumps(return_dict)
    return HttpResponse(json_data, content_type='application/javascript')

@csrf_exempt
def comment(request):
    """ajax"""
    form = CommentForm(request.POST)
    if form.is_valid():
        f = form.save(commit=False)
        f.postid_id = request.POST['postid']
        f.message = request.POST['message']
        f.userid_id = request.user.id
        f.save()
        return_dict = {'success': True, 'message': 'comment saved'}
    else:
        return_dict = {'success': False, 'message': 'sumting wong'}
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

def img_upload(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.userid_id = request.user.id
            f.save()
            # handle image stuff
            return HttpResponseRedirect('/upload/image/')
    else:
        form = UploadImageForm()
    context = {
        'form': form,
        'title': 'upload image',
    }
    return render(request, 'ket_forms/upload.html', context)

@login_required
def weather(request, location=None):
    f1 = urllib2.urlopen('http://api.wunderground.com/api/cc79222c4e1f495c/geolookup/conditions/q/TN/Dyersburg.json')
    f2 = urllib2.urlopen('http://api.wunderground.com/api/cc79222c4e1f495c/geolookup/conditions/q/FL/Destin.json')
    json_string1 = f1.read()
    json_string2 = f2.read()
    parsed_json1 = json.loads(json_string1)
    parsed_json2 = json.loads(json_string2)
    f1.close()
    f2.close()
    context = {
        'title': 'your forecast',
        'co_dy': parsed_json1['current_observation'],
        'co_de': parsed_json2['current_observation'],
    }
    return render(request, 'weather.html', context)
