from django.apps import AppConfig


class DemoConfig(AppConfig):
    name = 'Demo'

    def ready(self):
        import Demo.signals