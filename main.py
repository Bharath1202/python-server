from flask import Flask
from flask_cors import CORS
from waitress import serve
from service import database
from auth import register
from auth import login

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

pmsql = database.database()
cursor = pmsql.cursor()


@app.route('/register', methods=['POST'])
def registerForm():
    returnData = register.reg()
    data = {'res': returnData}
    return data


@app.route('/register/login', methods=['POST'])
def loginData():
    logReturn = login.loginForm()
    return logReturn


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=3070)
