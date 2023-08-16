from service import database
from flask import Flask, request,make_response

pmsql = database.database()
cursor = pmsql.cursor()


def getRegisterCsutomerAcc():
    customeraccArray = []
    try:
        getAcc = f"""select * from customer_account"""
        cursor.execute(getAcc)
        acc = cursor.fetchall()
        for i in acc:
            res = {
                "_id": i[0],
                "firstName": i[1],
                "lastName": i[2],
                "age": i[3],
                "dateOfBirth": i[4],
                "gender": i[5],
                "email": i[6],
                "password":i[7],
                "mobileNumber": i[8],
                "alternateNumber": i[9],
                "martialStatus": i[10],
                "address": i[11],
                "nationality": i[12],
                "religion": i[13],
                "pincode": i[14],
                "userImage": i[15],
                "status": i[16],
                "registerDate":i[17],
                "bankName":i[18],
                "bankAccno":i[19],
                "ifscCode":i[20]
            }
            customeraccArray.append(res)
        data = {'result': customeraccArray}
        return data
    except Exception as e:
        print(e)
    value = {'res': 'response'}
    return value


def getSingleCustomerAccount():
    singlecutomerAccArray = []
    try:
        res = request.json
        value = res['params']['updates']
        for i in value:
            id = i['value']
            getData = f"""select customer._id,customer.accountNumber,customer.firstName,customer.lastName,
            customer.mobileNumber,b.bankName,customer.ifscCode,customer.userImage from customer_account as customer
            left join bank as b ON customer.bankName = b._id where customer._id = '{id}'"""
            cursor.execute(getData)
            detail = cursor.fetchall()
            for i in detail:
                res = {
                    "_id": i[0],
                    "accountNumber": i[1],
                    "firstName": i[2],
                    "lastName": i[3],
                    "mobileNumber": i[4],
                    "bankName": i[5],
                    "ifscCode": i[6],
                    "userImage": i[7],
                }
            singlecutomerAccArray.append(res)
            response1 = make_response({'result': singlecutomerAccArray})
            response1.status_code = 200
            return response1
    except Exception as e:
        response = make_response({'result': e})
        response.status_code = 400
        return response
    data = {'result': 'response'}
    return data
