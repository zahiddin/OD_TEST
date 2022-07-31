from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Student
from django.core.mail import EmailMessage


@receiver(post_save, sender=Student)
def send_mail(sender, instance, created, **kwargs):
    if created:
        message = f'{instance.full_name} Ваш учитель вас зарегистрировал'
        email = EmailMessage('Сообщение от Школы', message, to=[f'{instance.mail_address}'])
        email.send()

