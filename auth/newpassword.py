from flask import request,make_response
from service import database
from helpers import commonErrors
from pyodbc import Error

pmsql = database.database()
cursor = pmsql.cursor()
for i in commonErrors.errors:
    reset = i['success']['reset']
    notMarch = i['error']['notMatch']
def newPassword():
    res = request.json
    email = res['email']
    newPass= res['newPassword']
    reTypepass = res['reTypePassword']
    register_table = f"""select * from register where email='{email}' """
    cursor.execute(register_table)
    register_data = cursor.fetchall()
    try:
        for i in register_data:
            emailId = i[1]
            if newPass == reTypepass:
                change_password = f"""update register set password='{reTypepass}' where email='{emailId}'"""
                cursor.execute(change_password)
                cursor.commit()
                response = make_response({'result': reset})
                response.status_code = 200
                return response
            else:
                response = make_response({'result': notMarch})
                response.status_code = 403
                return response
    except Error as e:
        print(e)
    data = {'r':'k'}
    return data