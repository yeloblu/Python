import mysql.connector;

cn=mysql.connector.connect(host="localhost",user="root",password="",database="atul");
print(cn);

cursor=cn.cursor();
deptno=input("enter dept no::");
dname=input("enter dname::");
loc=input("enter loc::");

cursor.execute("insert into dept values("+deptno+", ''"+dname+"'',''"+loc+"'')");
cn.commit();

print("Dept saved ");
