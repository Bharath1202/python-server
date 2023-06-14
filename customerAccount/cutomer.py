from datetime import datetime

from flask import request, make_response
from service import database
from pyodbc import Error
from helpers import commonErrors
from random_object_id import generate
import pandas as pd

id = generate()

for i in commonErrors.errors:
    register = i['success']['register']
    login = i['success']['login']
    error = i['error']['exists']
    status = i['success']['status']

pmsql = database.database()
cursor = pmsql.cursor()

try:
    create_new_account = f"""create table customer_account(_id varchar (40),firstName varchar(15),lastName varchar( 
    4),age varchar(2), dateOfBirth varchar(20), gender varchar(7), email varchar(30), mobileNumber varchar(10), 
    alternateNumber varchar(10) ,martialStatus varchar(10),address varchar(500), nationality varchar(10), 
    religion varchar(10),pincode varchar(6),userImage varchar(170),status varchar(10),bankName varchar(100), 
    accountNumber varchar(16),ifscCode varchar(10))"""
    cursor.execute(create_new_account)
    cursor.commit()
except Error as e:
    print(e)


def newcustomerAcc():
    global customerId
    global verifyDate
    res = request.json
    id = res['_id']
    print(id)
    try:
        getData = f"""select * from account_Register where _id='{id}'"""
        cursor.execute(getData)
        customerId = cursor.fetchall()
        for i in customerId:
            registerDate = i[16]
            date = pd.Timestamp(registerDate)
            verifyDate = pd.Timedelta(datetime.now() - date).seconds / 86400
    except Error as e:
        print(e)

    fname = res['firstName']
    lname = res['lastName']
    age = res['age']
    dateOfBirth = res['dateOfBirth']
    gender = res['gender']
    email1 = res['email']
    mobile = res['mobileNumber']
    alternate = res['alternateNumber']
    martialStatus = res['martialStatus']
    address = res['address']
    nationality = res['nationality']
    religion = res['religion']
    pincode = res['pincode']
    userImage = res['userImage']
    bankName = res['bankName']
    bankAccNo = res['accountNumber']
    ifscCode = res['ifscCode']
    currentDate = datetime.now()
    status = 'In-progress'

    # try:
    #     insert_table = f"""insert into customer_account(_id,firstName,lastName,age,dateOfBirth,gender,email,
    #              mobileNumber,alternateNumber,martialStatus,address, nationality,religion,pincode,userImage,
    #              status,activationDate) values('{id}','{fname}','{lname}','{age}','{dateOfBirth}','{gender}','{email1}','{mobile}',
    #              '{alternate}','{martialStatus}','{address}',
    #              '{nationality}','{religion}','{pincode}','{userImage}','{status}','{currentDate}')"""
    #     cursor.execute(insert_table)
    #     cursor.commit()
    #     response1 = make_response({'success': register})
    #     response1.status_code = 200
    #     return response1
    # except Error as e:
    #     print(e)

    data = {'g': 'gg'}
    return data
