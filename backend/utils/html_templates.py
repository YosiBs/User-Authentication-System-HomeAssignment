RESET_FORM_MAIL = """
<html><body style="text-align:center; margin-top:100px;">
    <form action="/reset" method="POST">
        <input type="hidden" name="token" value="{token}" />
        <input type="password" name="new_password" placeholder="New Password" required />
        <button type="submit">Reset Password</button>
    </form>
</body></html>
"""

VERIFIED_HTML = """
<html>
    <head><title>Verified</title></head>
    <body style="text-align: center; margin-top: 100px; font-family: Arial, sans-serif;">
        <h1 style="color: green;">Email Verified Successfully ✅</h1>
        <p>You can close this window.</p>
    </body>
</html>
"""

INVALID_LINK_HTML = """
<html>
    <head><title>Invalid Link</title></head>
    <body style="text-align: center; margin-top: 100px; font-family: Arial, sans-serif;">
        <h1 style="color: red;">Invalid or Expired Verification Link ❌</h1>
        <p>You can close this window.</p>
    </body>
</html>
"""

def get_verification_email_html(token: str) -> str:
    return f"""
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


def get_reset_email_html(token: str) -> str:
    return f"""
    <html>
        <body style="text-align:center; font-family:sans-serif; margin-top:50px;">
            <h2>Password Reset</h2>
            <p>Click below to reset your password:</p>
            <a href="http://localhost:5000/reset?token={token}" 
                style="padding:10px 20px; background:#007bff; color:white; text-decoration:none; border-radius:5px;">
                Reset Password
            </a>
            <p>If this wasn't you, ignore this email.</p>
        </body>
    </html>
    """