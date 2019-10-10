import socket               # Import socket module

host = socket.gethostname() # Get local machine name
port = 12345           # Reserve a port for your service.


path="/home/prashant/2016Files/"

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

        s = socket.socket()         # Create a socket object
        s.connect((host, port))
        date=str(yy)+"-"+mmStr+"-"+ddStr
        fp=open(path+date+".csv","r")
        fp.readline()
        for row in fp:
            splitData=row.split(",")
            s.send("'"+date+"'"+","+"'"+splitData[0]+"'"+",")
            i=1
            while i<=12:
                s.send(splitData[i]+",")
                i=i+1
            s.send(splitData[i])

            
        s.send("quit\n")
        s.close()
        fp.close()



