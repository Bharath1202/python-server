from flask import request, make_response
from service import database
from pyodbc import Error
from helpers import token
from helpers import commonErrors
import cryptocode

pmsql = database.database()
cursor = pmsql.cursor()

for i in commonErrors.errors:
    register = i['success']['register']
    login = i['success']['login']
    error = i['error']['exists']
    invalid = i['error']['invalidEmail']
    verify = i['error']['verify']


def loginForm():
    global responseEmail, responsePassword
    res = request.json
    email = res['email']
    password = res['password']
    loginType = ''
    try:
        findData = f"""select * from register where email='{email}' """
        cursor.execute(findData)
        var = cursor.fetchall()
        for i in var:
            responseEmail = i[1]
            decodePassword = i[2]
            responsePassword = cryptocode.decrypt(decodePassword, "password")
            if responseEmail == "admin@gmail.com":
                loginType = 'admin'
            else:
                loginType = "user"
        if len(var) > 0:
            if responseEmail == email and responsePassword == password:
                access = token.create_access_token(data={'email': email})
                responseData = {
                    "userDetails": email,
                    "token": access,
                    "tokenType": 'Bearer',
                    "loginType": loginType
                }
                response = make_response({'result': responseData})
                response.status_code = 200
                return response
            else:
                response = make_response({'result': verify})
                response.status_code = 400
                return response
        else:
            response = make_response({'result': invalid})
            response.status_code = 400
            return response
    except Error as e:
        response = make_response({'Invalid': invalid})
        response.status_code = 409
        return response
