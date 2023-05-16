from django.apps import AppConfig


class YuyakakeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.yuyakake'

    def ready(self):
        import app.yuyakake.signals
