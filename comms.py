import serial

class Comms:
    """The bulk of the Serial communcation happens in this class"""

    def __init__(self, port="/dev/ttUSB0"):
        self.ser = serial.Serial(port, 9600)

    def close(self):
        self.ser.close()