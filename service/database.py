import pyodbc as p


def database():
    DriverName = 'SQL SERVER'
    ServerName = "DESKTOP-Q0GC56U\SQLEXPRESS"
    DatabaseName = 'MASTER'

    conn = p.connect(f"""DRIVER={DriverName};SERVER={ServerName};DATABASE={DatabaseName};Trust_Connections=yes""")
    return conn
