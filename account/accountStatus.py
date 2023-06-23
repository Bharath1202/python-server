from flask import Flask, request, make_response
from service import database

pmsql = database.database()
cursor = pmsql.cursor()
def changeStatus():
    res = request.json
    id = res['_id']
    status = res['status']
    update = f"""update customer_account set status='{status}' where _id='{id}'"""
    cursor.execute(update)
    cursor.commit()
    response = make_response({'success': status})
    response.status_code = 200
    d = {'result': status}
    return d