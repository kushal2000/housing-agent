#!/usr/bin/env python3
"""Send email via Gmail SMTP. Used by the research agent pipeline."""

import smtplib
import sys
from email.mime.text import MIMEText

SENDER = "kk837@cornell.edu"
APP_PASSWORD_FILE = "/home/kk837/.claude/.gmail_app_password"


def send(to: str, subject: str, body: str):
    with open(APP_PASSWORD_FILE) as f:
        password = f.read().strip()

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER
    msg["To"] = to

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(SENDER, password)
        server.send_message(msg)

    print(f"Sent to {to}: {subject}")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: send_email.py <to> <subject> <body>")
        sys.exit(1)
    send(sys.argv[1], sys.argv[2], sys.argv[3])
