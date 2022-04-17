import boto3
from config.celery import app
from .mailing import Mailing
from pathlib import Path

PATH_DIR = Path(__file__).resolve(strict=True).parent


@app.task(name='send_mail_task', autoretry_for=(Exception,), bind=True, retry_kwargs={'max_retries': 10, 'countdown': 5})
def send_mail(self):
    instance = Mailing()
    instance.test_email_pdf_attached()


@app.task(name='upload_file_task', autoretry_for=(Exception,), bind=True, retry_kwargs={'max_retries': 10, 'countdown': 5})
def upload_file(self):
    session = boto3.session.Session()
    client = session.client('s3',
                            region_name='fra1',
                            endpoint_url='https://url.fra1.digitaloceanspaces.com',
                            aws_access_key_id='FODASEXUTMJJ72ZGWDGC',
                            aws_secret_access_key='rX0Lw2DcFWVUyF36iz2nlllrhNJ4CY4BlCR73tMFEi4')

    client.upload_file(str(PATH_DIR / 'test.pdf'), 'files', 'test.pdf')