import os
import smtplib

FROM_EMAIL = os.environ.get("FROM_EMAIL")
TO_EMAIL = os.environ.get("TO_EMAIL")
PASSWORD = os.environ.get("PASSWORD")
AMAZON_URL = os.environ.get("AMAZON_URL")
SMTP_HOST = os.environ.get("SMTP_HOST")
SMTP_PORT = int(os.environ.get("SMTP_PORT"))


def send_email(price_float: float):
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as connection:
        connection.starttls()
        connection.login(user=FROM_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=FROM_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject:Raspberry Pi\n\nRaspberry Pi price dropped to ${price_float}\n{AMAZON_URL}"
        )
