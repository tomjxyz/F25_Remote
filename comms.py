import serial

class Comms:
    """The bulk of the Serial communcation happens in this class"""

    def __init__(self, port="/dev/ttyUSB0"):
        self.ser = serial.Serial(port, 9600)

    def sendMessage(self, data):
        self.ser.write(data)

    def close(self):
        self.ser.close()