from flask import request, make_response
from service import database

pmsql = database.database()
cursor = pmsql.cursor()


def getAllBank():
    bankArray = []
    try:
        get_bank = f"""select * from bank"""
        cursor.execute(get_bank)
        bank_account = cursor.fetchall()
        for i in bank_account:
            account = {
                '_id': i[0],
                "bankName": i[1],
                "branch": i[2],
                "location": i[3],
                "pinCode": i[4]
            }
            bankArray.append(account)
        response = make_response({'result': bankArray})
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    data = {'l': 'p'}
    return data
