import smtplib
import ssl
from flask import request,make_response
from service import database
from email.message import EmailMessage
import uuid
import random
import datetime
from helpers import commonErrors

id = uuid.uuid1()
appPassword = 'kedlmhrdqwfjxzlz'
context = ssl.create_default_context()
date = datetime
pmsql = database.database()
cursor = pmsql.cursor()
try:
    create_otp = f"""create table OTP(ID varchar(50),otp varchar(4),validTime varchar(30))"""
    cursor.execute(create_otp)
    cursor.commit()
except Exception as e:
    print(e)

global validTimeId

for i in commonErrors.errors:
    invalid = i['error']['invalidEmail']
    notRegister = i['error']['notRegister']
def opt():
    otp = random.randint(1000, 9999)
    try:
        global time1, otp1
        res = request.json
        email = res['emailId']
        sendEmail = email
        table = f"""select * from register where email='{email}' """
        cursor.execute(table)
        registerData = cursor.fetchall()
        if len(registerData) > 0:
            for i in registerData:
                if i[1] == sendEmail:
                    emailAppPassword = appPassword
                    sender_email = 'bharathbharat2412@gmail.com'
                    body = f"""This OTP is valid for 1 minutes {otp}"""
                    e = EmailMessage()
                    e['From'] = "bharathbharat2412@gmail.com"
                    e['To'] = email
                    e.set_content(body)
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smpt:
                        smpt.login(sender_email, emailAppPassword)
                        smpt.sendmail(sender_email, sendEmail, e.as_string())
                    minute = date.datetime.now()
                    set_table = f"""insert into OTP(ID,otp,validTime) values('{id.hex}','{otp}','{minute}')"""
                    cursor.execute(set_table)
                    cursor.commit()
                    data = {'otp': otp,"email":sendEmail}
                    return data
                else:
                    response = make_response({'result': invalid})
                    response.status_code = 400
                    return response
        else:
            response = make_response({'result': notRegister})
            response.status_code = 403
            return response
    except Exception as e:
        print(e)
    d = {'l':'o'}
    return d