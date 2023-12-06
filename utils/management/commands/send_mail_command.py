from django.core.management.base import BaseCommand
from data_models.models import Notifications
from django.core.mail import send_mail

class Command(BaseCommand):
    help = 'Send email notifications'

    def handle(self, *args, **options):
        pending_notifications = Notifications.objects.filter(status='pending')

        for notification in pending_notifications:
            recipient = notification.recipient
            subject = notification.subject
            body = notification.body

            send_mail(
                subject,
                body,
                'from@example.com',
                [recipient],
                fail_silently=False,
            )

            # Update the notification status
            notification.status = 'sent'
            notification.save()

        self.stdout.write(self.style.SUCCESS('Email notifications sent'))
