from typing import List, Optional

import pycmarkgfm
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


def send_email(
    subject: str,
    to_email_list: List[str],
    template: str,
    context: Optional[dict] = None,
    md_to_html: Optional[bool] = False,
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
        md_to_html: Whether the template content is written in Markdown format and
        should be rendered as HTML.

    Returns:
        None
    """

    # If context is None, set it to an empty dictionary
    if context is None:
        context = {}

    # Render the text template using the provided context
    text_content = render_to_string(template, context)

    if md_to_html:
        text_content = pycmarkgfm.gfm_to_html(text_content)

    # Create the email message object
    email = EmailMessage(
        subject=subject,
        body=text_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=to_email_list,
    )

    # If markdown to html is enabled, set the content type to HTML
    if md_to_html:
        email.content_subtype = "html"

    # Send the email
    email.send()
