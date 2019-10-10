#!usr/bin/env python
 
import minimalmodbus
import time
import serial
import pickle as fp
import matplotlib.pyplot as plt
from Tkinter import *
from decimal import *

root=Tk()

profileGrowWattV0=[
         1,2,4,9,#Vac1
         
         8,3,0,14,#Vpv
         5,12,11,6,#Iac
         7,15,14,10]#Ipv


slaveAddr=1
slaveSerialPort='/dev/ttyACM0'

instrument = minimalmodbus.Instrument(slaveSerialPort,slaveAddr) 

instrument.serial.baudrate = 9600
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

testFile=open("testDataFile.txt","w");


Vac=0
Vpv=0
Iac=0
Ipv=0
DateTime=0

startingAddr=0
totalRegisters=40
registerType=4

def applyFormula(data):
    count=0
    global Vac,Vpv,Iac,Ipv,DateTime,profileGrowWattV0
    for i in profileGrowWattV0:
        if count<Vac:
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

if instrument.debug == True:
	print instrument

i=1
dataArray=[]
while i<20:
    reg=startingAddr
        while reg<totalRegisters+startingAddr:
            try:
                dataReceived = instrument.read_registers(reg,1,registerType)
                
                print dataReceived
                
                #for j in dataReceived:
                #    print(Decimal(j))
                #applyFormula(dataReceived,profile)
                #print " Vac : " , Vac
                #print " Vpv : " , Vpv
                #print " Iac : " , Iac
                #print " Ipv : " , Ipv
                #print " Date and Time :",DateTime
                
                #fp.dump(test_reg,logFile)     
                #logFile.write(" ")
                #p.dump(time.time(),logFile)
                #time.sleep (1)
                dataArray.append(dataReceived)
                
            except Exception as ex:
                print ex
                dataArray.append(-1)

            reg=reg+1
        applyFormula(dataReceived)
        i=i+1
#logFile.close();
