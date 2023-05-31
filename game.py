from datetime import datetime
from threading import Timer
from random import randint
from service import database
from pyodbc import Error
pmsql = database.database()
cursor = pmsql.cursor()

try:
    create_period_table = f"""create table gameTable(date varchar(15), price varchar(10), number varchar(1),
           result varchar(10))"""
    cursor.execute(create_period_table)
    cursor.commit()
except Error as e:
    print(e)
class Timers(object):
    def __init__(self):

        self.number = 0
        self.price = '102'
        self.priceNumber = 0
        self.time()
        # self.callColor()

    def time(self):
        date = datetime.now().utctimetuple()
        year = date.tm_year
        month = date.tm_mon
        day = date.tm_mday
        dateFormat = f"{year}{month}{day}"
        self.number += 1
        self.priceNumber += 1
        self.finalDate = f"{dateFormat}{self.number}"
        r = randint(0,100)
        self.totalPrice = f"102{r}"
        Timer(1, self.time).start()

    def callColor(self):
        number = randint(0,9)
        print(number)
        if number % 2 == 0:
            self.color = '#00FF00'
            self.priceData = f"{self.totalPrice}{number}"
            response = {
                "date": self.finalDate,
                "price": self.priceData,
                "number": number,
                "color": self.color
            }
            insert_period_table = f"""insert into gameTable(date,price,number,result) values('{self.finalDate}','{self.priceData}','{number}','{self.color}')"""
            cursor.execute(insert_period_table)
            cursor.commit()
            return response
        else:
            self.color = '#ff0000'
            self.priceData = f"{self.totalPrice}{number}"
        Timer(1, self.callColor).start()
        response = {
            "date": self.finalDate,
            "price": self.priceData,
            "number": number,
            "color": self.color
        }
        insert_period_table = f"""insert into gameTable(date,price,number,result) values('{self.finalDate}','{self.priceData}','{number}','{self.color}')"""
        cursor.execute(insert_period_table)
        cursor.commit()
        return response

data = Timers()
