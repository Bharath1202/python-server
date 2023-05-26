import smtplib
import ssl
from email.message import EmailMessage

appPassword = 'kedlmhrdqwfjxzlz'
context = ssl.create_default_context()

d = "guganathanyogi1997@gmail.com"
sender_email = 'bharathbharat2412@gmail.com'
e = EmailMessage()
e['From'] = "bharathbharat2412@gmail.com"
e['To'] = "guganathanyogi1997@gmail.com"
i = 0
while i < 1000:
    body = f"""Dei"""
    e.set_content(body)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smpt:
        smpt.login(sender_email, appPassword)
        smpt.sendmail(sender_email, d, e.as_string())
    i += 1
