from flask import Flask, request
from flask_cors import CORS
from waitress import serve
from service import database
from auth import register, login, resetPassword, newpassword
import pandas as pd
import datetime
from account import accountRegister, getRegisterAccount, accountStatus
from pyodbc import Error
from helpers import commonErrors
from customerAccount import cutomer

newArray = []
app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

pmsql = database.database()
cursor = pmsql.cursor()

from threading import Timer

for i in commonErrors.errors:
    status = i['success']['status']


def call():
    otpData = f"""select * from OTP"""
    cursor.execute(otpData)
    var = cursor.fetchall()
    for i in var:
        time1 = i[2]
        validTimeId = i[0]
        present_time = pd.Timestamp(time1)
        data = pd.Timedelta(datetime.datetime.now() - present_time).seconds / 60
        print(data)
        if data > 1:
            drop_dataBase = f"""delete from OTP where ID='{validTimeId}'"""
            cursor.execute(drop_dataBase)
            cursor.commit()
        else:
            print('out')
    Timer(5, call).start()


# def getGameData():
#     gameData = f"""select * from gameTable"""
#     cursor.execute(gameData)
#     data = cursor.fetchall()
#     for i in data:
#         try:
#             if len(i) > 0:
#                 return i
#             else:
#                 print('out')
#         except Error as e:
#             print(e)


@app.route('/register', methods=['POST'])
def registerForm():
    returnData = register.reg()
    return returnData


@app.route('/login', methods=['POST'])
def loginData():
    logReturn = login.loginForm()
    return logReturn


@app.route('/email', methods=['POST'])
def opt():
    otpReturn = resetPassword.opt()
    return otpReturn


call()


@app.route('/newPassword', methods=['POST'])
def newPass():
    newPasswordReturn = newpassword.newPassword()
    return newPasswordReturn


@app.route('/accountRegister', methods=['POST'])
def newAcc():
    newAccountRegister = accountRegister.newAccountRegister()
    return newAccountRegister


@app.route('/getAccount', methods=['GET'])
def getAllRegisterAccount():
    returnGetAccount = getRegisterAccount.getRegisterAcc()
    return returnGetAccount


@app.route('/getSingleAccount', methods=['PUT'])
def getSingle():
    returnAccountDetail = getRegisterAccount.getSingleAccount()
    return returnAccountDetail


@app.route('/changeStatus', methods=['POST'])
def status():
    returnStatus = accountStatus.changeStatus()
    return returnStatus


@app.route('/customerAccount', methods=['POST'])
def customerAcc():
    returnCustomerAccount = cutomer.newcustomerAcc()
    print(returnCustomerAccount)
    return returnCustomerAccount


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=3070)
