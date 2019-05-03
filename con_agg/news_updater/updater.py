"""

updater.py is the actual file that will start running the background process for running the
newsapi.py functions on an interval.

Important libraries:

apscheduler


"""



from apscheduler.schedulers.background import BackgroundScheduler
from con_agg.news_updater.newsapi import reuters_news, cnn_news, site_check

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(site_check, 'interval', minutes=4)
    scheduler.start()