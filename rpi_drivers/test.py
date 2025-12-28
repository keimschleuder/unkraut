import rpi_drivers.arduino as arduino
import plantnet
import gpio
import servo
from time import sleep

# TODO: Write a test for all modules used in the main Programm

arduino_drv = arduino.Arduino()

arduino_drv.motor(True)
sleep(1)
arduino_drv.pump(True)
sleep(1)
arduino_drv.motor(False)
sleep(1)
arduino_drv.motor(True)
sleep(1)
arduino_drv.pump(False)
sleep(1)
arduino_drv.pump(True)
sleep(1)
arduino_drv.halt()