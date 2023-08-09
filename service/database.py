import mysql.connector
import pyodbc as p

def database():
    DriverName = 'SQL SERVER'
    # serverName = "DESKTOP-3URKGSG\SQLEXPRESS"
    # office server
    serverName = "DESKTOP-MS21F57\SQLEXP2022"
    DatabaseName = 'master'
    #
    conn = p.connect(f"""DRIVER={DriverName};SERVER={serverName};DATABASE={DatabaseName};Trust_Connections=yes""")
    return conn

