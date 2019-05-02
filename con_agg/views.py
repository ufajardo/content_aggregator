from django.shortcuts import render
from .models import WebsiteList, Content
# Create your views here.

def index(request):
    web_list = WebsiteList.objects.all()
    content_list = Content.objects.all()

    content = {
        "web_list": web_list,
        "content_list": content_list,
    }

    return render(request, 'con_agg/index.html', content)

