# here we want to connect mysql with python by
# 1. click settings
# 2.project database_to_mysql
# 3. python interpreter then click'+' symbol and add mysql-connector from the dropdown and install package


# mysql-connector
# step1 import mysql module
# step2 establish connection
#       mysql -u root -p password@123 (in ubuntu)
# step3 create cursor object
# step4 execute mysql query
# step5 close database connection

import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",password="password@123",auth_plugin="mysql_native_password")
cur=db.cursor()
sql="select version()"
cur.execute(sql)
data=cur.fetchone()
print(data)