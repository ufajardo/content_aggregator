"""

This is the file that will be used for the functions that will parse websites - it will need to get information
from the database for which websites to look up and how to scrape said websites.

Important libraries:

BeautifulSoup4

def update_time is a temporary function that will update the time automatically in the DB



"""

from con_agg.models import WebsiteList

def update_time():
    new_time = WebsiteList.object()