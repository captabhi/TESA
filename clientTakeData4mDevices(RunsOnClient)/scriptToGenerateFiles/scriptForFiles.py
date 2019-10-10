import random
from datetime import datetime
dd=1
mm=1
yy=2016
dMax=31
for mm in range(1,13):
    if (mm<10):
        mmStr="0"+str(mm)
    else:
        mmStr=str(mm)
    if mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12:
        dMax=32
    elif mm==2:
        dMax=29
    else:
        dMax=31
    
    for dd in range(1,dMax):
        if(dd<10):
            ddStr="0"+str(dd)
        else:
            ddStr=str(dd)
        fp=open(str(yy)+"-"+mmStr+"-"+ddStr+".csv","w")
        fp.write("Time,Vac1,Vac2,Vac3,Vpv1,Vpv2,Iac1,Iac2,Iac3,Ipv1,Ipv2,Pnow,Etoday,Eall,Fault Code,Upload Status\n")
        hour=9
        minute=0
        for row in range(1,600):
            fp.write(str(hour)+":"+str(minute)+",")
            for col in range(1,14):
                fp.write(str(random.randint(0,65535)))
                fp.write(",")
            minute=minute+1
            if minute >59:
                hour=hour+1
                minute=0
            
            fp.write("0,0")
            
            fp.write("\n")
        fp.close()

yy=2017
for mm in range(1,int(datetime.today().month)+1):
    if (mm<10):
        mmStr="0"+str(mm)
    else:
        mmStr=str(mm)
    if mm==int(datetime.today().month):
        dMax=int(datetime.today().day)+1
    elif mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12:
        dMax=32
    elif mm==2:
        dMax=29
    else:
        dMax=31
    print dMax
    
    for dd in range(1,dMax):
        if(dd<10):
            ddStr="0"+str(dd)
        else:
            ddStr=str(dd)
        path="/home/prashant/2017Files/"    
        fp=open(path+str(yy)+"-"+mmStr+"-"+ddStr+".csv","w")
        fp.write("Time,Vac1,Vac2,Vac3,Vpv1,Vpv2,Iac1,Iac2,Iac3,Ipv1,Ipv2,Pnow,Etoday,Eall,Fault Code,Upload Status\n")
        hour=9
        minute=0
        for row in range(1,600):
            fp.write(str(hour)+":"+str(minute)+",")
            for col in range(1,14):
                fp.write(str(random.randint(0,65535)))
                fp.write(",")
            minute=minute+1
            if minute >59:
                hour=hour+1
                minute=0
            
            fp.write("0,0")
            fp.write("\n")
        fp.close()
