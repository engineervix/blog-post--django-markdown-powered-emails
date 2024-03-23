from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm as DefaultAuthenticationForm
from django.contrib.auth.forms import UserChangeForm as DefaultUserChangeForm
from django.contrib.auth.forms import UserCreationForm as DefaultUserCreationForm

from project.users.models import User


class UserCreationForm(DefaultUserCreationForm):
    class Meta(DefaultUserCreationForm.Meta):
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
        )


class UserChangeForm(DefaultUserChangeForm):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
        )


class AuthenticationForm(DefaultAuthenticationForm):
    def confirm_login_allowed(self, user):
        super().confirm_login_allowed(user)
        messages.add_message(self.request, messages.SUCCESS, "Welcome to Project!")
