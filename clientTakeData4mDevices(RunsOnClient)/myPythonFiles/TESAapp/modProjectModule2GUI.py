#!usr/bin/env python
 
import minimalmodbus
import time
import serial
import pickle as fp
import matplotlib.pyplot as plt
from Tkinter import *

root=Tk()
deviceId=1

f=open("logFile.csv","w")

labelId=Label(root,text="Device Id : "+ str(deviceId),fg="black",bg="white")
labelId.grid(padx=10,pady=5,row=1,column=0)
labelCap=Label(root,text=" INSTALLED CAPACITY 05 KW ",fg="black",bg="white")
labelCap.grid(padx=10,pady=5,row=2,column=0)


profile=[1,2,4,9,#Vac
         8,3,0,14,#Vpv
         5,12,11,6,#Iac
         7,15,14,10]#Ipv


slaveAddr=13
slaveSerialPort='/dev/ttyACM0'

instrument = minimalmodbus.Instrument(slaveSerialPort,slaveAddr) 

instrument.serial.baudrate = 19200
instrument.serial.bytesize = 8
instrument.serial.parity = serial.PARITY_NONE
instrument.serial.stopbits= 1
instrument.serial.timeout= 1                		
instrument.mode	= minimalmodbus.MODE_RTU
instrument.debug = False
instrument.serial.xonxoff= True
instrument.serial.rtscts= False
instrument.serial.dsrdtr= False
minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL= False

#logFile=open("logForModbus68.txt","w");


Vac=0
Vpv=0
Iac=0
Ipv=0
DateTime=[]

startingAddr=0
totalRegisters=16
registerType=4

def applyFormula(data,profile):
    count=0
    global Vac,Vpv,Iac,Ipv,DateTime
    for i in profile:
        if count<4:
            Vac=Vac+data[i]
        elif count<8:
            Vpv=Vpv+data[i]
        elif count<12:
            Iac=Iac+data[i]
        else:
            Ipv=Ipv+data[i]
        count=count+1
    Vac=Vac/(count/4)
    Vpv=Vpv/(count/4)
    DateTime=time.asctime( time.localtime(time.time()) )


labelDT=Label(root,text=" Date and Time : " + str(DateTime),fg="blue",bg="white")
labelDT.grid(padx=0,pady=5,ipadx=0,row=4,column=0)

labelVac=Label(root,text=" Vac : "+ str(Vac),fg="blue",bg="white")
labelVac.grid(padx=0,pady=5,ipadx=0,row=5,column=0)

labelVpv=Label(root,text=" Vpv : "+ str(Vpv),fg="red",bg="white")
labelVpv.grid(padx=0,pady=5,row=6,column=0)

labelIac=Label(root,text=" Iac : "+ str(Iac),fg="green",bg="white")
labelIac.grid(padx=10,pady=5,row=7,column=0)

labelIpv=Label(root,text=" Ipv : "+ str(Ipv),fg="magenta",bg="white")
labelIpv.grid(padx=10,pady=5,row=8,column=0)



def guiUpdate(root):
    global Vac,Vpv,Iac,Ipv,DateTime,labelVac,labelVpv,labelIac,labelIpv
    labelDT.config(text=" Date and Time : " + str(DateTime))
    labelVac.config(text=" Vac : "+ str(Vac))
    labelVpv.config(text=" Vpv : "+ str(Vpv))
    labelIac.config(text=" Iac : "+ str(Iac))
    labelIpv.config(text=" Ipv : "+ str(Ipv))
    
    root.update_idletasks()
    root.update()
            

if instrument.debug == True:
	print instrument
i=0

while True:
        try:      
                dataReceived = instrument.read_registers(startingAddr,totalRegisters,registerType)
                #print (dataReceived)
                applyFormula(dataReceived,profile)
                #print " Vac : " , Vac
                #print " Vpv : " , Vpv
                #print " Iac : " , Iac
                #print " Ipv : " , Ipv
                #print " Date and Time :",DateTime
                f.write(str(DateTime)+","+str(Vac)+","+str(Vpv)+","+str(Iac)+","+str(Ipv))
                f.write("\n")
                guiUpdate(root)
                #fp.dump(test_reg,logFile)     
                #logFile.write(" ")
                #p.dump(time.time(),logFile)
                #time.sleep (0.05)

        except:
                print #("ERROR: Not responding ")
        i=i+1

file.close()
#logFile.close();
