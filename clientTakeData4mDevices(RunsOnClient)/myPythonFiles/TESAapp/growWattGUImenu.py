#!usr/bin/env python
 
import minimalmodbus
import time
import serial
import pickle as fp
import datetime
import matplotlib.pyplot as plt
from Tkinter import *

deviceId=1


root=Tk()

#frame2=Frame(root)
menu=Menu(root)
root.config(menu=menu)

today=datetime.date.today()
lastday=today

frame1=Frame(root)
frame1.pack()
settingMenu = Menu(menu)
menu.add_cascade(label="Setting", menu=settingMenu)

def showSiteDetails():
    print "Site Details:"

def blank():
    print "not implemented"

def showExportData():
    print "export data"

settingMenu.add_command(label="Site Details",command=showSiteDetails)
historyMenu=Menu(settingMenu)
settingMenu.add_cascade(label="History",menu=historyMenu)
historyMenu.add_command(label="Daily",command=blank)
historyMenu.add_command(label="Monthly",command=blank)
historyMenu.add_command(label="Yearly",command=blank)
settingMenu.add_command(label="Export Data",command=showExportData)




f=open(str(today)+".csv","w")

labelId=Label(frame1,text="Device Id : "+ str(deviceId),fg="black",bg="white")
labelId.grid(padx=10,pady=5,row=1,column=0)
labelCap=Label(frame1,text=" INSTALLED CAPACITY 05 KW ",fg="black",bg="white")
labelCap.grid(padx=10,pady=5,row=2,column=0)



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


DateTime=[]


#RegisterAddresses

Vac1Addr=14
Vac2Addr=18
Vac3Addr=22
Vpv1Addr=3
Vpv2Addr=7
Iac1Addr=15
Iac2Addr=19
Iac3Addr=23
Ipv1AddrH=5
Ipv1AddrL=6
Ipv2AddrH=9
Ipv2AddrL=10
PnowAddrH=11
PnowAddrL=12
EtodayAddrH=26
EtodayAddrL=27
EallAddrH=28
EallAddrL=29

##########################################################

Vac1=0
Vac2=0
Vac3=0
Vpv1=0
Vpv2=0
Iac1=0
Iac2=0
Iac3=0
Ipv1=0
Ipv2=0
Pnow=0
Etoday=0
Eall=0


labelDT=Label(frame1,text=" Date and Time : " + str(DateTime),fg="blue",bg="white")
labelDT.grid(padx=10,pady=5,ipadx=0,row=4,column=0)

labelVac=Label(frame1,text=" Vac : "+ str(Vac1)+"V / "+str(Vac2)+"V / "+str(Vac3)+"V",fg="blue",bg="white")
labelVac.grid(padx=10,pady=5,ipadx=0,row=5,column=0)

labelVpv=Label(frame1,text=" Vpv : "+ str(Vpv1)+"V / "+str(Vpv2)+"V",fg="red",bg="white")
labelVpv.grid(padx=10,pady=5,row=6,column=0)

labelIac=Label(frame1,text=" Iac : "+ str(Iac1)+"A / "+str(Iac2)+"A / "+str(Iac3)+"A",fg="green",bg="white")
labelIac.grid(padx=10,pady=5,row=7,column=0)

labelIpv=Label(frame1,text=" Ipv : "+ str(Ipv1)+"A / "+str(Ipv2)+"A",fg="magenta",bg="white")
labelIpv.grid(padx=10,pady=5,row=8,column=0)

labelPnow=Label(frame1,text=" Pnow : "+str(Pnow)+"kW",fg="yellow",bg="white")
labelPnow.grid(padx=10,pady=5,ipadx=0,row=5,column=1)

labelEtoday=Label(frame1,text=" Etoday : "+str(Etoday)+"kW",fg="brown",bg="white")
labelEtoday.grid(padx=10,pady=5,ipadx=0,row=6,column=1)

labelEall=Label(frame1,text=" Eall : "+str(Eall)+"kW",fg="purple",bg="white")
labelEall.grid(padx=10,pady=5,ipadx=0,row=7,column=1)

def fetchBasicData(data):    
    #global Vac1Addr,Vac2Addr,Vac3Addr,Vpv1Addr,Vpv2Addr,Iac1Addr,Iac2Addr,Iac3Addr,Ipv1AddrH,Ipv1AddrL,Ipv2AddrH,Ipv2AddrL,PnowAddrH,PnowAddrL,EtodayAddrH,EtodayAddrL,EallAddr,EallAddrL
    global Vac1,Vac2,Vac3,Vpv1,Vpv2,Iac1,Iac2,Iac3,Ipv1,Ipv2,Pnow,Etoday,Eall,DateTime
    Vac1=data[Vac1Addr]
    Vac2=data[Vac2Addr]
    Vac3=data[Vac3Addr]
    Vpv1=data[Vpv1Addr]
    Vpv2=data[Vpv2Addr]
    Iac1=data[Iac1Addr]
    Iac2=data[Iac2Addr]
    Iac3=data[Iac3Addr]
    Ipv1=data[Ipv1AddrL]+data[Ipv1AddrH]<<16
    Ipv2=data[Ipv2AddrL]+data[Ipv2AddrH]<<16
    Pnow=data[PnowAddrL]+data[PnowAddrH]<<16
    Etoday=data[EtodayAddrL]+data[EtodayAddrH]<<16
    Eall=data[EallAddrL]+data[EallAddrH]<<16
    DateTime=time.asctime( time.localtime(time.time()) )
    
    
    
    
    
def guiUpdate(frame1):
    #global Vac1,Vac2,Vac3,Vpv1,Vpv2,Vpv3,Iac1,Iac2,Iac3,Ipv1,Ipv2,Ipv3,Pnow,Etoday,Eall,DateTime#,labelVac,labelVpv,labelIac,labelIpv,labelPnow,labelEtoday,labelEall
    labelDT.config(text=" Date and Time : " + str(DateTime))
    labelVac.config(text=" Vac : "+ str(Vac1)+" V / "+str(Vac2)+" V / "+str(Vac3)+" V")
    labelVpv.config(text=" Vpv : "+ str(Vpv1)+" V / "+str(Vpv2)+" V")
    labelIac.config(text=" Iac : "+ str(Iac1)+" A / "+str(Iac2)+" A / "+str(Iac3)+" A")
    labelIpv.config(text=" Ipv : "+ str(Ipv1)+" A / "+str(Ipv2)+" A")
    labelPnow.config(text=" Pnow : "+str(Pnow)+" kW")    
    labelEtoday.config(text=" Etoday : "+str(Etoday)+" kW")
    labelEall.config(text=" Eall : "+str(Eall)+" kW")
    frame1.update_idletasks()
    frame1.update()





def makeCSVfile():
    global f,today,lastday
    today = datetime.date.today()
    if(str(today)==str(lastday)):
        f.write(str(DateTime)+","+str(Vac1)+","+str(Vac2)+","+str(Vac3)+","+str(Vpv1)+","+str(Vpv2)+","+str(Iac1)+","+str(Iac2)+","+str(Iac3)+","+str(Ipv1)+","+str(Ipv2)+",")
        f.write(str(Pnow)+","+str(Etoday)+","+str(Eall))
        f.write("\n")
    else:
        f.close()
        f.open(str(today)+".csv","a")
    lastday=today
    


startingAddr=0
totalRegisters=31
registerType=4


if instrument.debug == True:
	print instrument

i=0

while i<20:
        dataArray=[]
        print " i = " + str(i) +"\n"
        reg=startingAddr
        while reg<totalRegisters+startingAddr:
            try:
                dataReceived = instrument.read_registers(reg,1,registerType)
                frame1.update_idletasks()
                frame1.update()
                dataArray.append(dataReceived[0])
                
            except ValueError,TypeError:
                dataArray.append(-1)
            except IOError:
                #print "no response"
                while True:
                    try:
                        print "no response"
                        instrument.read_registers(0,1,4)
                    except IOError:
                        continue
                    except ValueError,TypeError:
                        print "",
                    break
            reg=reg+1
        print dataArray
        fetchBasicData(dataArray)
        guiUpdate(frame1)
        makeCSVfile()
        i=i+1
        del(dataArray)
f.close()
