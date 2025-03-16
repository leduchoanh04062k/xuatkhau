# from django.core.mail import send_mail
# from django.core.mail import EmailMessage, EmailMultiAlternatives
# from celery import shared_task
# from .models import Contact
# from django.template.loader import render_to_string

# @shared_task
# def contact_submit(data, ip):
#     submit = Contact(email=data['email'], ip=ip)
#     if 'phone' in data:
#         submit.phone = data['phone']
#     if 'name' in data:
#         submit.name = data['name']    
#     if 'content' in data:
#         submit.content = data['content']
#     submit.save()

import os
from requests import Request, Session, hooks
from twilio.http.http_client import TwilioHttpClient
from twilio.http.response import Response

class MyRequestClass(TwilioHttpClient):
    def __init__(self):
        self.response = None

    def request(self, method, url, params=None, data=None, headers=None, auth=None, timeout=None,
                allow_redirects=False):
        kwargs = {
            'method': method.upper(),
            'url': url,
            'params': params,
            'data': data,
            'headers': headers,
            'auth': auth,
        }

        session = Session()
        request = Request(**kwargs)

        prepped_request = session.prepare_request(request)
        session.proxies.update({
            'http': os.getenv('HTTP_PROXY'),
            'https': os.getenv('HTTPS_PROXY')
        })
        response = session.send(
            prepped_request,
            allow_redirects=allow_redirects,
            timeout=timeout,
        )

        return Response(int(response.status_code), response.text)