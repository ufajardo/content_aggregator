"""

This is the file that will be used for the functions that will parse websites - it will need to get information
from the database for which websites to look up and how to scrape said websites.

Important libraries:

BeautifulSoup4

def update_time is a temporary function that will updatepy  the time automatically in the DB



"""

from con_agg.models import WebsiteList, Content
from django.utils.timezone import now
from bs4 import BeautifulSoup
from urllib import request



def update_time():
    new_time = WebsiteList.objects.all()
    for item in new_time:
        item.last_update = now()
        item.save()


def cnn_news():
    object = WebsiteList.objects.get(pk=1)

    url = object.web_url
    doc = request.urlopen(url)
    soup = BeautifulSoup(doc, features='html.parser')

    for allh3 in soup.find_all('h3')[:5]:
        for header in allh3:
            Content.objects.create_content(header.text, "https://www.cnn.com"+str(header.get('href')), object)


def fox_news():
    object = WebsiteList.objects.get(pk=2)

    url = object.web_url
    doc = request.urlopen(url)
    soup = BeautifulSoup(doc, features='html.parser')

    for allh3 in soup.find_all('h4')[:5]:
        for header in allh3:
            Content.objects.create_content(header.text, "https://www.cnn.com/"+str(header.get('href')), object)