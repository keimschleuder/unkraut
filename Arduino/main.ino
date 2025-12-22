#include <Wire.h>
 
#define MOTOR_PIN 2
 
byte RxByte;
bool value;
 
void I2C_RxHandler(int numBytes)
{
  while(Wire.available()) {  // Read Any Received Data
    RxByte = Wire.read();
  }
}
 
void setup() {
  pinMode(MOTOR_PIN, OUTPUT);
  Wire.begin(0x2f);
  Wire.onReceive(I2C_RxHandler);
}
 
void loop() {
  digitalWrite(MOTOR_PIN, RxByte);
  delay(100);
}
