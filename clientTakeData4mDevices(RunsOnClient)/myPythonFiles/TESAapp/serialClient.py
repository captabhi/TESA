import pymodbus
import serial
from pymodbus.pdu import ModbusRequest
from pymodbus.client.sync import ModbusSerialClient as ModbusClient #initialize a serial RTU client instance
from pymodbus.transaction import ModbusRtuFramer

import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

#count= the number of registers to read
#unit= the slave unit this request is targeting
#address= the starting address to read from

client= ModbusClient(method = "rtu", port="/dev/ttyACM0",stopbits = 1, bytesize = 8, parity = 'N' ,baudrate= 19200)

#Connect to the serial modbus server
connection = client.connect()
print (connection)
while 1:
#Starting add, num of reg to read, slave unit.
        result= client.read_holding_registers(0x00,2,unit= 0x0a)
        if result :
                    print result.registers
        


#Closes the underlying socket connection
client.close()

