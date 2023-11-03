import pyodbc as p


def database():
    DriverName = 'SQL SERVER'
    # serverName = "DESKTOP-3URKGSG\SQLEXPRESS"
    # office server
    serverName = "DESKTOP-2TJG5N9\SQLEXPRESS"
    DatabaseName = 'master'
    #
    conn = p.connect(f"""DRIVER={DriverName};SERVER={serverName};DATABASE={DatabaseName};Trust_Connections=yes""")
    return conn
