import smtplib
import ssl
from email.message import EmailMessage

appPassword = 'ywdlmabvzjrwqfpw'
context = ssl.create_default_context()

d = "guganathanyogi1997@gmail.com"
sender_email = 'Hacker72363744@gmail.com'
e = EmailMessage()
e['From'] = "Hacker72363744@gmail.com"
e['To'] = "bharathaustin403@gmail.com"
i = 0
for i in range(1000):
    body = f"""Hii"""
    e.set_content(body)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smpt:
        smpt.login(sender_email, appPassword)
        smpt.sendmail(sender_email, d, e.as_string())
