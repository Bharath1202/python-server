import smtplib
import ssl
from email.message import EmailMessage
import time

appPassword = 'wiuriapxdbbwisut'
# gTTS('Hello Surndhar').save('surenshar.mp3')
context = ssl.create_default_context()
v = "viveka@upturntechnology.com"
g = "guganathanyogi1997@gmail.com"
g1 = "guganathan@upturntechnology.com"
emailArray = [g,g1]

t = "gayathri@upturntechnology.com"
b = "bharathaustin403@gmail.com"
sender_email = 'noheavenforyours@gmail.com'
e = EmailMessage()
e['From'] = "noheavenforyours@gmail.com"
e['To'] = "guganathanyogi1997@gmail.com"
e['subject'] = 'We track you'
i = 0
# for email in emailArray:
for i in range(1):
    body = f"""{'😈'}"""
    e.set_content(body)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smpt:
        smpt.login(sender_email, appPassword)
        smpt.sendmail(sender_email, g, e.as_string())

# def notify():
#     while True:
#         notification.notify(
#             title="ALERT!!!",
#             message="Take a break! It has been an hour!",
#             timeout=10
#         )
#         time.sleep(2)
# notify()
