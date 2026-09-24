import os
import ssl
import smtplib
from email.message import EmailMessage
from pathlib import Path

class EmailNotifier:
    def __init__(self):
        self.enabled = os.getenv("EMAIL_ENABLED", "false").lower() == "true"
        self.host = os.getenv("SMTP_HOST", "smtp.gmail.com")
        self.port = int(os.getenv("SMTP_PORT", "587"))
        self.user = os.getenv("SMTP_USER", "")
        self.password = os.getenv("SMTP_PASSWORD", "")
        self.to = os.getenv("ALERT_TO", "")

    def send(self, subject, body, attachment=None):
        if not self.enabled:
            return False, "Email disabled"
        missing = [name for name, value in (
            ("SMTP_USER", self.user),
            ("SMTP_PASSWORD", self.password),
            ("ALERT_TO", self.to),
        ) if not value]
        if missing:
            return False, "Missing: " + ", ".join(missing)

        msg = EmailMessage()
        msg["From"] = self.user
        msg["To"] = self.to
        msg["Subject"] = subject
        msg.set_content(body)

        if attachment:
            data = Path(attachment).read_bytes()
            msg.add_attachment(data, maintype="image", subtype="jpeg",
                               filename=Path(attachment).name)

        context = ssl.create_default_context()
        with smtplib.SMTP(self.host, self.port, timeout=20) as smtp:
            smtp.ehlo()
            smtp.starttls(context=context)
            smtp.ehlo()
            smtp.login(self.user, self.password)
            smtp.send_message(msg)
        return True, "Email sent"
