
import serial
import time

# make connection with the car via serial usb port. 
# send appropriate commands to the arduino board
class Car():

    # connect to the car via below serial port 
    def __init__(self):
        self.ser = serial.Serial('/dev/cu.usbmodem1411', 9600)
        time.sleep(2)
        print("Established connection with Car")

    def stop(self):
        self.send("S")
        
    def forward(self):
        self.send("F")
        
    def back(self):
        self.send("B")
        
    def left(self):
        self.send("L")
        
    def right(self):
        self.send("R")
        
    def send(self, command):
        self.ser.write(command.encode())
        

