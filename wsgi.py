import os
import sys

sys.path.append('/var/www/kiteeatingtree.org/')
sys.path.append('/var/www/kiteeatingtree.org/ket2')
os.environ['PYTHON_EGG_CACHE'] = '/var/www/kiteeatingtree.org/.python-egg'
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
