from smbus import SMBus
import time

class Motor:
    def __init__(self, address=0x2f):
        self.addr = address # bus address
        self.bus = SMBus(1) # indicates /dev/ic2-1

    def drive(self, output: bool):
        if output:
            self.bus.write_byte(self.addr, 0x1) # Switch on
        else:
            self.bus.write_byte(self.addr, 0x0) # Switch off

    def halt(self):
        self.drive(False)

    def drive_for(self, output:bool, duration_sec: int):
        self.drive(output)
        end_time = time.time() + duration_sec
        while time.time() < end_time:
            pass
        self.halt()