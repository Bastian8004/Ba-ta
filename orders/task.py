from django.core.mail import send_mail

from .models import Order


def order_created(order_id):

    order = Order.objects.get(id=order_id)
    subject = 'Zamówienie numer {}'.format(order.id)
    message = 'Drogi {},\n\nUkończyłeś właśnie swojje zamówienie.\
                Twój numer zamówienia to: {}.'.format(order.first_name,
                                             order.id)
    mail_sent = send_mail(subject,
                          message,
                          'bastastore@gmail.com',
                          [order.email])
    return mail_sent
