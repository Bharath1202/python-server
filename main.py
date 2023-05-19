from flask import Flask
from flask_cors import CORS
from waitress import serve
from service import database
from auth import register, login, resetPassword, newpassword
import pandas as pd
import datetime

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

pmsql = database.database()
cursor = pmsql.cursor()

from threading import Timer


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


@app.route('/register', methods=['POST'])
def registerForm():
    returnData = register.reg()
    print(returnData)
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


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=3070)
