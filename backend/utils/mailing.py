from django.core.mail import send_mail, EmailMessage
from pathlib import Path

PATH_DIR = Path(__file__).resolve(strict=True).parent

class Mailing:
    def test_mail(self):
        send_mail(
            subject = "Test Email",
            message = "This is a test email",
            from_email = None,
            recipient_list = ['<your_recipient_email>'],
            fail_silently = False
        )
        
    def test_email_pdf_attached(self):
        pdf = str(PATH_DIR / 'test.pdf')
        
        email = EmailMessage(
            'Hello!!!!',
            'https://retornos-consumibles-file.fra1.digitaloceanspaces.com/retornos-consumibles-file/test.pdf',
            'from@example.com',
            ['to1@example.com', 'to2@example.com'],
            ['bcc@example.com'],
            reply_to=['another@example.com'],
            headers={'Message-ID': 'foo'},
        )

        email.attach_file(pdf)
        email.send()
