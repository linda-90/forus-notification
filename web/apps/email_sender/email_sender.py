import os

from django.conf import settings
from django.core.mail import get_connection
from mail_templated import send_mail

from apps.notification_user.models import UserConnectionField


class Sender():
    def __init__(self, user, email):
        self.user = user
        self.email = email
        self.backend_index = 0

    def send_email(self, template, data):
        if self.user:
            connections = UserConnectionField.objects.find_emails_connection_by_user(self.user)
            for connection in connections:
                email = connection.value
                self.send_email_with_connection(template, data, email)
        if self.email:
            self.send_email_with_connection(template, data, self.email)

    def send_email_with_connection(self, template, data, email):

        for iteration in range(len(settings.EMAIL_CONNACTIONS) - 1):
            try:
                smtp_connection = get_connection(
                    host=settings.EMAIL_CONNACTIONS[iteration].get('EMAIL_HOST'),
                    port=settings.EMAIL_CONNACTIONS[iteration].get('EMAIL_PORT'),
                    username=settings.EMAIL_CONNACTIONS[iteration].get('EMAIL_HOST_USER'),
                    password=settings.EMAIL_CONNACTIONS[iteration].get('EMAIL_HOST_PASSWORD'),
                    use_tls=settings.EMAIL_CONNACTIONS[iteration].get('EMAIL_USE_TLS'),
                    use_ssl=settings.EMAIL_CONNACTIONS[iteration].get('EMAIL_USE_SSL'),
                )
                send_mail(template, data, settings.EMAIL_CONNACTIONS[iteration].get('EMAIL_FROM'), [email],
                          connection=smtp_connection)
                break
            except:
                pass
