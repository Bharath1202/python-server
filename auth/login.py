from flask import request, make_response
from service import database
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
    userData = []
    res = request.json
    email = res['email']
    password = res['password']
    loginType = ''
    try:
        if email == "admin@gmail.com":
            loginType = 'admin'
            findData = f"""select * from register where email='{email}' """
            cursor.execute(findData)
            var = cursor.fetchall()
            for i in var:
                user = {
                    '_id': i[0],
                    'name': i[1],
                    'email': i[2],
                    'mobile': i[4],
                }
                userData.append(user)
                responseEmail = i[2]
                decodePassword = i[3]
                responsePassword = cryptocode.decrypt(decodePassword, "password")
                if len(var) > 0:
                    if responseEmail == email and responsePassword == password:
                        access = token.create_access_token(data={'email': email})
                        responseData = {
                            "userDetails": userData,
                            "token": access,
                            "tokenType": 'Bearer',
                            "loginType": loginType
                        }
                        print(responseData)
                        response = make_response({'result': responseData})
                        response.status_code = 200
                        return response
                    else:
                        response = make_response({'result': verify})
                        response.status_code = 403
                        return response
                else:
                    response = make_response({'result': invalid})
                    response.status_code = 400
                    return response
        else:
            loginType = "user"
            findData = f"""select * from register where email='{email}' """
            cursor.execute(findData)
            var = cursor.fetchall()
            for i in var:
                print(i)
                userEmail =  i[2]
                userPassword =  i[3]
                responsePassword1 = cryptocode.decrypt(userPassword, "password")
                print(userEmail)
                if len(var) > 0:
                    if userEmail == email and responsePassword1 == password:
                        access = token.create_access_token(data={'email': email})
                        responseData = {
                            "userDetails": userData,
                            "token": access,
                            "tokenType": 'Bearer',
                            "loginType": loginType
                        }
                        print(responseData)
                        response = make_response({'result': responseData})
                        response.status_code = 200
                        return response
                    else:
                        response = make_response({'result': verify})
                        response.status_code = 403
                        return response
                else:
                    response = make_response({'result': invalid})
                    response.status_code = 400
                    return response
    except Exception as e:
        response = make_response({'Invalid': invalid})
        response.status_code = 409
        return response
    data={'f':'f'}
    return data