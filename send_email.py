import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail(to, sub, msg):
    # Set up the parameters
    sender_email = 'joblink@outlook.com'
    receiver_email = to
    password = 'joblink@123'
    subject = sub
    body = msg

    # Create the email content
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Connect to Outlook's SMTP server
    with smtplib.SMTP('smtp.office365.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(message)
        return True
