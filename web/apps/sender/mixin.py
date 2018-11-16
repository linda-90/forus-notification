from apps.sender.tasks import send_email, send_mobile_push


class BaseSendMixin(object):
    def send_push(self, reffer_user_id, title, body):
        send_mobile_push(None,reffer_user_id, title, body)

    def send(self, reffer_user_id, template, data):
        send_email(reffer_user_id, template, data)
        pass
