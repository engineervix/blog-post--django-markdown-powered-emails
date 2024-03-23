import logging

from django.core.management.base import BaseCommand

from project.events.factories import EventFactory

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Create a bunch of Event models for testing
    """

    def handle(self, *args, **options):

        events = EventFactory.create_batch(size=12)
        if events:
            self.stdout.write(
                self.style.SUCCESS(f"Successfully created {len(events)} events")
            )
