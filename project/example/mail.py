from typing import List, Optional

from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


def send_email(
    subject: str,
    to_email_list: List[str],
    template: str,
    context: Optional[dict] = None,
) -> None:
    """
    Sends an email with the specified subject,
    to the specified list of email recipients,
    using the supplied text template with optional context.

    Args:
        subject: The subject line of the email.
        to_email_list: A list of email addresses to send the email to.
        template: The path to the text template to use.
        context: A dictionary containing values to pass to the template (optional).

    Returns:
        None
    """

    # If context is None, set it to an empty dictionary
    if context is None:
        context = {}

    # Render the text template using the provided context
    text_content = render_to_string(template, context)

    # Create the email message object
    email = EmailMessage(
        subject=subject,
        body=text_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=to_email_list,
    )

    # Send the email
    email.send()
