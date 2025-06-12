import smtplib
from email.message import EmailMessage

def send_verification_email(to_email, token):
    msg = EmailMessage()
    msg['Subject'] = 'Verify your email'
    msg['From'] = 'huxhron@gmail.com'
    msg['To'] = to_email

    html_content = f"""
    <html>
        <body>
            <h2>Welcome!</h2>
            <p>Please verify your email by clicking the button below:</p>
            <a href="http://localhost:5000/verify?token={token}" 
                style="display:inline-block;padding:10px 20px;background-color:#28a745;color:#fff;text-decoration:none;border-radius:5px;">
                Verify Email
            </a>
            <p>If the button doesn't work, paste this link in your browser:</p>
            <p><code>http://localhost:5000/verify?token={token}</code></p>
        </body>
    </html>
    """
    msg.add_alternative(html_content, subtype='html')
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('huxhron@gmail.com', 'muxwxqiykynjsery')
        smtp.send_message(msg)


def send_reset_email(to_email, token):
    msg = EmailMessage()
    msg['Subject'] = 'Reset your password'
    msg['From'] = 'huxhron@gmail.com'
    msg['To'] = to_email

    html = f"""
    <html><body style="text-align:center; font-family:sans-serif; margin-top:50px;">
      <h2>Password Reset</h2>
      <p>Click below to reset your password:</p>
      <a href="http://localhost:5000/reset?token={token}" style="padding:10px 20px; background:#007bff; color:white; text-decoration:none; border-radius:5px;">Reset Password</a>
      <p>If this wasn't you, ignore this email.</p>
    </body></html>
    """
    msg.add_alternative(html, subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('huxhron@gmail.com', 'muxwxqiykynjsery')
        smtp.send_message(msg)
