import psycopg2

# Setting up the bloctrox database.
conn = psycopg2.connect(database="bloctrox", # the database in which I created in psql
                        host="localhost",
                        user="postgres",
                        password="password of the datbase",
                        port="5432")
# created a cursor
cursor = conn.cursor()

# Executing a SQL query to insert data into  table
insert_query = """ INSERT INTO bloctrox (id, user_name, eth_address) VALUES (101, 'orion3000', '0x455A569b9c7eE32E3EC5dadAe3413f1355972e0D')"""


cursor.execute(insert_query)
conn.commit()
print("1 Record inserted in BlocTrox Database successfully")

# Fetch result
cursor.execute("SELECT * FROM bloctrox")
record = cursor.fetchall()
print("Result ", record)

# Executing a SQL query to update table
update_query = """Update bloctrox set user_name = '3000Orion' where id = 90"""
cursor.execute(update_query)
conn.commit()
count = cursor.rowcount
print(count, "Record updated successfully ")

# Fetch result
cursor.execute("SELECT * FROM bloctrox")
print("Result ", cursor.fetchall())

# Deletion of a query
delete_query = """Delete FROM bloctrox where id = 90"""
cursor.execute(delete_query)
conn.commit()
count = cursor.rowcount
print(count, "Record deleted successfully ")

# Fetch result
cursor.execute("SELECT * from bloctrox")
print("Result ", cursor.fetchall())




