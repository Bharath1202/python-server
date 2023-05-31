import smtplib
import ssl
from email.message import EmailMessage

appPassword = 'ywdlmabvzjrwqfpw'
context = ssl.create_default_context()
v = "viveka@upturntechnology.com"
g = "guganathanyogi1997@gmail.com"
t = "gayathri@upturntechnology.com"
sender_email = 'Hacker72363744@gmail.com'
e = EmailMessage()
e['From'] = "Hacker72363744@gmail.com"
e['To'] = "bharathaustin403@gmail.com"
e['subject'] = 'We track you'
i = 0
for i in range(15):
    body = f"""{'😈'}"""
    e.set_content(body)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smpt:
        smpt.login(sender_email, appPassword)
        smpt.sendmail(sender_email, g, e.as_string())


