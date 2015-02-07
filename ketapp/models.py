from django.db import models
from django.core.validators import validate_email, MinValueValidator, MinValueValidator
from django.forms import ModelForm

class User(models.Model):
    firstname = models.CharField('first name', max_length=40)
    lastname = models.CharField('last name', max_length=40)
    email = models.EmailField('email', max_length=100, validators=[validate_email])
    username = models.CharField('username', max_length=20, validators=[MinValueValidator(3)])
    password = models.CharField('password', max_length=50, validators=[MinValueValidator(4)])

    class Meta:
        db_table = 'users'

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        #exclude = ['title']

