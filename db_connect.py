import pyodbc


# connecting_to_python = pyodbc.connect('driver= {OBDC driver for SQL}; Server = databases2.spartaglobal.academy;')

server = "databases2.spartaglobal.academy"
database = "Northwind"
username = "SA"
password = "Passw0rd2018"


connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

#making a cursor,,, keeos state.. (deck of cards )

cursor = connection.cursor

# being a code plumber and investigating

print(connection)
print(cursor)

query_result = cursor.execute("SELECT * FROM Products")

print(query_result.fetchone())

#fetchone() remember curson maintains state
# if you want to get back to the start, you need a new curson or to the run the command again

print(query_result.fetchone()) # one less card in the deck
print(query_result.fetchone()) # one less card in the deck /////
data_point_card = query_result.fetchone()  # object

# this one entry of data is a 'pyodbc.Row' object
print(type(data_point_card))


# can behave like an iterable list
print(data_point_card[1])

# makes it like an oop list now, where initialized parameters are the column name... like light! particle and wave
print(data_point_card.ProductName)
#
# fetchall ---> output next all pyodbc.Row into list --- remember cursor maintains state (i.e. deck of cards)

# dangerous - dont use irl as a db could have 1000000 entries

list_of_all_rows = query_result.fetchall()



while True:
#     use our query results or cursor with query result and
#     fetch one at a time
#    do whatever we want with that data point
# stop the iteration when there is no more data
# or when it is none (py) or null (sql)
row = query_result.fetchone()
print(row.ProductName,'NOW ONLY' row.ProductPrice * 1.25)
if row == None:
    break



# change the order put if above

while True:
#     use our query results or cursor with query result and
#     fetch one at a time
#    do whatever we want with that data point
# stop the iteration when there is no more data
# or when it is none (py) or null (sql)
row = query_result.fetchone()
if row == None:
    break
print(row.ProductName,'NOW ONLY' row.ProductPrice * 1.25)


