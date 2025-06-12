import smtplib
from email.message import EmailMessage

from backend.config import EMAIL_APP_PASSWORD, EMAIL_FROM, SMTP_PORT, SMTP_SERVER
from backend.utils.html_templates import get_reset_email_html, get_verification_email_html

def send_verification_email(to_email, token):
    msg = EmailMessage()
    msg['Subject'] = 'Verify your email'
    msg['From'] = EMAIL_FROM
    msg['To'] = to_email

    msg.add_alternative(get_verification_email_html(token), subtype='html')
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.login(EMAIL_FROM, EMAIL_APP_PASSWORD)
        smtp.send_message(msg)


def send_reset_email(to_email, token):
    msg = EmailMessage()
    msg['Subject'] = 'Reset your password'
    msg['From'] = EMAIL_FROM
    msg['To'] = to_email

    msg.add_alternative(get_reset_email_html(token), subtype='html')
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.login(EMAIL_FROM, EMAIL_APP_PASSWORD)
        smtp.send_message(msg)
