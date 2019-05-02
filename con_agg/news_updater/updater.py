"""

updater.py is the actual file that will start running the background process for running the
newsapi.py functions on an interval.

Important libraries:

apscheduler


"""



from apscheduler.schedulers.background import BackgroundScheduler
from con_agg.news_updater.newsapi import reuters_news, cnn_news

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(reuters_news, 'interval', minutes=4)
    scheduler.add_job(cnn_news, 'interval', minutes=5)
    scheduler.start()