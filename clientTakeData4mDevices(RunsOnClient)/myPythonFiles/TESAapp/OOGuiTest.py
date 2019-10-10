#!usr/bin/env python
 
import minimalmodbus
import time
import serial
import pickle as fp
import datetime #import datetime 
import matplotlib.pyplot as plt
import csv
from Tkinter import *
import os.path
                


root=Tk()




#################################################################
#instrument initialisation

slaveAddr=13

slaveSerialPort='/dev/ttyACM0'

instrument = minimalmodbus.Instrument(slaveSerialPort,slaveAddr) 

instrument.serial.baudrate = 19200
instrument.serial.bytesize = 8
instrument.serial.parity = serial.PARITY_NONE
instrument.serial.stopbits= 1
instrument.serial.timeout= 0.2                		
instrument.mode	= minimalmodbus.MODE_RTU
instrument.debug = False
instrument.serial.xonxoff= True
instrument.serial.rtscts= False
instrument.serial.dsrdtr= False
minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL= False

######################################################################
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




#####################################################################


class mainWindow(Frame):

    
    today=datetime.date.today()
    lastday=today
    f=open(str(today)+".csv","w")
    deviceId=1
    Time=[]
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

    def __init__(self,instrument,root):
        Frame.__init__(self,root)

        self.menu=Menu(self)
        root.config(menu=self.menu)

        self.today=datetime.date.today()
        self.lastday=self.today


        self.settingMenu = Menu(self.menu)
        self.menu.add_cascade(label="Setting", menu=self.settingMenu)


        self.settingMenu.add_command(label="Site Details",command=self.showSiteDetails)
        self.historyMenu=Menu(self.settingMenu)
        self.settingMenu.add_cascade(label="History",menu=self.historyMenu)
        self.historyMenu.add_command(label="Daily",command=self.dailyDataPlot)
        self.historyMenu.add_command(label="Monthly",command=self.monthlyDataResult)
        self.historyMenu.add_command(label="Yearly",command=self.blank)
        self.settingMenu.add_command(label="Export Data",command=self.showExportData)





        
        self.labelId=Label(self,text="Device Id : "+ str(self.deviceId),fg="black",bg="white")
        self.labelId.grid(padx=10,pady=5,ipadx=40,row=1,column=1,sticky="N")

        self.labelCap=Label(self,text=" INSTALLED CAPACITY 05 KW ",fg="black",bg="white")
        self.labelCap.grid(padx=10,pady=5,ipadx=10,row=2,column=1,sticky="W")

        self.labelDT=Label(self,text=" Date and Time : " + str(self.Time),fg="blue",bg="white")
        self.labelDT.grid(padx=10,pady=5,row=2,column=0,sticky="W")

        self.labelVac=Label(self,text=" Vac : "+ str(self.Vac1)+"V / "+str(self.Vac2)+"V / "+str(self.Vac3)+"V",fg="blue",bg="white")
        self.labelVac.grid(padx=10,pady=5,ipadx=20,row=5,column=0,sticky="W")

        self.labelVpv=Label(self,text=" Vpv : "+ str(self.Vpv1)+"V / "+str(self.Vpv2)+"V",fg="red",bg="white")
        self.labelVpv.grid(padx=10,pady=5,ipadx=20,row=6,column=0,sticky="W")

        self.labelIac=Label(self,text=" Iac : "+ str(self.Iac1)+"A / "+str(self.Iac2)+"A / "+str(self.Iac3)+"A",fg="green",bg="white")
        self.labelIac.grid(padx=10,pady=5,ipadx=20,row=7,column=0,sticky="W")

        self.labelIpv=Label(self,text=" Ipv : "+ str(self.Ipv1)+"A / "+str(self.Ipv2)+"A",fg="magenta",bg="white")
        self.labelIpv.grid(padx=10,pady=5,ipadx=20,row=8,column=0,sticky="W")

        self.labelPnow=Label(self,text=" Pnow : "+str(self.Pnow)+"kW",fg="yellow",bg="white")
        self.labelPnow.grid(padx=10,pady=5,ipadx=20,row=5,column=2,sticky="W")

        self.labelEtoday=Label(self,text=" Etoday : "+str(self.Etoday)+"kW",fg="brown",bg="white")
        self.labelEtoday.grid(padx=10,pady=5,ipadx=20,row=6,column=2,sticky="W")

        self.labelEall=Label(self,text=" Eall : "+str(self.Eall)+"kW",fg="purple",bg="white")
        self.labelEall.grid(padx=10,pady=5,ipadx=20,row=7,column=2,sticky="W")

    def showSiteDetails(self):
        print "Site Details:"

    def blank(self):
        print "not implemented"

    def showExportData(self):
        print "export data"


    def dailyDataPlot(self):


        def getAndPlot():

           fileName=str(yyyy.get())+"-"+str(mm.get())+"-"+str(dd.get())
           readFile=open("/home/prashant/pythonGeneratedFiles/"+fileName+".csv","r")
           csvReader=csv.reader(readFile)
           index=int(param.get())
           if index > 13:
               index=13
            
           #Xdata=range(len(csvReader))
           Ydata=[]
           for row in csvReader:
               Ydata.append(int(row[index-1]))
           Xdata=range(len(Ydata))
           plt.plot(Xdata,Ydata)
           plt.show()
        

        win= Toplevel(self)
        Label(win,text="Enter Parameter Index (1-13):").pack(side="left")#.grid(row=1,column=1)
        param=Entry(win,bd=5,width=3)
        param.pack(side="left")#.grid(row=1,column=1)
        #Label(win,text="Enter Date:").pack(side="left")
        Label(win,text="DD:").pack(side="left")#.grid(row=2,column=1)
        dd = Entry(win,bd=5,width=3)
        dd.pack(side="left")#grid(row=2,column=1)
        Label(win,text="MM:").pack(side="left")#.grid(row=2,column=2)
        mm = Entry(win,bd=5,width=3)
        mm.pack(side="left")#.grid(row=2,column=2)
        Label(win,text="YYYY:").pack(side="left")#.grid(row=2,column=3)
        yyyy = Entry(win,bd=5,width=5)
        yyyy.pack(side="left")#.grid(row=2,column=3)
        
        button=Button(win,text=" PLOT ",command=getAndPlot)
        button.pack(side="left")#.grid(row=3,column=2)

        
        #self.updateGUItasks()


    def monthlyDataResult(self):


        def findEnergyUsed():
           m=month.get()
           if m<10:
               strM="0"+str(m)
           else:
               strM=str(m)
           fileName="2015-"+strM+"-01"
           filePath="/home/prashant/pythonGeneratedFiles/"+fileName+".csv"
           dd=1
           energyIndex=12
           Emonth=0
           peak=0
           
           while os.path.exists(filePath):
                
               readFile=open(filePath,"r")
               csvReader=csv.reader(readFile)
               
               fileName="2015-"+strM+"-01"
               filePath="/home/prashant/pythonGeneratedFiles/"+fileName+".csv"
            

        
        win= Toplevel(self)
        Label(win,text="Enter Month(1-12):",).grid(row=1,col=1)
        month=Entry(win,bd=5,width=3)
        month.grid(row=1,col=1)
        button=Button(win,text=" DONE ",command=getAndPlot)
        button.grid(row=3,col=2)

        
    def fetchBasicData(self,data):    

        self.Vac1=data[Vac1Addr]
        self.Vac2=data[Vac2Addr]
        self.Vac3=data[Vac3Addr]
        self.Vpv1=data[Vpv1Addr]
        self.Vpv2=data[Vpv2Addr]
        self.Iac1=data[Iac1Addr]
        self.Iac2=data[Iac2Addr]
        self.Iac3=data[Iac3Addr]
        self.Ipv1=data[Ipv1AddrL]+data[Ipv1AddrH]<<16
        self.Ipv2=data[Ipv2AddrL]+data[Ipv2AddrH]<<16
        self.Pnow=data[PnowAddrL]+data[PnowAddrH]<<16
        self.Etoday=data[EtodayAddrL]+data[EtodayAddrH]<<16
        self.Eall=data[EallAddrL]+data[EallAddrH]<<16
        self.Time=str(time.asctime( time.localtime(time.time()) ))
        
        
    def guiUpdate(self):

        self.labelDT.config(text=" Date and Time : " + str(self.Time))
        self.labelVac.config(text=" Vac : "+ str(self.Vac1)+" V / "+str(self.Vac2)+" V / "+str(self.Vac3)+" V")
        self.labelVpv.config(text=" Vpv : "+ str(self.Vpv1)+" V / "+str(self.Vpv2)+" V")
        self.labelIac.config(text=" Iac : "+ str(self.Iac1)+" A / "+str(self.Iac2)+" A / "+str(self.Iac3)+" A")
        self.labelIpv.config(text=" Ipv : "+ str(self.Ipv1)+" A / "+str(self.Ipv2)+" A")
        self.labelPnow.config(text=" Pnow : "+str(self.Pnow)+" kW")    
        self.labelEtoday.config(text=" Etoday : "+str(self.Etoday)+" kW")
        self.labelEall.config(text=" Eall : "+str(self.Eall)+" kW")
        self.update_idletasks()
        self.update()


    def makeCSVfile(self):
        self.today = datetime.date.today()
        if(str(self.today)==str(self.lastday)):
            self.f.write(str(self.Time)+","+str(self.Vac1)+","+str(self.Vac2)+","+str(self.Vac3)+","+str(self.Vpv1)+","+str(self.Vpv2)+","+str(self.Iac1)+","+str(self.Iac2)+","+str(self.Iac3)+","+str(self.Ipv1)+","+str(self.Ipv2)+",")
            self.f.write(str(self.Pnow)+","+str(self.Etoday)+","+str(self.Eall))
            self.f.write("\n")
        else:
            self.f.close()
            self.f.open(str(self.today)+".csv","a")
        self.lastday=self.today

    def updateGUItasks(self):
        self.update_idletasks()
        self.update()
        
    

    def mainFunction(self,startingAddr,totalRegisters,registerType):
        i=0
        while i<20:
                dataArray=[]
                print " i = " + str(i) +"\n"
                reg=startingAddr
                while reg<totalRegisters+startingAddr:
                    try:
                        dataReceived = instrument.read_register(reg,0,registerType)
                        dataArray.append(dataReceived)
                        self.updateGUItasks()
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
                self.fetchBasicData(dataArray)
                self.updateGUItasks()    
                self.guiUpdate()
                self.updateGUItasks()
                self.makeCSVfile()
                self.updateGUItasks()
                i=i+1
                del(dataArray)
        self.f.close()



startingAddr=0
totalRegisters=31
registerType=4

obj=mainWindow(instrument,root)
obj.pack()
obj.mainFunction(startingAddr,totalRegisters,registerType)
root.mainloop()





