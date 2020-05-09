from __future__ import absolute_import, unicode_literals
from celery import task, shared_task
from celery.decorators import periodic_task
from celery.task.schedules import crontab
from decouple import config

from django.core.mail import EmailMultiAlternatives, EmailMessage
from django.template import Context
from django.template.loader import render_to_string
from anymail.message import attach_inline_image_file

import requests

from users.models import CustomUser

from applications.models import (Application)
from faqs.models import (Faq)
from houses.models import (House)
from medias.models import (Media)
from organisations.models import (Organisation)
from rebates.models import (Rebate)
from reports.models import (Report)
#from tickets.models import ()
from users.models import (CustomUser)


def initialise_app_for(user):

    return json_data

@periodic_task(run_every=(crontab(minute=0, hour=0)),name="email_daily_application_summary", ignore_result=True)
def email_daily_application_summary():

    user_list = CustomUser.objects.filter(user_type='AD')

    merge_data = {
        'ORDERNO': "12345", 
        'TRACKINGNO': "1Z987"
    }
    
    plaintext_context = Context(autoescape=False)  
    subject = render_to_string("email_daily_application_summary_subject.txt", merge_data)
    text_body = render_to_string("email_daily_application_summary_body.txt", merge_data)
    html_body = render_to_string("email_daily_application_summary.html", merge_data)

    message = EmailMultiAlternatives(
        subject=subject, 
        from_email="api@pipeline.com.my",
        to=email_list, 
        body=text_body)
    message.attach_alternative(html_body, "text/html")
    message.send()    