from flask import request, make_response
from service import database
from pyodbc import Error
from helpers import commonErrors

for i in commonErrors.errors:
    register = i['success']['register']
    login = i['success']['login']
    error = i['error']['exists']

pmsql = database.database()
cursor = pmsql.cursor()
getAccountArray = []
try:
    create_new_account = f"""create table account_Register(firstName varchar(15),lastName varchar(4),age varchar(2), 
    gender varchar(7), email varchar(30), mobileNumber varchar(10),alternateNumber varchar(10) ,address varchar(500), nationality varchar(10), 
    religion varchar(10),pincode varchar(6),userImage varchar(170))"""
    cursor.execute(create_new_account)
    cursor.commit()
except Error as e:
    print(e)



def newAccountRegister():
    global status_code
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
    gender = res['gender']
    email1 = res['email']
    mobile = res['mobileNo']
    alternate = res['alternateNo']
    address = res['address']
    nationality = res['nationality']
    religion = res['religion']
    pincode = res['pinCode']
    userImage = res['userImage']
    try:
        if len(getAccountArray) == 0:
            insert_table = f"""insert into account_Register(firstName,lastName,age,gender,email,mobileNumber,alternateNumber,address,
            nationality,religion,pincode,userImage) values('{fname}','{lname}','{age}','{gender}','{email1}','{mobile}','{alternate}','{address}',
            '{nationality}','{religion}','{pincode}','{userImage}')"""
            cursor.execute(insert_table)
            cursor.commit()
    except Error as e:
        print(e)
    try:
        if len(getAccountArray) > 0:
            for i in getAccountArray:
                if not i[5] in mobile:
                    insert_table = f"""insert into account_Register(firstName,lastName,age,gender,email,mobileNumber,alternateNumber,address,
                              nationality,religion,pincode,userImage) values('{fname}','{lname}','{age}','{gender}','{email1}','{mobile}','{alternate}','{address}',
                              '{nationality}','{religion}','{pincode}','{userImage}')"""
                    cursor.execute(insert_table)
                    cursor.commit()
                    response = make_response({'success':register},{register:register})
                    response.status_code = 200
                    status_code=response.status_code
                    return response
                else:
                    response = make_response({'error':error})
                    response.status_code = 403
                    status_code=response.status_code
                    return response
        else:
            print('no Account')
    except Error as e:
        print(e)
    if status_code == 200:
        data = {'result':register}
        return data
    else:
        data = {'result': error}
        return data
