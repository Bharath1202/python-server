from flask import Flask
from flask_cors import CORS
from waitress import serve

import customerAccount.cutomer
from service import database
from auth import register, login, resetPassword, newpassword
import pandas as pd
import datetime
from account import accountRegister, getRegisterAccount, accountStatus
from bank import bank, getBank, deposit, withdraw
from helpers import commonErrors
from customerAccount import cutomer, getCustomerAccount
from datetime import datetime

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
    if (len(var) > 0):
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


def verify():
    try:
        getData = f"""select * from customer_account"""
        cursor.execute(getData)
        customerId = cursor.fetchall()
        for i in customerId:
            id = i[0]
            registerDate = i[17]
            date = pd.Timestamp(registerDate)
            verifyDate = pd.Timedelta(datetime.now() - date).seconds / 30
            if verifyDate > 20:
                dataBase = f"""update customer_account set status='verify' where _id='{id}'"""
                cursor.execute(dataBase)
                cursor.commit()
    except Exception as e:
        print(e)
    Timer(5, verify).start()


verify()


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
    return returnCustomerAccount


@app.route('/getAllCustomerAccount', methods=['GET'])
def getCusAcc():
    getCustomerAcc = getCustomerAccount.getRegisterCsutomerAcc()
    return getCustomerAcc


@app.route('/getCustomerAccount', methods=['PUT'])
def getSingleCusAcc():
    getSingleCustomerAcc = getCustomerAccount.getSingleCustomerAccount()
    return getSingleCustomerAcc


@app.route('/registerBank', methods=['POST'])
def registerBankAcc():
    return_bank = bank.newBank()
    return return_bank


@app.route('/getAllBank', methods=['GET'])
def getAllBankAcc():
    return_get_bank = getBank.getAllBank()
    print(return_get_bank)
    return return_get_bank


@app.route('/deposit', methods=['POST'])
def depositAmount():
    amount = deposit.deposit()
    return amount


@app.route('/getAllDeposit', methods=['GET'])
def getdepositAmount():
    getamount = deposit.getDeposit()
    return getamount


@app.route('/uploadImage', methods=['POST'])
def uploadImg():
    image = cutomer.uploadImage()
    return image


@app.route('/withdraw', methods=['POST'])
def withdrawAmt():
    withdrawamount = withdraw.withdraw()
    return withdrawamount


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=3070)
