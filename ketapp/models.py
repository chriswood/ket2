from django.db.models import CharField, EmailField, TextField, BooleanField
from django.db.models import DateTimeField, ForeignKey, Model, ImageField
from django.core.validators import validate_email, MinValueValidator
from django import forms
from django.contrib.auth.models import User
from ket2.settings import MEDIA_ROOT

#  USE auth_users!!!!!!!!! #
class UserCustom(Model):
    firstname = CharField('first name', max_length=40)
    lastname = CharField('last name', max_length=40)
    email = EmailField('email', max_length=100, validators=[validate_email])
    username = CharField('username', max_length=20, validators=[MinValueValidator(3)])
    password = CharField('password', max_length=50, validators=[MinValueValidator(4)])

    class Meta:
        db_table = 'users_custom'

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class Post(Model):
    userid = ForeignKey(User)
    title = CharField('title', max_length=80)
    message = TextField('message', max_length=500)
    created = DateTimeField(auto_now_add=True)
    last_edited = DateTimeField(auto_now=True)
    deleted = BooleanField(default=False)
    photo = ImageField(null=True, blank=True)

    class Meta:
        db_table = 'posts'

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['photo'].label = 'image (optional)'
        
    class Meta:
        model = Post
        exclude = ['created', 'last_edited', 'userid', 'deleted']

class Comment(Model):
    postid = ForeignKey(Post, related_name='comment')
    userid = ForeignKey(User, related_name='comment')
    message = TextField('message', max_length=500)
    created = DateTimeField(auto_now_add=True)
    last_edited = DateTimeField(auto_now=True)
    deleted = BooleanField(default=False)

    class Meta:
        db_table = 'comments'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']
        widgets = {
          'message': forms.Textarea(attrs={'rows': 2, 'cols': 60}),
        }
