import mysql.connector


def database():
    connect = mysql.connector.connect(user='root',
                          host='localhost',
                              password='Bharath@123',
                                port=3306,
                              database='project')
    # DriverName = 'SQL SERVER'
    # ServerName = "DESKTOP-Q0GC56U\SQLEXPRESS"
    # DatabaseName = 'MASTER'
    #
    # conn = p.connect(f"""DRIVER={DriverName};SERVER={ServerName};DATABASE={DatabaseName};Trust_Connections=yes""")
    return connect

