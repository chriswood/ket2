"""Custom template filters"""
from django import template
from hashlib import md5
from ket2.settings import MEDIA_URL, MEDIA_ROOT

register = template.Library()

def gravaturl(email, s='100'):
    '''Return url wuth or without default'''
    param = md5(email.strip().lower()).hexdigest()
    return "http://www.gravatar.com/avatar/{0}?d=monsterid&s={1}".format(param, s)

register.filter('gravaturl', gravaturl)

def imgurl(image):
    """Return full image path"""
    return(MEDIA_URL+image.name)

register.filter('imgurl', imgurl)
