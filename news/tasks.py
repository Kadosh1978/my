from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from celery import shared_task
import time

from requests import head
from news.models import Post, Category



@shared_task
def send_notifications(pk):
    post = Post.objects.get(pk=pk)
    categories = post.category.all()
    title = post.head
    subscribers_emails = []

    for category in categories:
        subscribers_users = category.subscribers.all()
        for sub_user in subscribers_users:
            subscribers_emails.append(sub_user.email)

    html_content = render_to_string(
        'post_created_email.html',
        {
            
            'text': post.preview,
            'link': f'{settings.SITE_URL}/news/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject= head,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to= subscribers_emails,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()  





# def send_notifications(preview, pk, head, subscribers):
#     html_content = render_to_string(
#         'post_created_email.html',
#         {
            
#             'text': preview,
#             'link': f'{settings.SITE_URL}/news/{pk}'
#         }
#     )

#     msg = EmailMultiAlternatives(
#         subject= head,
#         body='',
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         to= subscribers,
#     )

#     msg.attach_alternative(html_content, 'text/html')
#     msg.send()  



# @receiver(m2m_changed, sender=PostCategory)
# def notify_about_new_post(sender, instance, **kwargs):
#     if kwargs['action'] == 'post_add':
#         categories = instance.category.all()
#         subscribers_emails = []

#         for cat in categories:
#             subscribers = cat.subscribers.all()
#             subscribers_emails +=[s.email for s in subscribers]

#         send_notifications(instance.preview(), instance.pk, instance.head, subscribers_emails)