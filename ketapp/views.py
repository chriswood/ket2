from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from ket2.settings import STATIC_URL

# Create your views here.
def index(request):
    context = {'STATIC_URL': STATIC_URL}
    return render(request, 'index.html', context)
