import pyodbc

class MSDBconnection():
    #should establish the connection with any database we have in MS SQL
    def __init__(self):
        self.server = "databases2.spartaglobal.academy"
        self.database = "Northwind"
        self.username = "SA"
        self.password = "Passw0rd2018"
        self.cursor = self.conn.cursor()

    #
    def _establish_connection(self):
        connection = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        return connection
# we need to add self to call the particular instances
    #open to sql injections if you do this, abstract? :/
    def __sql_query(self, sql_string):
        #call method to filter out drop table and DELETE * and only allow certain SQL queries
        return self.cursor.execute(sql_string)

nwind = MSDBconnection
nwind.sql_query('SELECT * FROM PRODUCTS')

print(nwind.sql_query('SELECT * FROM PRODUCTS'))
