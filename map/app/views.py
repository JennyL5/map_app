import os
from django.shortcuts import render


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATICFILES_DIRS = os.path.join(BASE_DIR, 'static')

# Create your views here.
def data_view(request, *args, **kwargs):
    return render(request, "data.html", {"data" : 0})
