from django.core import mail
from django.test import TestCase

from project.events.factories import EventFactory, EventRegistrationFactory
from project.users.factories import UserFactory


class EventRegistrationTestCase(TestCase):
    def test_event_registration_notification_email_sent(self):
        event = EventFactory(title="Test Event")
        user = UserFactory(
            first_name="Jane", last_name="Doe", email="jane@example.co.zm"
        )

        mail.outbox = []

        EventRegistrationFactory(event=event, user=user)

        self.assertEqual(len(mail.outbox), 1)
        sent_email = mail.outbox[0]
        self.assertEqual(sent_email.subject, "Event Registration for Test Event")
        self.assertEqual(sent_email.to, [user.email])
        self.assertIn(
            "Howdy Jane Doe,",
            sent_email.body,
        )
        self.assertIn(
            "you have successfully registered for “Test Event”",
            sent_email.body,
        )
