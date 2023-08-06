import mysql.connector
import pyodbc as p

def database():
    DriverName = 'SQL SERVER'
    ServerName = "DESKTOP-3URKGSG\SQLEXPRESS"
    DatabaseName = 'master'
    #
    conn = p.connect(f"""DRIVER={DriverName};SERVER={ServerName};DATABASE={DatabaseName};Trust_Connections=yes""")
    return conn

