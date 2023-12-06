from django.core.management.base import BaseCommand
from data_models.models import AccountVerification
from django.core.mail import send_mail

class Command(BaseCommand):
    help = 'Verify account'

    def handle(self, *args, **options):
        pending_verification = AccountVerification.objects.filter(verification_status='pending')

        for verification in pending_verification:
            # Update the account_verification status
            verification.verification_status = 'verified'
            verification.save()
            
            
            send_mail(
                'You account verification',
                f'Your account has been successfuly verified!',
                'from@example.com',
                [verification.user.email],
                fail_silently=False,
            )


        self.stdout.write(self.style.SUCCESS('Accounts verified successfully!'))
