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
            findData = f"""select _id,firstName,lastName,age,dateOfBirth,email,password,mobileNumber,address,
            userImage,bankId from customer_account where email='{email}'"""
            cursor.execute(findData)
            var = cursor.fetchall()
            print('dddd', var)
            for i in var:
                user = [
                    {
                        '_id': i[0],
                        'firstName': i[1],
                        'lastName': i[2],
                        'age': i[3],
                        'DOB': i[4],
                        'email': i[5],
                        "mobileNumber": i[7],
                        'address': i[8],
                        'bankId': i[9],
                        'userImage': i[10]
                    }
                ]
            # print(user)
                userEmail = i[5]
                userPassword = i[6]
                responsePassword1 = cryptocode.decrypt(userPassword, "password")
                if len(var) > 0:
                    if userEmail == email and responsePassword1 == password:
                        access = token.create_access_token(data={'email': email})
                        responseData = {
                            "userDetails": user,
                            "token": access,
                            "tokenType": 'Bearer',
                            "loginType": loginType
                        }
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
        response = make_response({'Invalid': e})
        response.status_code = 409
        return response
    data = {'f': 'f'}
    return data
