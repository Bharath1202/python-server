from flask import request, make_response
from service import database
from pyodbc import Error
from helpers import commonErrors
from random_object_id import generate
from datetime import datetime
id = generate()
date = datetime.now()
for i in commonErrors.errors:
    register = i['success']['register']
    login = i['success']['login']
    error = i['error']['exists']
    status = i['success']['status']

pmsql = database.database()
cursor = pmsql.cursor()
getAccountArray = []
try:
    create_new_account = f"""create table account_Register(_id varchar (40),firstName varchar(15),lastName varchar(
    4),age varchar(2), dateOfBirth varchar(30), gender varchar(7), email varchar(30), password varchar(50), mobileNumber varchar(10),
    alternateNumber varchar(10) ,martialStatus varchar(10),address varchar(500), nationality varchar(10), 
    religion varchar(10),pincode varchar(6),userImage varchar(170),status varchar(10),activationDate varchar(50))"""
    cursor.execute(create_new_account)
    cursor.commit()
except Error as e:
    print(e)



def newAccountRegister():
    global status_code
    global response1
    global response2
    try:
        getAccount = f"""select * from account_Register"""
        cursor.execute(getAccount)
        data = cursor.fetchall()
        for i in data:
            getAccountArray.append(i)
    except Error as e:
        print(e)
    res = request.json
    fname = res['firstName']
    lname = res['lastName']
    age = res['age']
    dateOfBirth = res['dateOfBirth']
    gender = res['gender']
    email1 = res['email']
    password = '123456'
    mobile = res['mobileNo']
    alternate = res['alternateNo']
    martialStatus = res['martialStatus']
    address = res['address']
    nationality = res['nationality']
    religion = res['religion']
    pincode = res['pinCode']
    userImage = res['userImage']
    status = 'pending'
    currentDate = datetime.now()
    try:
        if len(getAccountArray) == 0:
            insert_table = f"""insert into account_Register(_id,firstName,lastName,age,dateOfBirth,gender,email,
            mobileNumber,alternateNumber,martialStatus,address, nationality,religion,pincode,userImage,
            status,activationDate,password) values('{id}','{fname}','{lname}','{age}','{dateOfBirth}','{gender}','{email1}', '{mobile}',
            '{alternate}','{martialStatus}','{address}',
            '{nationality}','{religion}','{pincode}','{userImage}','{status}','{currentDate}','{password}')"""
            cursor.execute(insert_table)
            cursor.commit()
            response1 = make_response({'success': register})
            response1.status_code = 200
            return response1
    except Error as e:
        print(e)
    try:
        if len(getAccountArray) > 0:
            for i in getAccountArray:
                if not i[5] in mobile:
                    insert_table = f"""insert into account_Register(_id,firstName,lastName,age,dateOfBirth,gender,
                    email,mobileNumber,alternateNumber,martialStatus,address, nationality,religion,pincode,userImage,
                    status,activationDate,password,) values('{id}','{fname}','{lname}','{age}','{dateOfBirth}','{gender}','{email1}',
                    '{mobile}','{alternate}','{martialStatus}','{address}',
                              '{nationality}','{religion}','{pincode}','{userImage}','{status}','{currentDate}','{password}')"""
                    cursor.execute(insert_table)
                    cursor.commit()
                    response1 = make_response({'success':register})
                    response1.status_code = 200
                    return response1
                else:
                    response2 = make_response({'error':error})
                    response2.status_code = 403
                    status_code=response2.status_code
                    return response2
        else:
            print('no Account')
    except Error as e:
        print(e)
    data= {'res':"response1"}
    return data
