
from datetime import datetime
f=open("2015-01-01.csv","r")

y=[]
s=f.readline().split(",")
print s
time=datetime.strptime(f.readline().split(",")[0],"%H:%M")
print time
f.close()
    
