from django.core.mail import send_mail
from django.core.mail import EmailMessage, EmailMultiAlternatives
from celery import shared_task
from .models import Contact
from django.template.loader import render_to_string

@shared_task
def contact_submit(data, ip):
    submit = Contact(email=data['email'], ip=ip)
    if 'phone' in data:
        submit.phone = data['phone']
    if 'name' in data:
        submit.name = data['name']    
    if 'content' in data:
        submit.content = data['content']
    submit.save()
