import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configure your email credentials
SENDER_EMAIL = "chaitrapaladugula@gmail.com"
SENDER_PASSWORD = "olmf miao iduj brey"   # Use App Password for Gmail
RECEIVER_EMAIL = "paladugulachaitra123@gmail.com"

def send_email(subject, message):
    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        server.quit()

        print("✅ Email sent successfully!")

    except Exception as e:
        print(f"⚠️ Failed to send email: {e}")
