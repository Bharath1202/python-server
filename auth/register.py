from service import database
from pyodbc import Error
from flask import request, make_response
from helpers import token
from helpers import commonErrors

for i in commonErrors.errors:
    register = i['success']['register']
    login = i['success']['login']
    error = i['error']['exists']
pmsql = database.database()
cursor = pmsql.cursor()
emailArray = []

try:
    reg = """select * from register"""
    cursor.execute(reg)
    data = cursor.fetchall()
    for i in data:
        emailArray.append(i[1])
except Error as e:
    print('e', e)


def reg():
    try:
        table = f"""create table register(userName varchar(20), email varchar(20), password varchar(50), mobileNumber varchar(10))"""
        cursor.execute(table)
        cursor.commit()
    except Error as e:
        print(e)

    res = request.json
    userName = res['userName']
    email = res['email']
    password = res['password']
    mobileNumber = int(res['mobile'])
    access = token.create_access_token(data={'email': email})
    if email == "admin@gmail.com":
        loginType = 'admin'
    else:
        loginType = "user"
    data = {
        "email": email,
        "mobile": int(mobileNumber),
        "loginType": loginType,
    }
    try:
        if len(emailArray) == 0:
            insert = f"""insert into register(username,email,password,mobileNumber) values('{userName}','{email}','{password}',{mobileNumber})"""
            cursor.execute(insert)
            cursor.commit()
            response = make_response({'response': register})
            response.status_code = 200
            return response
        else:
            print('out')
    except Error as err:
        response = make_response({'error': err})
        response.status_code = 409
        return response
    try:
        if not email in emailArray:
            insert = f"""insert into register(username,email,password,mobileNumber) values('{userName}','{email}','{password}',{mobileNumber})"""
            cursor.execute(insert)
            cursor.commit()
            response = make_response({'response': register})
            response.status_code = 200
            return response
    except Error as err:
        response = make_response({'error': err})
        response.status_code = 409
        return response
    return data