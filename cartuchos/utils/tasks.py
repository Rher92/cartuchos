from config.celery import app
from .mailing import Mailing

@app.task(name='send_mail_task', autoretry_for=(Exception,), bind=True, retry_kwargs={'max_retries': 10, 'countdown': 5})
def send_mail(self):
    instance = Mailing()
    instance.test_email_pdf_attached()
