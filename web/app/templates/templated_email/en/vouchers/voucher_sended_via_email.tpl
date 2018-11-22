
{% extends "templated_email/base.tpl" %}
{% block subject %}Your voucher{% endblock %}
{% block html %}
    Dear citizen,
    <br/>
    You’ve requested to receive your {{ fund_product_name }} voucher by e-mail.
    <br/>
    You can use the QR-Code below to show to a provider.
    <br/>
    They will scan your code and deliver your product / service.
    <br/>
    <br/>
    <img style="display: block; margin: 0 auto;" src="{{ qr_url }}" width="300" />
{% endblock %}