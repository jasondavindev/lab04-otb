import mysql.connector
import os

IS_PREPARED = os.getenv('IS_PREPARED')

print('Exetuing with IS_PREPARED?', IS_PREPARED != None)

conn = mysql.connector.connect(
    host='db', port='3306', user='dba', password='dba', database='test')

cursor = conn.cursor(prepared=(IS_PREPARED != None))

for i in range(0, 101):
    if IS_PREPARED:
        stmt = "SELECT count(*) FROM users where age = %s"
        cursor.execute(stmt, (str(i),))
    else:
        stmt = "SELECT count(*) FROM users where age = '%s'" % (str(i))
        cursor.execute(stmt)
    print(stmt)

    for (count) in cursor:
        print(count)

conn.close()
