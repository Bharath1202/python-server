# from datetime import datetime
# from threading import Timer
# from random import randint
# from service import database
# from pyodbc import Error
# pmsql = database.database()
# cursor = pmsql.cursor()
# time = datetime.now()
# try:
#     create_period_table = f"""create table gameTable(date varchar(15), price varchar(10), number varchar(1),
#            result varchar(10),time varchar(50))"""
#     cursor.execute(create_period_table)
#     cursor.commit()
# except Error as e:
#     print(e)
# class Timers(object):
#     def __init__(self):
#
#         self.number = 0
#         self.price = '102'
#         self.priceNumber = 0
#         self.time()
#         # self.callColor()
#
#     def time(self):
#         date = datetime.now().utctimetuple()
#         year = date.tm_year
#         month = date.tm_mon
#         day = date.tm_mday
#         dateFormat = f"{year}{month}{day}"
#         self.number += 1
#         self.priceNumber += 1
#         self.finalDate = f"{dateFormat}{self.number}"
#         r = randint(0,100)
#         self.totalPrice = f"102{r}"
#         # Timer(120, self.time).start()
#
#     def callColor(self):
#         number = randint(0,9)
#         if number % 2 == 0:
#             self.color = '#00FF00'
#             self.priceData = f"{self.totalPrice}{number}"
#             response = {
#                 "date": self.finalDate,
#                 "price": self.priceData,
#                 "number": number,
#                 "color": self.color
#             }
#             insert_period_table = f"""insert into gameTable(date,price,number,result,time) values('{self.finalDate}','{self.priceData}','{number}','{self.color}','{time}')"""
#             cursor.execute(insert_period_table)
#             cursor.commit()
#             return response
#         else:
#             self.color = '#ff0000'
#             self.priceData = f"{self.totalPrice}{number}"
#         # Timer(120, self.callColor).start()
#         response = {
#             "date": self.finalDate,
#             "price": self.priceData,
#             "number": number,
#             "color": self.color
#         }
#         insert_period_table = f"""insert into gameTable(date,price,number,result,time) values('{self.finalDate}','{self.priceData}','{number}','{self.color}','{time}')"""
#         cursor.execute(insert_period_table)
#         cursor.commit()
#         return response
#
# data = Timers()




# def gameList():
#     returnGame = game.Timers().callColor()
#     Timer(120, gameList).start()
#
#
# gameList()
#
#
# @app.route('/game', methods=['GET'])
# def g():
#     global list_data
#     gameData = f"""select * from gameTable"""
#     cursor.execute(gameData)
#     data1 = cursor.fetchall()
#     for i in data1:
#         list_data = {
#             'date': i[0],
#             'price': i[1],
#             'number': i[2],
#             'color': i[3]
#         }
#         newArray.append(list_data)
#     print(newArray)
#     data = {'res': newArray}
#     return data
