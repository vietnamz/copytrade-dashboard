# Create your tasks here
from celery import task
from django.template import loader
from django.core import mail
from django.conf import Settings


@task
def send_email(subject, msg, recipients):
    html = loader.render_to_string('email.html', {
        'user_name' : "tammd",
        'subject': 'thank you'
    })
    mail.send_mail(subject=subject, message=msg, from_email=Settings.EMAIL_HOST_USER, recipient_list=recipients, fail_silently=False, auth_user=Settings.EMAIL_HOST_USER, auth_password=Settings.EMAIL_HOST_PASSWORD, html_message=html)
