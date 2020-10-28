from django.apps import AppConfig


class DbAppConfig(AppConfig):
    name = 'DB_app'
    label = 'DB_app_label'

    def ready(self):
        import DB_app.signals_handlers