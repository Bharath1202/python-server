import datetime

from flask import request, make_response
from service import database
from random_object_id import generate

id = generate()

pmsql = database.database()
cursor = pmsql.cursor()

def withdraw():
    global cusId
    global id
    global amount
    try:
        getAmount = f"""select * from deposit"""
        cursor.execute(getAmount)
        var = cursor.fetchall()
        if len(var) > 0:
            for i in var:
                id = i[0]
                cusId = i[1]
                amount = int(i[3])
    except Exception as e:
        print(e)

    res = request.json
    customerId = res['customerId']
    bankId = res['bankId']
    totalamount = int(res['withdrawtamount'])
    date = datetime.datetime.now()
    try:
        deposits = f"""create table withdraw(id varchar(100),customerId varchar(100),bankId varchar(100),withdrawAmount varchar(100),
           date varchar(100),depositId varchar(100))"""
        cursor.execute(deposits)
        cursor.commit()
    except Exception as e:
        print(e)
    try:
        insertAmount = f"""insert into deposit(id,customerId,bankId,withdrawAmount,date,depositId) values('{id}','{customerId}','{bankId}',{totalamount},'{date}','{id}')"""
        print(insertAmount)
        # cursor.execute(insertAmount)
        # cursor.commit()
        # response = make_response({'result': 'Save Successfully'})
        # response.status_code = 200
        # return response
    except Exception as e:
        print(e)
    data = {'result': 'error'}
    return data