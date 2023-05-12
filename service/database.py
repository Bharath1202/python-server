import pyodbc as p


def database():
    DriverName = 'SQL SERVER'
    ServerName = "DESKTOP-Q0GC56U\SQLEXPRESS"
    DatabaseName = 'MASTER'

    conn = p.connect(f"""DRIVER={DriverName};SERVER={ServerName};DATABASE={DatabaseName};Trust_Connections=yes""")
    # conn = p.connect(
    #     'Driver={SQL Server};SERVER=' + server_name + ';DATABASE=' + db_name + ';UID=' + user_name + ';PWD=' + password)
    return conn
