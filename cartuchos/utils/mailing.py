from django.core.mail import send_mail


class Mailing:
    def test_mail(self):
        send_mail(
            subject = "Test Email",
            message = "This is a test email",
            from_email = None,   # This will have no effect is you have set DEFAULT_FROM_EMAIL in settings.py
            recipient_list = ['<your_recipient_email>'],    # This is a list
            fail_silently = False     # Set this to False so that you will be noticed in any exception raised
        )