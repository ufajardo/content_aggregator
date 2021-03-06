"""

This is the file that will be used for the functions that will parse websites - it will need to get information
from the database for which websites to look up and how to scrape said websites.

Important libraries:

BeautifulSoup4

def update_time is a temporary function that will updatepy  the time automatically in the DB


def site_check is a function that loops through all of the websites in websitelist and uses beautifulsoup to


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


def site_check():
    site_list = WebsiteList.objects.all()

    for x in site_list:
        site_object = WebsiteList.objects.get(web_name=x.web_name)

        url = site_object.web_url
        doc = request.urlopen(url)
        soup = BeautifulSoup(doc, features='html.parser')

        Content.objects.filter(website=x.pk).delete()

        for all_header in soup.find_all(x.header_type)[:5]:
            for header in all_header:
                Content.objects.create_content(header.text, header.get('href'), site_object)

        x.last_update = now()
        x.save()

