from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UtilsConfig(AppConfig):
    name = "project.utils"
    label = "utils"
    verbose_name = _("Utils")
