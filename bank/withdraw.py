import datetime

from flask import request, make_response
from service import database
from random_object_id import generate

id = generate()

pmsql = database.database()
cursor = pmsql.cursor()


def withdraw():
    global cusId
    global bankId
    global depositId
    global amount
    res = request.json
    customerId = res['customerId']
    bankid = res['bankId']
    withdrawAmount = int(res['withdrawAmount'])
    date = datetime.datetime.now()
    try:
        getAmount = f"""select id,customerId,bankId,depositAmount from deposit where customerId = '{customerId}'"""
        cursor.execute(getAmount)
        var = cursor.fetchall()
        if len(var) > 0:
            for i in var:
                depositId = i[0]
                cusId = i[1]
                bankId = i[2]
                amount = int(i[3])
    except Exception as e:
        print(e)

    try:
        deposits = f"""create table withdraw(id varchar(100),customerId varchar(100),bankId varchar(100),withdrawAmount varchar(100),
           date varchar(100),depositId varchar(100))"""
        cursor.execute(deposits)
        cursor.commit()
    except Exception as e:
        print(e)
    try:
        if customerId == cusId and bankid == bankId:
            if amount > withdrawAmount:
                insertAmount = f"""insert into withdraw(id,customerId,bankId,withdrawAmount,date,depositId) values('{id}','{customerId}','{bankId}',{withdrawAmount},'{date}','{depositId}')"""
                deposit = f"""update deposit set depositAmount={amount - withdrawAmount} where customerId='{customerId}'"""
                cursor.execute(insertAmount)
                cursor.execute(deposit)
                cursor.commit()
                response = make_response({'result': ' Withdrawal Successfully'})
                response.status_code = 200
                return response
            else:
                response = make_response({'result': 'Insufficient amount'})
                response.status_code = 200
                return response
    except Exception as e:
        print(e)
    data = {'result': 'error'}
    return data
