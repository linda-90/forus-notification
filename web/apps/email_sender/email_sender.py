import os

from django.conf import settings
from django.core import mail
from mail_templated import send_mail

from apps.notification_user.models import UserConnectionField


class Sender():
    def __init__(self, user):
        self.user = user

    def send_email(self, template, data):
        connections = UserConnectionField.objects.find_emails_connection_by_user(self.user)

        for connection in connections:
            email = connection.value

            send_mail(template, data, settings.EMAIL_FROM, [email], connection=connection)


            # djemail.send_email(
            #     to=email,
            #     template_name=template,  # .txt and/or .html
            #     context=data,
            #     subject="Forus notification"
            # )
            # send_templated_mail(
            #     template_name=template,
            #     from_email='mk@gmail.com',
            #     сс=[email],
            #     bcc=[email],
            #     recipient_list=[email],
            #     context=data,
            # )
