import cx_Oracle
import time
#import csv

try:
    con = cx_Oracle.connect('jessica/shareplex@myrds19c')
    print("Oracle Version: "+str(con.version))
    cursor = con.cursor()
    cmd1 = "truncate table mytest"
    cmd2 = "begin\
              for i in 1..10 loop\
              Insert into mytest values (i,'test');\
              end loop;\
            end;"

    cursor.execute("Drop table mytest purge")
    cursor.execute("create table mytest(id number,\
             name varchar2(10))")
    cursor.execute("alter table mytest add primary key(id)")
    cursor.execute(cmd1)
    cursor.execute(cmd2)
    con.commit()

    print("select * from mytest")
    start = time.time()
    cursor.arraysize = 100
    cursor.execute("select * from mytest")
    res = cursor.fetchall()
    elapsed = (time.time() - start)
    print(elapsed, " seconds")
    print("select * from mytest")
    for r in res:
       print(r)
    #for result in cursor:
    #  print("select count(*) from mytest:"+str(result))
    print("Table created snd inserted succesfully")
except cx_Oracle.DatabaseError as e:
    print("There is a problem with Oracle",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()

