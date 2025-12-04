import time

import board
from adafruit_motor import servo

from adafruit_pca9685 import PCA9685

i2c = board.I2C()  # uses board.SCL and board.SDA

# Create a simple PCA9685 class instance.
pca = PCA9685(i2c)
# You can optionally provide a finer tuned reference clock speed to improve the accuracy of the
# timing pulses. This calibration will be specific to each board and its environment. See the
# calibration.py example in the PCA9685 driver.
# pca = PCA9685(i2c, reference_clock_speed=25630710)
pca.frequency = 50

class ServoChannel():
    def __init__(self, channel: int):
        self.servo = servo.Servo(pca.channels[channel])

    def set_angle(self, angle: int):
        self.servo.angle = angle

    def set_fraction(self, fraction: float):
        self.servo.fraction = fraction

    def terminate(self):
        pca.deinit()