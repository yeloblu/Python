#to test connection with mysql database

import mysql.connector;

cn=mysql.connector.connect(host="localhost",user="root",password="",database="atul");
print(cn);
