from service import database
from flask import request, make_response
from helpers import commonErrors
from random_object_id import generate

id = generate()

pmsql = database.database()
cursor = pmsql.cursor()
for i in commonErrors.errors:
    register = i['success']['register']
try:
    create_bank = f"""create table bank(_id varchar(100),bankName varchar(100), branch varchar(100),location varchar(100),
    pinCode varchar(6))"""
    cursor.execute(create_bank)
    cursor.commit()
except Exception as e:
    print(e)


def newBank():
    res = request.json
    bank_name: str = res['bankName']
    branch: str = res['branch']
    location: str = res['location']
    pincode: int = res['pinCode']
    try:
        if len(bank_name) > 0:
            insert_bank = f"""insert into bank(_id,bankName,branch,location,pinCode)values('{id}','{bank_name}','{branch}','{location}','{pincode}')"""
            cursor.execute(insert_bank)
            cursor.commit()
            response = make_response({'result': register})
            response.status_code = 200
            return response
    except Exception as e:
        print(e)
    data = {'result': 'error'}
    return data
