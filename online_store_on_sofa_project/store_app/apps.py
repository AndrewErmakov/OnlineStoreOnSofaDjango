from django.apps import AppConfig


class StoreAppConfig(AppConfig):
    name = 'store_app'

    def ready(self):
        from . import signals
        return signals
