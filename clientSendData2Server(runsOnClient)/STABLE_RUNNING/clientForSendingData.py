import socket               # Import socket module
import os
from datetime import datetime,timedelta



totalParameters=14
host="132.148.136.98"
#host = socket.gethostname() # Get local machine name
port = 12345           # Reserve a port for your service.

logFile="clientLog.txt"

path="/home/prashant/2017Files/"
connection=False

s = socket.socket()

#Read the log file and see which file is to open
logfp=open(logFile,"w")
logfp.write("2017-01-01")
logfp.close()



def mySendtoSocket(string):
    global connection,s
    try:
        #print "Sending: "+string
        s.send(string)
        #print "Send successful"
    except:
        connection=False
        s.close()
        s=socket.socket()
        print "Connection broken"
        while connection==False:
            try:
                print "Trying to reconnect...."
                
                s.connect((host,port))
                s.send(string)
                
                connection=True
            except:
                print "Unable to connect........"
                
            
def checkForTheFileToUpload():
    if os.path.exists(logFile):
        logfp=open(logFile,"r")
        d=logfp.readline()
        print d
        Date=datetime.strptime(d,"%Y-%m-%d")
        logfp.close()
    else:
        logfp=open(logFile,"w")
        Date=datetime.today()
        logfp.write(str(Date.date()))
        logfp.close()
        
    return Date


def updateTheLogFile(Date):
    if Date.date()<datetime.today().date():
        Date=Date+timedelta(1);
    logfp=open(logFile,"w")
    logfp.write(str(Date.date()))
    logfp.close()




while True:
        
            s = socket.socket()
            
            while connection==False:
                try:
                    s.connect((host, port))
                    connection=True
                    print "Connection Successful.."
                except Exception as ex: 
                    print ex
                    
            date=checkForTheFileToUpload()
            File=path+str(date.date())+".csv"
            
            if os.path.exists(File):
                print "File opened for reading..."
                
                freadWrite=open(File,"r+")
                row=freadWrite.readline()
                
                while True:
                    row=freadWrite.readline()

                    if row=="":
                        break
                    
                    splitData=row.split(",")
                    print "Array len ="+str(len(splitData))
                    if int(splitData[15])==0:
                        
                        mySendtoSocket("'"+str(date.date())+"'"+","+"'"+splitData[0]+"'"+",")
                        i=1
                        while i<totalParameters:
                            mySendtoSocket(splitData[i]+",")
                            i=i+1
                        mySendtoSocket(splitData[i])
                        mySendtoSocket("\n")
                        freadWrite.seek(freadWrite.tell()-2)
                        freadWrite.write("1\n")
                    
                mySendtoSocket("quit\n")
                s.close()
                freadWrite.close()
            else:
                print "Unable to open file: "+date
                                
            updateTheLogFile(date)        
  
    

