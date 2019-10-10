#include <SoftwareSerial.h>

/**
 *  Modbus slave example 3:
 *  The purpose of this example is to link a data array
 *  from the Arduino to an external device through RS485.
 *
 *  Recommended Modbus Master: QModbus
 *  http://qmodbus.sourceforge.net/
 */

#include <ModbusRtu.h>

#define DATA_SIZE 16
#define SLAVE_ADDRESS 13 
#define Serial_PORT 0
#define BAUD_RATE 19200
// assign the Arduino pin that must be connected to RE-DE RS485 transceiver
#define TXEN 4 

// data array for modbus network sharing
/*
uint16_t voltageACdata[DATA_SIZE] = {
  3, 1415, 9265, 4, 2, 7182, 28182, 8, 0, 0, 0, 0, 0, 0, 1, -1 };

uint16_t voltagePVdata[DATA_SIZE] = {
  23, 5415, 1455, 45, 5, 2745, 582, 53, 44, 34, 92, 642, 36, 38, 98, 94 };

uint16_t currentACdata[DATA_SIZE] = {
  83, 442, 96, 62, 5, 534, 252, 42, 56, 97 ,54, 84, 5496, 6112, 9, 149 };

uint16_t currentPVdata[DATA_SIZE] = {
  494, 6567, 5267, 542, 9724, 5292, 3087, 9493, 29, 1267, 8465, 128, 648, 13, 71, -113 };
*/
uint16_t wholeData[DATA_SIZE*4];
/*
void initializeWholeDataPacket()
{
  for(int i=0;i<DATA_SIZE*4;i=i+4)
  {
    //Serial.print("i= ");
    //Serial.println(i);
    wholeData[i+((i/4)%4)]=voltageACdata[i/4];
    //Serial.print(i+((i/4)%4));
    //Serial.print("  ");
    //Serial.println(wholeData[i+((i/4)%4)]);
    
    wholeData[i+((i/4+1)%4)]=voltagePVdata[i/4];
    //Serial.print(i+((i/4+1)%4));
    //Serial.print("  ");
    //Serial.println(wholeData[i+((i/4+1)%4)]);
    
    wholeData[i+((i/4+2)%4)]=currentACdata[i/4];
    //Serial.print(i+((i/4+2)%4));
    //Serial.print("  ");
    //Serial.println(wholeData[i+((i/4+2)%4)]);
    
    wholeData[i+((i/4+3)%4)]=currentPVdata[i/4];
    //Serial.print(i+((i/4+3)%4));
    //Serial.print("  ");
    //Serial.println(wholeData[i+((i/4+3)%4)]);
    
  }

}
*/

void printWholeData()
{
  for(int i=0;i<DATA_SIZE*2;i++)
  {
    Serial.print(i);
    Serial.print("  ");
    Serial.println(wholeData[i]);
    Serial.print(" ");
  }

}


void randomizeData()
{
  for(int i=0;i<DATA_SIZE*2;i++)
  {
    wholeData[i]=random(0,65535);
  }



}
/**
 *  Modbus object declaration
 *  u8id : node id = 0 for master, = 1..247 for slave
 *  u8serno : //Serial port (use 0 for //Serial)
 *  u8txenpin : 0 for RS-232 and USB-FTDI 
 *               or any pin number > 1 for RS-485
 */
Modbus slave(SLAVE_ADDRESS,Serial_PORT,TXEN); // this is slave @1 and RS-485

void setup() {
  ////Serial.flush();
  //Serial.begin(9600);
  //initializeWholeDataPacket();
  //for(int i=0;i<DATA_SIZE*4;i++)
  //wholeData[i]=i;
  //printWholeData();
  ////Serial.print("HELLO");
  //delay(2000);
  randomSeed(analogRead(0));
  slave.begin( BAUD_RATE ); // baud-rate at 19200

}

void loop() {
  
  randomizeData();
  //printWholeData();

  slave.poll( wholeData, DATA_SIZE *2);
 
}
