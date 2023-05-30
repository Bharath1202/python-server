from flask import request, make_response
from service import database
from pyodbc import Error
from helpers import commonErrors

pmsql = database.database()
cursor = pmsql.cursor()
getAccountArray = []
try:
    create_new_account = f"""create table account_Register(firstName varchar(15),lastName varchar(4),age varchar(2), 
    gender varchar(7), email varchar(30), mobileNumber varchar(10), address varchar(500), nationality varchar(10), 
    religion varchar(10))"""
    cursor.execute(create_new_account)
    cursor.commit()
except Error as e:
    print(e)
try:
    getAccount = f"""select * from account_Register"""
    cursor.execute(getAccount)
    data = cursor.fetchall()
    for i in data:
        getAccountArray.append(i)
except Error as e:
    print(e)


def newAccountRegister():
    res = request.json
    fname = res['fname']
    lname = res['lname']
    age = res['age']
    gender = res['gender']
    email1 = res['email']
    mobile = res['mobileNumber']
    address = res['address']
    nationality = res['nationality']
    regilion = res['regilion']
    try:
        if len(getAccountArray) == 0:
            insert_table = f"""insert into account_Register(firstName,lastName,age,gender,email,mobileNumber,address,
            nationality,religion) values('{fname}','{lname}','{age}','{gender}','{email1}','{mobile}','{address}',
            '{nationality}','{regilion}')"""
            cursor.execute(insert_table)
            cursor.commit()
    except Error as e:
        print(e)
    try:
        if len(getAccountArray) > 0:
            for i in getAccountArray:
                if not i[5] in mobile:
                    insert_table = f"""insert into account_Register(firstName,lastName,age,gender,email,mobileNumber,address,
                              nationality,religion) values('{fname}','{lname}','{age}','{gender}','{email1}','{mobile}','{address}',
                              '{nationality}','{regilion}')"""
                    cursor.execute(insert_table)
                    cursor.commit()
                else:
                    print('out')
        else:
            print('no Account')
    except Error as e:
        print(e)
    data = {'l': 't'}
    return data
