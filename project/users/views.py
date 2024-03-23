from django.contrib import messages
from django.contrib.auth.views import LogoutView as DjangoLogoutView


class LogoutView(DjangoLogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.add_message(
            self.request, messages.SUCCESS, "You have been logged out of Project!"
        )
        return super().dispatch(request, *args, **kwargs)
