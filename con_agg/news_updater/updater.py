"""

updater.py is the actual file that will start running the background process for running the
newsapi.py functions on an interval.

Important libraries:

apscheduler


"""



from apscheduler.schedulers.background import BackgroundScheduler
from con_agg.news_updater import newsapi

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(newsapi.cnn_news, 'interval', minutes=1)
    scheduler.start()