"""

updater.py is the actual file that will start running the background process for running the
newsapi.py functions on an interval.

Important libraries:

apscheduler


"""


from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from con_agg.newsapi import newsapi

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(newsapi.update_time, 'interval', minutes=1)