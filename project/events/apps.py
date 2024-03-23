from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EventsConfig(AppConfig):
    name = "project.events"
    label = "events"
    verbose_name = _("Events")

    def ready(self):
        import project.events.signals  # noqa F401
