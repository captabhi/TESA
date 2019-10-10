#!usr/bin/env python
 
import minimalmodbus
import time
import serial
import pickle as fp
from datetime import datetime
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import csv
from Tkinter import *
import os.path
import numpy as np                

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import random

root=Tk()

LARGE_FONT= ("Verdana", 12)
style.use("ggplot")



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

    
    today=str(datetime.today().date())
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

        self.today=datetime.today().date()
        self.lastday=self.today


        self.optionMenu = Menu(self.menu)
        self.menu.add_cascade(label="Options", menu=self.optionMenu)


        self.optionMenu.add_command(label="Site Details",command=self.showSiteDetails)
        self.historyMenu=Menu(self.optionMenu)
        self.optionMenu.add_cascade(label="History",menu=self.historyMenu)
        self.historyMenu.add_command(label="Daily",command=self.dailyDataPlot)
        self.historyMenu.add_command(label="Monthly",command=self.monthlyDataResult)
        self.historyMenu.add_command(label="Yearly",command=self.yearlyDataResult)




        self.Xtick=np.arange(0,23*60,30)
        #self.Xtick=range(0,40)
        self.Xticklabels=[]

        for r in range(0,23):
            self.Xticklabels.append(str(r)+":"+"00")
            self.Xticklabels.append(str(r)+":"+"30")
            
                ######Edit axis limits for actual time, time.sleep(),yticks,xticks,xticklabels
        ######
        ######

        self.fig = Figure(figsize=(4,4), dpi=100)
        #f.add_axes([0,100,0,100])
        #self.fig.autofmt_xdate(bottom=0.2, rotation=180, ha='right')
        self.fig.set_tight_layout(True)

        self.a = self.fig.add_subplot(111,xlabel="Time -->",ylabel="Pnow(KW)-->",xticks=self.Xtick,xticklabels=self.Xticklabels,yticks=range(0,1000,100))
        ####Graph axis parameters
        self.a.axis([0*60,60*20,0,1000])

        for label in self.a.get_xmajorticklabels():
            label.set_rotation(70)
            label.set_horizontalalignment("right")
        #self.a.axhline(y=0)
        #self.a.axvline(x=0)
        self.a.spines['left'].set_smart_bounds(True)
        self.a.spines['bottom'].set_smart_bounds(True)


        self.canvas = FigureCanvasTkAgg(self.fig,master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=3,column=0,columnspan=3,sticky="N")#.pack(side="right", fill="both", expand=True)

        ###########
        ###########
        ###########
        
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

        #########
        #########
        #########
        

        
    def showSiteDetails(self):
        
        print "Site Details:"
        siteFile=open("siteDetails.txt","r")
        info=siteFile.read()
        tp=Toplevel(self)
        Label(tp,text=info,fg="white",bg="black").pack(fill=X)
        
        


    def blank(self):
        print "oops!!!!!!!!!!!!!!!!!! blank"

        
    def dailyDataPlot(self):

        


        dateMax=31

        def getAndPlot():
            path="/home/prashant/pythonGeneratedFiles/"
            
            m=int(mm.get())
            d=int(dd.get())
            fileName=yyyy.get()
            if m<10:
                fileName=fileName+"-0"+str(m)+"-"
            else:
                fileName=fileName+"-"+str(m)+"-"
            if d<10:
                fileName=fileName+"0"+str(d)
            else:
                fileName=fileName+str(d)
                
            print fileName
            fp=open(path+fileName+".csv","r")
            
            index=10

            #First row specifies particular parameter name            
            print fp.readline()
                        
            Xdata=[]
            Ydata=[]
            xtick=[]


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
                



            Etoday=splitedData[11]
            runTime=time-datetime.strptime(xtick[0],"%H:%M")
            print runTime
            fig=plt.figure("Device Id:"+str(self.deviceId)+"     Date:"+fileName)
            plt.scatter(Xdata,Ydata)
            temp= np.arange(min(Xdata), max(Xdata), 30)



            plt.xlabel("Time\nRun Time :"+str(runTime)+"\nEtoday = "+str(Etoday)+" KWh")
            plt.ylabel("Power")
            plt.tight_layout()
            plt.grid(True)
            plt.xticks(temp,xtick,rotate=70)
            plt.plot(Xdata,Ydata)
            plt.show()

        
        def updateMaxDate():
            global dateMax
            y=int(yyyy.get())
            m=int(mm.get())
            if m == 1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
                dateMax=31
            elif m==2:
                if y%4==0:
                    if y%400==0 and y%100!=0:
                        dateMax=29
                    else:
                        dateMax=28
                else:
                    dateMax=28
            else:
                dateMax=30
            dd.config(to=dateMax)
           

         
        win= Toplevel(self)

        Label(win,text="DD:").grid(row=2,column=1)#.pack(side="left")#.grid(row=2,column=2)

        dd = Spinbox(win, from_=1, to=dateMax, state="readonly",width=2)
        dd.grid(row=2,column=1)#.pack(side="left")#grid(row=2,column=1)

        Label(win,text="MM:").grid(row=2,column=2)#.pack(side="left")#.grid(row=2,column=2)

        mm = Spinbox(win, from_=1, to=12, state="readonly",command=updateMaxDate,width=2)
        mm.grid(row=2,column=2)#.pack(side="left")#.grid(row=2,column=2)

        Label(win,text="YYYY:").grid(row=2,column=3)#.pack(side="left")#.grid(row=2,column=3)

        yyyy = Spinbox(win, from_=2005, to=2050, state="readonly",command=updateMaxDate,width=5)
        yyyy.grid(row=2,column=3)#.pack(side="left")#.grid(row=2,column=3)
        
        button=Button(win,text=" PLOT ",command=getAndPlot)
        button.grid(row=3,column=2)#.pack(side="left")#.grid(row=3,column=2)

        
        
        #self.updateGUItasks()

    def createMonthlyDataFile(self):

        path="/home/prashant/pythonGeneratedFiles/"
        year="2015"

        powerIndex=10        
        for m in range(1,13):
            totalEnergy=0
            temp=datetime(1900,1,1,0,0,0)
            duration=datetime(1900,1,1,0,0,0)
            peak=0
        
            mFile=year
            if m<10:
                mFile=mFile+"-0"+str(m)
            else:
                mFile=mFile+"-"+str(m)
            
            fm=open(mFile+".csv","w")
            fm.write("Total energy,Peak,Duration\n")
            print "Creating Month :",m," File..............."        
            if m == 1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
                dateMax=31
            elif m==2:
                dateMax=28
            else:
                dateMax=30
            
            for d in range(1,dateMax+1):
                fileName=year        
                
                if m<10:
                    fileName=fileName+"-0"+str(m)+"-"
                else:
                    fileName=fileName+"-"+str(m)+"-"
                if d<10:
                    fileName=fileName+"0"+str(d)
                else:
                    fileName=fileName+str(d)
                if os.path.exists(path+fileName+".csv"):
                    
                    
                    fp=open(path+fileName+".csv","r")
                    print fp.readline().split(",")
                    
                    startTime=datetime.strptime(fp.readline().split(",")[0],"%H:%M")
                    for fileData in fp:
                        singleData=fileData.split(",")
                        if int(singleData[powerIndex]) > peak:
                            peak=singleData[powerIndex]
                    
                    endTime=datetime.strptime(singleData[0],"%H:%M")
                    temp=endTime-startTime
                    duration=duration + temp
                    fp.close()
                    totalEnergy=totalEnergy+int(singleData[11])
            print "Month :"+ str(m)+"-"+year
            print "Total Energy=",totalEnergy
            print "Duration :",duration
            print "Peak :",peak
            fm.write(str(totalEnergy))
            fm.write(",")
            fm.write(str(peak))
            fm.write(",")
            fm.write(str(duration))
            fm.close()


            
    def createYearlyDataFile(self):
        energy=0
        peak=0
        duration=datetime(1900,1,1,0,0,0)
        temp=datetime(1900,1,1,0,0,0)

        fname="2015"#str(datetime.today().year)
        fy=open(fname+".csv","w")
        fy.write("Total energy,Peak,Duration\n")
            
        for m in range(1,13):#int(datetime.today().month)+1):
            fname="2015"
            if m<10:
                fname=fname+"-0"+str(m)
            else:
                fname=fname+"-"+str(m)
            #print fname
            fm=open(fname+".csv","r")
            fm.readline()
            data=fm.readline().split(",")
            if int(data[1])>peak:
                peak=int(data[1])
            energy=energy+int(data[0])
            
            #            temp=
            #print temp
            #print duration
            temp=datetime.strptime(data[2],"%Y-%m-%d %H:%M:%S")-datetime(1900,1,1,0,0,0)
            duration=duration + temp

            
        fy.write(str(energy))
        fy.write(",")
        fy.write(str(peak))
        fy.write(",")
        fy.write(str(duration))
        fy.close()



####    Yet to be implemented
####
####

    """            
    def updateYearlyData(self):
        energy=0
        peak=0
        #duration=datetime(1900,1,1,0,0,0)
      
        fname=str(datetime.today().year)
        fy=open(fname+".csv","w")
        fy.write("Total energy,Peak,Duration\n")
        m=int(datetime.today().month)    
        if m<10:
            fname=fname+"-0"+str(m)
        else:
            fname=fname+"-"+str(m)
                    
        fm=open(fname+".csv","r")
        fm.readline()
        data=fm.readline().split(",")
        if int(data[1])>peak:
            peak=int(data[1])

        energy=energy+int(data[0])
        duration=datetime.strptime(data[2],"%Y-%m-%d %H:%M:%S")#+duration
        fy.write(str(energy))
        fy.write(",")
        fy.write(str(peak))
        fy.write(",")
        fy.write(str(duration))
        fy.close()

    """


        
    def updateMonthlyData(self):
        y,m,d=self.lastday.split("-")
        fm=open(path+y+"-"+m+".csv","r")
        print fm.readline()
        data=fm.readline().split(",")
        fm.close()
        print self.f.readline()
        totalEnergy=int(data[0])+self.Etoday
        startTime=datetime.strptime(self.f.readline().split(",")[0],"%H:%M")
        mx=int(data[1])
        for p in self.f:
            splittedData=p.split(",")
            temp=int(splittedData[10])
            if mx<temp:
                mx=temp
                
        duration=datetime.strptime(splittedData[0],"%H:%M")-startTime
        
        totDur=datetime.strptime(data[2],"%Y-%m-%D %H:%M:%S")+duration
        
        fm=open(path+y+"-"+m+".csv","w")
        fm.write(str(totalEnergy))
        fm.write(",")
        fm.write(str(mx))
        fm.write(",")
        fm.write(str(totDur))
        fm.close()
        
       
    def yearlyDataResult(self):


        monthList=[31,59,90,120,151,181,212,243,273,304,334,365]
        fileName="2015"
        filePath=fileName+".csv"
        readFile=open(filePath,"r")
        readFile.readline()
        data=readFile.readline().split(",")
        Eyear=data[0]
        peak=data[1]
        duration=datetime.strptime(data[2],"%Y-%m-%d %H:%M:%S")
        tp=Toplevel(self)
        tp.title("Year : 2015")
        Label(tp,text="Total Energy used = "+Eyear+" W\nPeak Power used in Year = "+peak+" W\n Total duration energy generated = "+str(monthList[duration.month-1]*24+duration.hour+duration.day*24)+" hours "+str(duration.minute)+" minutes",bg="white",fg="blue").pack(side="top",fill=X)
           
        
        

       
    def monthlyDataResult(self):


        def findEnergyUsed():
            
           m=month.get()
           if int(m)<10:
               strM="0"+str(m)
           else:
               strM=str(m)
           fileName="2015-"+strM
           filePath=fileName+".csv"
           readFile=open(filePath,"r")
           readFile.readline()
           data=readFile.readline().split(",")
           Emonth=data[0]
           peak=data[1]
           duration=datetime.strptime(data[2],"%Y-%m-%d %H:%M:%S")
           #tp=Toplevel(self)
           #tp.title("Year : 2015")
           Label(win,text="Total Energy used = "+Emonth+" W\nPeak Power in Month = "+peak+" W\n Duration energy generated = "+str(int(duration.hour)+int(duration.day)*24)+" hours "+str(duration.minute)+" minutes",bg="white",fg="blue").grid(column=0,row=2,columnspan=2,sticky="N")
                
        win= Toplevel(self)
        win.title("Year : 2015")
        Label(win,text="Select Month:",bg="white").grid(row=0,column=0,sticky="W")
        month=Spinbox(win, from_=1, to=12, state="readonly",width=2,bg="white")
        month.grid(row=0,column=1,sticky="E")
        button=Button(win,text=" DONE ",command=findEnergyUsed)
        button.grid(row=1,column=0,sticky="E")

     
    def fetchBasicData(self,data):    

        self.Vac1=data[Vac1Addr]/10
        self.Vac2=data[Vac2Addr]/10
        self.Vac3=data[Vac3Addr]/10
        self.Vpv1=data[Vpv1Addr]/10
        self.Vpv2=data[Vpv2Addr]/10
        self.Iac1=data[Iac1Addr]/10
        self.Iac2=data[Iac2Addr]/10
        self.Iac3=data[Iac3Addr]/10
        self.Ipv1=(data[Ipv1AddrL]+data[Ipv1AddrH]*65535)/10
        self.Ipv2=(data[Ipv2AddrL]+data[Ipv2AddrH]*65535)/10
        self.Pnow=(data[PnowAddrL]+data[PnowAddrH]*65535)/10
        self.Etoday=(data[EtodayAddrL]+data[EtodayAddrH]*65535)/10
        self.Eall=(data[EallAddrL]+data[EallAddrH]*65535)/10
        self.Time=str(datetime.today().hour)+":"+str(datetime.today().minute)
        
        
    def guiUpdate(self):

        self.labelDT.config(text=" Date and Time : " + str(self.Time))
        self.labelVac.config(text=" Vac : "+ str(self.Vac1)+" V / "+str(self.Vac2)+" V / "+str(self.Vac3)+" V")
        self.labelVpv.config(text=" Vpv : "+ str(self.Vpv1)+" V / "+str(self.Vpv2)+" V")
        self.labelIac.config(text=" Iac : "+ str(self.Iac1)+" A / "+str(self.Iac2)+" A / "+str(self.Iac3)+" A")
        self.labelIpv.config(text=" Ipv : "+ str(self.Ipv1)+" A / "+str(self.Ipv2)+" A")
        self.labelPnow.config(text=" Pnow : "+str(self.Pnow)+" W")    
        self.labelEtoday.config(text=" Etoday : "+str(self.Etoday)+" KWh")
        self.labelEall.config(text=" Eall : "+str(self.Eall)+" KWh")
        self.update_idletasks()
        self.update()


    def makeCSVfile(self):
        self.today = str(datetime.today().date())
        if(str(self.today)==str(self.lastday)):
            self.f.write(str(self.Time)+","+str(self.Vac1)+","+str(self.Vac2)+","+str(self.Vac3)+","+str(self.Vpv1)+","+str(self.Vpv2)+","+str(self.Iac1)+","+str(self.Iac2)+","+str(self.Iac3)+","+str(self.Ipv1)+","+str(self.Ipv2)+",")
            self.f.write(str(self.Pnow)+","+str(self.Etoday)+","+str(self.Eall))
            self.f.write("\n")
        else:
            self.f.close()
            self.f.open(str(self.lastday)+".csv","r")
            self.updateMonthlyData()
            self.f.open(str(self.today)+".csv","w")
        self.lastday=self.today

    def updateGUItasks(self):
        self.update_idletasks()
        self.update()
        
    def plotDataLive1(self,xdata,ydata):
            
        i=0
        xtick=[]
        for j in range(7,20):
            xtick.append(str(j)+":"+"00")
            xtick.append(str(j)+":"+"30")
            
        xtickBand=np.arange(420,20*60+30,30)

        print xtick
        plt.axis([420,20*60+30,0,65535])
        plt.xticks(xtickBand,xtick)
        plt.grid(True)
        plt.tight_layout()
            
        plt.ion()
        y=[]
        x=[]
        while i<600:
            y.append()

            plt.pause(0.05)
            
            plt.plot(x,y)
            
            #plt.show()
            #plt.draw()
            i=i+1
            #plt.show()
        plt.ioff()
        plt.show()
        
    
    
    def mainFunction(self,startingAddr,totalRegisters,registerType):

        def animate():
            #xList.append(count)
            #yList.append(self.Pnow)

            ####    Live graph...............
            ####
            xList.append(int(datetime.today().second))

            
            #xList.append(int(self.Time.split(":")[0])*60+int(self.Time.split(":")[1])-420)
            yList.append(int(self.Pnow)/10000000)
            self.a.scatter(xList,yList)
            self.a.plot(xList,yList)
            self.fig.canvas.draw()


        #self.createMonthlyDataFile()
        #self.createYearlyDataFile()   

        ###############################################################         Main loop
        count=0
        xList=[]
        yList=[]
        while True:#count<20:
    
                dataArray=[]
                print " count = " + str(count) +"\n"
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
                animate()   
                #ani = animation.FuncAnimation(self.fig, animate, interval=1000)
                #root.mainloop()
                self.updateGUItasks()
                    

                
                #xList.append(i)#int(self.Time.split(":")[0])*60+int(self.Time.split(":")[0])-420)
                #yList.append(int(self.Pnow)/100000000)
                #yList.append(float(i)/10)
                #self.a.plot(xList, yList)
                count=count+1
                print yList
                print xList
                del(dataArray)
                #time.sleep(1)
        self.f.close()



startingAddr=0
totalRegisters=31
registerType=4

obj=mainWindow(instrument,root)
obj.pack()
obj.mainFunction(startingAddr,totalRegisters,registerType)
root.mainloop()





