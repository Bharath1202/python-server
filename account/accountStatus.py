from flask import Flask, request, make_response
from service import database
import smtplib
import ssl
from email.message import EmailMessage

sender_email = 'noheavenforyours@gmail.com'
appPassword = 'wiuriapxdbbwisut'
context = ssl.create_default_context()

pmsql = database.database()
cursor = pmsql.cursor()
def changeStatus():
    global userEmail
    res = request.json
    id = res['_id']
    status = res['status']
    update = f"""update customer_account set status='{status}' where _id='{id}'"""
    cursor.execute(update)
    cursor.commit()
    select = f"""select * from customer_account where _id='{id}'"""
    cursor.execute(select)
    data = cursor.fetchall()
    for i in data:
        userEmail = i[6]
    e = EmailMessage()
    e['From'] = "noheavenforyours@gmail.com"
    e['To'] = userEmail
    e['subject'] = "Sample"
    for i in range(1):
        body = f"""Thanks for choosing our bank 
                   Your password : 123456 """
        e.set_content(body)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smpt:
            smpt.login(sender_email, appPassword)
            smpt.sendmail(sender_email, userEmail, e.as_string())
    response = make_response({'result': 'Please check your mail'})
    response.status_code = 200

    d = {'result': 'Please check your mail'}
    return d