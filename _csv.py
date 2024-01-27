import csv
#file = open('sample.csv','w')
with open('sample.csv','w')as file:
    data=[
        [1,'Chandan',23],
        [2,'Nandan',22],
        [3,'Bandan',54]

        ]
    record=csv.writer(file)
    record.writerow(['id,name','age'])
    record.writerows(data)