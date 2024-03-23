from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ExampleConfig(AppConfig):
    name = "project.example"
    label = "example"
    verbose_name = _("Example")
