from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from project.events.forms import EventRegistrationForm
from project.events.models import Event, EventRegistration


class EventListingView(TemplateView):
    template_name = "events/event_listing.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        events = Event.objects.all()
        context["events"] = events

        return context


class EventRegistrationView(LoginRequiredMixin, CreateView):
    model = EventRegistration
    form_class = EventRegistrationForm
    template_name = "events/event.html"
    success_url = reverse_lazy("home")

    def get_event(self):
        event_id = self.kwargs.get("pk")
        return Event.objects.get(id=event_id)

    def user_has_registered(self, event):
        """
        Check if the user has already registered for the event.
        """
        user = self.request.user
        return EventRegistration.objects.filter(user=user, event=event).exists()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = self.get_event()
        context["event"] = event
        context["user_has_registered"] = self.user_has_registered(event)
        return context

    def form_valid(self, form):
        event = self.get_event()

        if not self.user_has_registered(event):
            form.instance.event = event
            form.instance.user = self.request.user
            messages.add_message(
                self.request,
                messages.SUCCESS,
                f"You have successfully registered for “{event.title}”.",
            )
            return super().form_valid(form)
        else:
            messages.add_message(
                self.request,
                messages.WARNING,
                "You have already registered for this event.",
            )
            return super().form_invalid(form)
