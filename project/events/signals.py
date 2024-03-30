from django.db.models.signals import post_save
from django.dispatch import receiver

from project.events.models import EventRegistration
from project.utils.mail import send_email


@receiver(post_save, sender=EventRegistration)
def send_email_notification(sender, instance, created, **kwargs):
    if created:
        send_email(
            subject=f"Event Registration for {instance.event.title}",
            to_email_list=[instance.user.email],
            template="events/event_registration_notification_email.txt",
            context={"event": instance.event, "user": instance.user},
            md_to_html=True,
        )
