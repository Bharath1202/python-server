from flask import request, make_response
from service import database
from pyodbc import Error
from helpers import token
from helpers import commonErrors

pmsql = database.database()
cursor = pmsql.cursor()

for i in commonErrors.errors:
    register = i['success']['register']
    login = i['success']['login']
    error = i['error']['exists']
    invalid = i['error']['invalidEmail']
def loginForm():
    res = request.json
    email = res['email']
    loginType = ''
    try:
        findData = f"""select * from register where email='{email}' """
        cursor.execute(findData)
        var = cursor.fetchall()
        for i in var:
            if i[1] == "admin@gmail.com":
                loginType = 'admin'
            else:
                loginType = "user"
        access = token.create_access_token(data={'email': email})
        if len(var) > 0:
            responseData = {
                    "userDetails": email,
                    "token": access,
                    "tokenType": 'Bearer',
                    "loginType": loginType
                    }
            response = make_response({'res':responseData})
            response.status_code = 200
            return response
    except Error as e:
        response = make_response({'Invalid':invalid})
        response.status_code = 409
        return response

    # except Error as e:
    #     response = make_response({'error': e})
    #     response.status_code = 409
    #     return response
    # findData = database.db['register'].find_one({'email':email})
    # if email == findData['email']:
    #     if email == 'admin@gmail.com':
    #         loginType = 'admin'
    #         access = token.create_access_token(data={'email': email})
    #         response = {
    #             "userDetails": [{'email': email}],
    #             "token": access,
    #             "tokenType": 'Bearer',
    #             "loginType": loginType
    #         }
    #     else:
    #         loginType = "user"
    #         access = token.create_access_token(data={'email': email})
    #         response = {
    #                 "userDetails": [{'email': email}],
    #                 "token": access,
    #                 "tokenType": 'Bearer',
    #                 "loginType": loginType
    #         }
    #     return response
    data = {'Invalid':invalid}
    return data
# if __name__ == "__main__":
#     serve(app, host="0.0.0.0", port=3070)
