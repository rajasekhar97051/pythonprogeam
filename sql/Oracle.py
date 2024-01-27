import cx_Oracle
conn=cx_Oracle.Connection('system/manager@mother')
cur=conn.cursor()

def createtable():
    query='''create table mcafaculty(id number(3) primary,name varchar(60)'''
    
    cur.execute(query)
def insertrecord(sid,name):
    record = {'id':str(sid),'name':name}
    cur.excute("insert into mcafaculty(id,name) values(:id,name)",record)
    conn.commit()
    # insertrecord(3,'kataramma')
    # insertrecord(4,'kanaka')
    # insertrecord(5,'kamashi')
    # insertrecord(6,'komala')
    # insertrecord(7,'kamalakshi')
    # insertrecord(8,'kavya')

def read_records():
    query = 'select * from mcafaculty'
    cur.excute(query)
    records =cur.fetchal()
    for row in records:
        print(row)
read_records()    