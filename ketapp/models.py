from django.db.models import CharField, EmailField, TextField, BooleanField
from django.db.models import DateTimeField, ForeignKey, Model
from django.core.validators import validate_email, MinValueValidator
from django.forms import ModelForm, PasswordInput
from django.contrib.auth.models import User

#  USE auth_users!!!!!!!!! #
class UserCustom(Model):
    firstname = CharField('first name', max_length=40)
    lastname = CharField('last name', max_length=40)
    email = EmailField('email', max_length=100, validators=[validate_email])
    username = CharField('username', max_length=20, validators=[MinValueValidator(3)])
    password = CharField('password', max_length=50, validators=[MinValueValidator(4)])

    class Meta:
        db_table = 'users_custom'

class UserEditForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        widgets = {
            'password': PasswordInput(),
        }

class Post(Model):
    userid = ForeignKey(User)
    title = CharField('title', max_length=80)
    message = TextField('message', max_length=500)
    created = DateTimeField(auto_now_add=True)
    last_edited = DateTimeField(auto_now=True)
    deleted = BooleanField(default=False)

    class Meta:
        db_table = 'posts'

class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['created', 'last_edited', 'userid', 'deleted']
