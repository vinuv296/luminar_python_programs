import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",password="password@123",database="pythonfeb",auth_plugin="mysql_native_password")
cur=db.cursor()
sql="update students set total_mark=300 where id=100"
try:
    cur.execute(sql)
    db.commit()
except Exception as e:
    print(e.args)
    db.rollback()
finally:
    db.close()