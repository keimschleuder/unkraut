from smbus import SMBus

class Motor:
    def __init__(self, address=0x2f):
        self.addr = address # bus address
        self.bus = SMBus(1) # indicates /dev/ic2-1

    def drive(self, output: bool):
        if output:
            self.bus.write_byte(self.addr, 0x1) # Switch on
        else:
            self.bus.write_byte(self.addr, 0x0) # Switch off