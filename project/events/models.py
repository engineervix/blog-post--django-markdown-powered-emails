from django.db import models
from django.urls import reverse
from django.utils import timezone

from project.users.models import User


class Event(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    date_and_time = models.DateTimeField()

    @property
    def is_past(self):
        return self.date_and_time < timezone.now()

    def get_absolute_url(self):
        return reverse("event-registration", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["-date_and_time"]

    def __str__(self):
        return self.title


class EventRegistration(models.Model):
    registration_date = models.DateTimeField(auto_now_add=True)

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="event_registrations"
    )

    class Meta:
        ordering = ["-registration_date"]
        constraints = [
            models.UniqueConstraint(
                fields=["event", "user"], name="unique_registration"
            )
        ]

    def __str__(self):
        return f"{self.user} » {self.event}"
