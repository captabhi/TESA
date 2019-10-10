import datetime
import csv


today=datetime.date.today()
f=open(str(today)+".csv","r")
reader=csv.reader(f)

for row in reader:
    #for col in row:
    print row
    print
