#!/usr/bin/env python3
"""Send email via Gmail SMTP. Used by the research agent pipeline."""

import smtplib
import sys
from email.mime.text import MIMEText

SENDER = "kk837@cornell.edu"
DEFAULT_CC = "kb529@cornell.edu"
CONTACT_PHONE = "607-327-2580"
SELF_ADDRESSES = {"kk837@cornell.edu", "kb529@cornell.edu"}
APP_PASSWORD_FILE = "/home/kk837/.claude/.gmail_app_password"


def send(to: str, subject: str, body: str, cc: str = DEFAULT_CC):
    recipients = {addr.strip() for addr in to.split(",")}
    is_outreach = not recipients.issubset(SELF_ADDRESSES)
    if is_outreach and CONTACT_PHONE not in body:
        body = body.rstrip() + "\n" + CONTACT_PHONE + "\n"

    with open(APP_PASSWORD_FILE) as f:
        password = f.read().strip()

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER
    msg["To"] = to
    if cc:
        msg["Cc"] = cc

    all_recipients = [to] + ([cc] if cc else [])

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(SENDER, password)
        server.send_message(msg, to_addrs=all_recipients)

    print(f"Sent to {to} (cc: {cc}): {subject}")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: send_email.py <to> <subject> <body>")
        sys.exit(1)
    send(sys.argv[1], sys.argv[2], sys.argv[3])
