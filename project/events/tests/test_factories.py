from django.test import TestCase

from project.events.factories import EventFactory, EventRegistrationFactory
from project.events.models import Event, EventRegistration
from project.users.models import User


class EventFactoryTestCase(TestCase):
    def test_event_creation(self):
        self.assertEqual(Event.objects.count(), 0)
        event = EventFactory()
        self.assertIsInstance(event, Event)
        self.assertEqual(Event.objects.count(), 1)


class EventRegistrationFactoryTestCase(TestCase):
    def test_registration_creation(self):
        self.assertEqual(EventRegistration.objects.count(), 0)
        registration = EventRegistrationFactory()
        self.assertIsInstance(registration, EventRegistration)
        self.assertIsInstance(registration.user, User)
        self.assertIsInstance(registration.event, Event)
        self.assertEqual(EventRegistration.objects.count(), 1)
