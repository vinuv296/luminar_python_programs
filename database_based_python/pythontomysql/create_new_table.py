import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",password="password@123",database="pythonfeb",auth_plugin="mysql_native_password")
cur=db.cursor()
# sql="create table students(id int,name varchar(50),address varchar(50),class varchar(50),total_mark int)"
# cur.execute(sql)
# db.close()

sql="insert into students(id,name,address,class,total_mark)values(100,'vinu','house name','5th',250)"
try:
    cur.execute(sql)
    db.commit()
except Exception as e:
    print(e.args)
    db.rollback()
finally:
    db.close()
