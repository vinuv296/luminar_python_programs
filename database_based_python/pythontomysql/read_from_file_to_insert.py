import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",password="password@123",database="pythonfeb",auth_plugin="mysql_native_password")
cur=db.cursor()
f=open("employee")
for lines in f:
    data=lines.rstrip("\n").split(",")
    sql="insert into employee(eid,ename,designation,salary,location)values(%s,%s,%s,%s,%s)"
    cur.execute(sql,tuple(data))
    db.commit()
db.close()