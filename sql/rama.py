import cx_Oracle,csv
conn=cx_Oracle.Connection('system/manager@mother')
cur=conn.cursor()

def createtable():
    query='''create table mcaraja(id number(3) primary key,name varchar(60))'''
    cur.execute(query)
#createtable()

def insertrecord(sid,name):
    record = {'id':str(sid),'name':name}
    cur.execute("insert into mcaraja(id,name) values(:id,:name)",record)
    conn.commit()
# insertrecord(3,'raju')
# insertrecord(4,'ramana')
# insertrecord(5,'rajkumar')
# insertrecord(6,'raja')
# insertrecord(7,'ramanna')
# insertrecord(8,'ravi')
def read_records():
    query='select *from mcaraja'
    cur.execute(query)
    records=cur.fetchall()
    with open('recoeds.csv','w',newline='') as csvfile:
        data=csv.writer(csvfile)
        data.writerow(['id','name'])
    for row in records:
        data.writerow(row)
#read_records()
def fetch_records(sid):
    record={'id':str(sid)}
    query ='select * from mcaraja where id = :id'
    cur.execute(query,record)
    record=cur.fetchall()
    for row in record:
        print(row)
#fetch_records(2)
def update_name(sid):
    fetch_records(sid)
    name=input('enter new name to update :-')
    record={'id':str(sid),'name':name}
    query='update mcaraja set name = %s where id =: id'
    cur.execute(query,record)
    conn.commit()
    fetch_records(sid)
def delete_records(sid):
    record={'id':str(sid)}
    query ='delete from mcaraja where id=id'
    cur.execute(query,record)
    conn.commit()
#delete_records(2)
def truncate():
    query ='truncate table mcaraja' 
def insert_from_csv():
    with open('records.csv','r') as csvfile:
        data=csv.reader(csvfile)
        data=list(data)
        for row in range(1,len(data)):
          insertrecord(*data[row])