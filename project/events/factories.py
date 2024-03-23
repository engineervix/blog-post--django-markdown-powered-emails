import factory
from django.utils import timezone

from project.events.models import Event, EventRegistration
from project.users.factories import UserFactory


class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Event

    title = factory.Faker("sentence")
    description = factory.Faker("text")
    location = factory.Faker("address")
    date_and_time = factory.Faker(
        "date_time_this_year",
        tzinfo=timezone.get_current_timezone(),
        before_now=False,
        after_now=True,
    )


class EventRegistrationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = EventRegistration

    event = factory.SubFactory(EventFactory)
    user = factory.SubFactory(UserFactory)
