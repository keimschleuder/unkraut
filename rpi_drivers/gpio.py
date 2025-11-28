import gpiod

chip = gpiod.Chip('gpiochip4')

class GPIO_PIN:
    def __init__(self, pin: int, output: bool, consumer: str):
        self.line = chip.get_line(pin)
        if output:
            self.line.request(consumer=consumer, type=gpiod.LINE_REQ_DIR_OUT)
        else:
            self.line.request(consumer=consumer, type=gpiod.LINE_REQ_DIR_IN)

class GPIO_IN_PIN(GPIO_PIN):
    def __init__(self, pin, consumer = "GPIO Input Pin"):
        super().__init__(pin, False, consumer)

    def get_input(self):
        return self.line.get_value()

class GPIO_OUT_PIN(GPIO_PIN):
    def __init__(self, pin, consumer = "GPIO Output Pin"):
        super().__init__(pin, True, consumer)

    def set_output(self, value):
        return self.line.set_value(value)