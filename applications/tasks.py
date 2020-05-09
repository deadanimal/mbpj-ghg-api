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


# Crontab: https://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html
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


    
"""
def generate_pdf():

    from django.core.files.storage import default_storage
    #default_storage.exists('zeus/tickets')

    filename = 'tickets/storage_test.txt'
    pdffile = default_storage.open(filename, 'w')
    pdffile.write('storage contents')
    pdffile.close()

    url_link = config('AWS_S3_ENDPOINT_URL') + '/' + config('AWS_STORAGE_BUCKET_NAME') + '/' + filename
    return url_link


@periodic_task(run_every=(crontab()),name="lola", ignore_result=True)
def lola():

    link_provided = 'https://webhook.site/fadccae5-b9e5-441b-8168-cea4b96a31db'
    r = requests.get(link_provided)

    return True


@shared_task
def create_task(task_type):
    time.sleep(int(task_type) * 10)
    return True
"""
