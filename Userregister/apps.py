from django.apps import AppConfig


class UserregisterConfig(AppConfig):
    name = 'Userregister'

    def ready(self):
        import Userregister.signals