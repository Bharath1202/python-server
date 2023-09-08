import datetime

from flask import request, make_response
from service import database
from random_object_id import generate

id = generate()

pmsql = database.database()
cursor = pmsql.cursor()


def deposit():
    res = request.json
    customerId = res['customerId']
    bankId = res['bankId']
    totalamount = int(res['depositAmount'])
    date = datetime.datetime.now()
    print('ddd', date)
    try:
        deposits = f"""create table deposit(id varchar(100),customerId varchar(100),bankId varchar(100),depositAmount varchar(100),
        date varchar(100))"""
        cursor.execute(deposits)
        cursor.commit()
    except Exception as e:
        print(e)
    try:
        insertAmount = f"""insert into deposit(id,customerId,bankId,depositAmount,date) values('{id}','{customerId}','{bankId}',{totalamount},'{date}')"""
        cursor.execute(insertAmount)
        cursor.commit()
        response = make_response({'result': 'Save Successfully'})
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    data = {'result': 'error'}
    return data


def getDeposit():
    getDepositArray = []
    get = "select * from deposit"
    cursor.execute(get)
    data = cursor.fetchall()
    try:
        if len(data) > 0:
            for i in data:
                res = {
                    "amount": i[3],
                    "date": i[4]
                }
                getDepositArray.append(res)
            return getDepositArray
    except Exception as e:
        print(e)
    data = {'result': 'error'}
    return data
