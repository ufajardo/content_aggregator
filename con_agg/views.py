from django.shortcuts import render
from .models import WebsiteList
# Create your views here.

def index(request):
    web_list = WebsiteList.objects.all()

    content = {
        "web_list": web_list
    }

    return render(request, 'con_agg/index.html', content)

