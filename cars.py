import sqlite3
import pandas as pd


conn = sqlite3.connect('cars.db')
cursor = conn.cursor()
print("Database created and Successfully Connected to SQLite")

'''
## create new table for cars.csv
table = 'CREATE TABLE cars (name TEXT, year INTEGER, selling_price INTEGER, km_driven INTEGER, fuel TEXT, seller_type TEXT, transmission INTEGER, owner TEXT)'
cursor = conn.cursor()
cursor.execute(table)
conn.commit()
print('Table created successfully')

# load the data into a Pandas DataFrame
cars = pd.read_csv('cars.csv')
# write the data to a sqlite table
cars.to_sql('cars', conn, if_exists='append', index = False)
'''

# fetch all rows from cars table
cursor.execute('''SELECT * FROM cars''').fetchall()

# Select first 5 record from the table
query_select = 'SELECT * FROM cars LIMIT 5'
for i in cursor.execute(query_select):
    print(i)

#query 1: select top 3 selling_price cars
query1 =  """SELECT name, year, selling_price 
           FROM cars
           Order by selling_price DESC
           LIMIT 3;"""
top_price = cursor.execute(query1).fetchall()

# show result
print("\n Top 3 sell price cars:")
for car in top_price:
    print(car)

#query 2: select top 5 oldest cars
query2 =  """SELECT name, year 
           FROM cars
           Order by year ASC
           LIMIT 5;"""
oldest_year = cursor.execute(query2).fetchall()

# show result
print("\n Top 5 oldest cars:")
for car in oldest_year:
    print(car)

#query 3: select top 5 km_driven cars with manual transmission
query3 =  """SELECT name, km_driven, transmission 
           FROM cars
           WHERE transmission = 'Manual'
           Order by km_driven DESC
           LIMIT 5;"""
most_driven = cursor.execute(query3).fetchall()

# show result
print("\n Top 5 driven cars with manual transmission:")
for car in most_driven:
    print(car)

#query 4: select top 5 selling_price cars which have more than one onwers
query4 =  """SELECT name, selling_price, owner 
           FROM cars
           WHERE owner != 'First Owner'
           Order by selling_price DESC
           LIMIT 5;"""
top_price = cursor.execute(query4).fetchall()

# show result
print("\n Top 5 selling_price cars which have more than one onwers:")
for car in top_price:
    print(car)

#query 5: select top 5 selling_price cars which are not sold by individual
query5 =  """SELECT name, selling_price, seller_type 
           FROM cars
           WHERE seller_type != 'Individual'
           Order by selling_price DESC
           LIMIT 5;"""
top_price = cursor.execute(query5).fetchall()

# show result
print("\n Top 5 5 selling_price cars which are not sold by individual:")
for car in top_price:
    print(car)