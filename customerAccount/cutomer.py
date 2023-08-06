from flask import request, make_response
from service import database
from helpers import commonErrors
from random_object_id import generate

id = generate()

for i in commonErrors.errors:
    register = i['success']['register']
    login = i['success']['login']
    error = i['error']['exists']
    status = i['success']['status']

pmsql = database.database()
cursor = pmsql.cursor()

try:
    create_new_account = f"""create table customer_account(_id varchar (40),firstName varchar(15),lastName varchar( 
    4),age varchar(2), dateOfBirth varchar(30), gender varchar(7), email varchar(30),password varchar(50), mobileNumber varchar(10), 
    alternateNumber varchar(10) ,martialStatus varchar(10),address varchar(500), nationality varchar(10), 
    religion varchar(10),pincode varchar(6),userImage varchar(170),status varchar(20),registerdDate varchar(30),
    bankName varchar(100), accountNumber varchar(16),ifscCode varchar(10))"""
    cursor.execute(create_new_account)
    cursor.commit()
except Exception as e:
    print(e)


def newcustomerAcc():
    global customerId
    global verifyDate
    global registerDate
    global userImage
    res = request.json
    id = res['_id']
    print(id)
    try:
        getData = f"""select * from account_Register where _id='{id}'"""
        cursor.execute(getData)
        customerId = cursor.fetchall()
        for i in customerId:
            registerDate = i[16]
            userImage = i[14]
            print(registerDate)
            # date = pd.Timestamp(registerDate)
            # verifyDate = pd.Timedelta(datetime.now() - date).seconds / 86400
    except Exception as e:
        print(e)

    fname = res['firstName']
    lname = res['lastName']
    age = res['age']
    dateOfBirth = res['dateOfBirth']
    gender = res['gender']
    email1 = res['email']
    password = '123456'
    mobile = res['mobileNumber']
    alternate = res['alternateNumber']
    martialStatus = res['martialStatus']
    address = res['address']
    nationality = res['nationality']
    religion = res['religion']
    pincode = res['pincode']
    userImage = userImage
    bankName = res['bankName']
    bankAccNo = res['accountNumber']
    ifscCode = res['ifscCode']
    currentDate = registerDate
    status = 'In-progress'
    try:
        insert_table = f"""insert into customer_account(_id ,firstName,lastName,age,dateOfBirth,gender,email,password,
        mobileNumber, alternateNumber,martialStatus,address,nationality, religion,pincode,userImage,status,registerdDate,bankName,
        accountNumber,ifscCode) values('{id}','{fname}','{lname}','{age}','{dateOfBirth}',
        '{gender}','{email1}','{password}', '{mobile}',
                 '{alternate}','{martialStatus}','{address}',
                 '{nationality}','{religion}','{pincode}','{userImage}','{status}','{currentDate}','{bankName}','{bankAccNo}','{ifscCode}')"""
        cursor.execute(insert_table)
        cursor.commit()
        for i in customerId:
            cusId = i[0]
            delete_account_register = f"""delete from account_Register where _id='{cusId}'"""
            cursor.execute(delete_account_register)
            delete_account_register1 = f"""delete from account_Register where mobileBumber='{mobile}'"""
            cursor.execute(delete_account_register1)
            cursor.commit()
        response1 = make_response({'success': register})
        response1.status_code = 200
        return response1
    except Exception as e:
        print(e)

    data = {'g': 'gg'}
    return data
