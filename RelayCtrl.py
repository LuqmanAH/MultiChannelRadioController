import serial
import serial.tools.list_ports
from time import sleep

def onRelay():
    portList = list(serial.tools.list_ports.comports())

    for port in portList:
        if "USB-SERIAL CH340" in port.description:
            COM = str(port[0])

    ard = serial.Serial(COM, 9600)

    for i in range(5):
        command = str("ON")
        sleep(1)
        ard.write(command.encode('utf-8'))
    
def offRelay():

    portList = list(serial.tools.list_ports.comports())
    
    for port in portList:
        if "USB-SERIAL CH340" in port.description:
            COM = str(port[0])

    ard = serial.Serial(COM, 9600)
    
    for i in range(5):
        command = str("OFF")
        sleep(1)
        ard.write(command.encode('utf-8'))

def setSerial():
    portlist = list(serial.tools.list_ports.comports())

    for port in portlist:
        if "USB-SERIAL CH340" in port.description:
            COM = str(port[0])
    while True:
        ard = serial.Serial(COM, 9600)