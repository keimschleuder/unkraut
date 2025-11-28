import argparse
import gpiod
import rpi_drivers.motor
import rpi_drivers.plantnet

# Console Arguments init
parser = argparse.ArgumentParser(prog = "main.py", 
                                 usage = "python main.py [-h]", 
                                 description = "Intended to run on a Raspberry Pi 5 with AI-HAT and AI-Camera. It detects harmful plants and destroys them.", 
                                 epilog = "Program written for the 'Jugend Forscht'-Competition by Niklas Keim", 
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)

# GPIO init
chip = gpiod.Chip('gpiochip4')

motor_drv = rpi_drivers.motor.Motor()

plantnet_drv = rpi_drivers.plantnet.PlantNet()
