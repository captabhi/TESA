#!usr/bin/env python
 
import minimalmodbus
import time
import serial
import pickle as fp


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

#logFile=open("logForModbus68.txt","w");
reg=40
startingAddr=0
totalRegisters=10
registerType=4

if instrument.debug == True:
	print instrument
i=0
while i<50:
        try:
                #dataReceived = instrument.read_register(reg,0,registerType)
                dataReceived = instrument.read_registers(statingAddr,totalRegisters,registerType)
                print (dataReceived)
                
                #fp.dump(test_reg,logFile)     
                #logFile.write(" ")
                #p.dump(time.time(),logFile)
                #time.sleep (0.05)

        except:
                print ("ERROR: Not responding ")
        i=i+1		 
#logFile.close();
