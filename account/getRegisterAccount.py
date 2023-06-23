from service import database
from pyodbc import Error
from flask import Flask, request

pmsql = database.database()
cursor = pmsql.cursor()


def getRegisterAcc():
    accArray = []
    try:
        getAcc = f"""select * from account_Register"""
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
                "status": i[15]
            }
            accArray.append(res)
        data = {'result': accArray}
        return data
    except Error as e:
        print(e)
    value = {'res': 'response'}
    return value


def getSingleAccount():
    singleAccArray = []
    try:
        res = request.json
        value = res['param']['updates']
        for i in value:
            id = i['param']
            getData = f"""select * from account_Register where _id='{id}'"""
            cursor.execute(getData)
            detail = cursor.fetchall()
            print(detail)
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
                    "status": i[15]
                }
            singleAccArray.append(res)
            data = {'result': singleAccArray}
            return data
    except Error as e:
        print(e)
    data = {'result': 'response'}
    return data
