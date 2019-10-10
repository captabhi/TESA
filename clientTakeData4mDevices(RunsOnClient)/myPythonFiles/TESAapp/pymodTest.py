from pymodbus3.client.sync import ModbusSerialClient
client = ModbusSerialClient('/dev/ttyACM0')
client.write_coil(1, True)
result = client.read_coils(1,1)
print (result.bits[0])
client.close()
