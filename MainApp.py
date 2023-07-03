# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Luqman Al Helmy
# Created Date: 10/09/22
# version ='1.0'
# ---------------------------------------------------------------------------
""" PyQt5 based GUI for interfacing with Handy-Transceiver through UART communication with Arduino NANO and transmitting ToneInvoke Module DTMF tones. """ 
# ---------------------------------------------------------------------------
#

import sys
import ToneInvoke
import serial.tools.list_ports

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtSerialPort
from time import sleep

from Main_Window_v0_2 import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    # init_GUI_import from Main_window2.py
    # autoSet serial port for CH340 Arduino NANO.
    def __init__(self) :
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.timerScreen = QTimer()
        self.timerScreen.setInterval(2000)
        self.timerScreen.setSingleShot(True)
        self.timerScreen.timeout.connect(self.handleDTMF)

        self.timerScreen2 = QTimer()
        self.timerScreen2.setInterval(2000)
        self.timerScreen2.setSingleShot(True)
        self.timerScreen2.timeout.connect(self.OffPTT)

        self.PB_transmit.setEnabled(True)
        self.PB_transmit.clicked.connect(self.OnPTT)
        self.PB_transmit.clicked.connect(self.timerScreen.start)
        self.PB_transmit.clicked.connect(self.timerScreen2.start)

        global COM
        for port in list(serial.tools.list_ports.comports()):
            if "Arduino Uno" in port.description:
                COM = str(port[0])

        try:
            self.serial = QtSerialPort.QSerialPort(
                COM,
                baudRate=QtSerialPort.QSerialPort.  Baud9600    
            )
            self.PB_transmit.setEnabled(True)

            if not self.serial.isOpen():
                if not self.serial.open(QIODevice.ReadWrite):
                    self.serial.open(QIODevice.ReadWrite)
        except NameError: 
            self.StatDisplay.setText("serial tidak ditemukan")
            self.StatDisplay.setStyleSheet("color: red")
            self.PB_transmit.setEnabled(False)

    def OnPTT(self):
        OnPayload = "ON"
        self.serial.write(OnPayload.encode())

    def OffPTT(self):
        OffPayload = "OFF"
        self.serial.write(OffPayload.encode())

    def handleDTMF(self):
        xstring = str(self.line_toneInput.text())
        ToneInvoke.InvokeStr(xstring)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())