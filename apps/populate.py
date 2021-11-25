import mysql.connector
import uuid
from random import randint
from time import time
import datetime

conn = mysql.connector.connect(
    host='db', port='3306', user='dba', password='dba', database='test')

cursor = conn.cursor(prepared=True)

createTable = """
CREATE TABLE IF NOT EXISTS users (
    name varchar(25),
    age varchar(3),
    createdAt timestamp
)
"""

cursor.execute(createTable)

stmt = 'INSERT INTO users (name, age, createdAt) VALUES (%s, %s, %s)'

for i in range(0, 300000):
    name = str(uuid.uuid4())[:25]
    age = randint(10, 100)
    ts = time()
    timestamp = datetime.datetime.fromtimestamp(
        ts).strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute(stmt, (name, str(age), timestamp,))

conn.commit()

cursor.execute('select count(*) from users')

for i in cursor:
    print(i)

conn.close()
