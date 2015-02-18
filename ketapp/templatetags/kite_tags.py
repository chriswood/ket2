"""Custom template filters"""
from django import template
from hashlib import md5

register = template.Library()

def gravaturl(email, default='monsterid'):
    '''Return url wuth or without default'''
    param = md5(email.strip().lower()).hexdigest()
    return "http://www.gravatar.com/avatar/{0}?d={1}&s=100".format(param, default)

register.filter('gravaturl', gravaturl)
