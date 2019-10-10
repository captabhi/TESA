import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt
fileName="2017-07-29.csv"
fp=open(fileName,"r")
            
index=10
#First row specifies particular parameter name            
print fp.readline()
            
#Xdata=range(len(csvReader))
Xdata=[]
Ydata=[]
xtick=[]

i=0
splitedData=fp.readline().split(",")
Ydata.append(int(splitedData[index]))
time=datetime.strptime(splitedData[0],"%H:%M")
startTime=time
Xdata.append(time.hour*60+time.minute)
xtick.append(str(startTime.hour)+":"+str(startTime.minute))


for row in fp:
    splitedData=row.split(",") 
    Ydata.append(int(splitedData[index]))
    time=datetime.strptime(splitedData[0],"%H:%M")
    Xdata.append(time.hour*60+time.minute)
    if ((time.hour-startTime.hour)*60+(time.minute-startTime.minute))>29:
        startTime=time
        xtick.append(str(startTime.hour)+":"+str(startTime.minute))
    
    #if i>100:
    #    break
    #i=i+1



Etoday=splitedData[11]
runTime=time-datetime.strptime(xtick[0],"%H:%M")
print runTime
deviceId=1
plt.scatter(Xdata,Ydata)
temp= np.arange(min(Xdata), max(Xdata), 30)


plt.text(540,70000,"Device Id:"+str(deviceId)+"     Date:"+fileName)
plt.xlabel("Time\nRun Time :"+str(runTime)+"\nEtoday = "+str(Etoday)+" KWh")
plt.ylabel("Power")
plt.grid(True)
plt.tight_layout()
plt.xticks(temp,xtick)
plt.plot(Xdata,Ydata)
plt.show()


