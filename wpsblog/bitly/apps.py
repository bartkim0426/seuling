from django.apps import AppConfig


class BitlyAppConfig(AppConfig):
    name = "bitly"

    def ready(self):
        from bitly.signals.post_save_bitlink import post_save_bitlink
