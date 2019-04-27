from django.apps import AppConfig


class ConAggConfig(AppConfig):
    name = 'con_agg'

    def ready(self):
        from con_agg.news_updater import updater
        updater.start()
