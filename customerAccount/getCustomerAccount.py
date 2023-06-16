from service import database
from pyodbc import Error
from flask import Flask, request

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
                "mobileNumber": i[7],
                "alternateNumber": i[8],
                "martialStatus": i[9],
                "address": i[10],
                "nationality": i[11],
                "religion": i[12],
                "pincode": i[13],
                "userImage": i[14],
                "status": i[15],
                "registerDate":i[16],
                "bankName":i[17],
                "bankAccno":i[18],
                "ifscCode":i[19]
            }
            customeraccArray.append(res)
        data = {'result': customeraccArray}
        return data
    except Error as e:
        print(e)
    value = {'res': 'response'}
    return value


def getSingleCustomerAccount():
    singlecutomerAccArray = []
    try:
        res = request.json
        value = res['param']['updates']
        for i in value:
            id = i['value']
            getData = f"""select * from customer_account where _id='{id}'"""
            cursor.execute(getData)
            detail = cursor.fetchall()
            for i in detail:
                res = {
                    "_id": i[0],
                    "firstName": i[1],
                    "lastName": i[2],
                    "age": i[3],
                    "dateOfBirth": i[4],
                    "gender": i[5],
                    "email": i[6],
                    "mobileNumber": i[7],
                    "alternateNumber": i[8],
                    "martialStatus": i[9],
                    "address": i[10],
                    "nationality": i[11],
                    "religion": i[12],
                    "pincode": i[13],
                    "userImage": i[14],
                    "status": i[15],
                    "registerDate": i[16],
                    "bankName": i[17],
                    "bankAccno": i[18],
                    "ifscCode": i[19]
                }
            singlecutomerAccArray.append(res)
            data = {'result': singlecutomerAccArray}
            return data
    except Error as e:
        print(e)
    data = {'result': 'response'}
    return data
