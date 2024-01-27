import cx_Oracle
conn=cx_Oracle.Connection('system/manager@mother')
cur=conn.cursor()

def createtable():
    query='''create table mcafaculty(id number(3) primary,name varchar(60);'''
    
    cur.execute(query)
def insertrecord():
    query='''insert into mcafaculty(id,name) values(1,'praveen')'''
    cur.execute(query)
    conn.commit()