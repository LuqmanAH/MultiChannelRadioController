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

from Main_Window_2 import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
    # init_GUI_import from Main_window2.py
    # autoSet serial port for CH340 Arduino NANO.
    def __init__(self, parent=None) :
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.serOpen.clicked.connect(self.findSerial)
        self.ui.PTTOn.clicked.connect(self.OnPTT)
        self.ui.PTT_Stop.clicked.connect(self.OffPTT)
        self.ui.PB_transmit.clicked.connect(self.handleDTMF)

        global COM
        for port in list(serial.tools.list_ports.comports()):
            # Please write the proper serial device if not using arduino NANO 
            # Please write the proper baudrate if not using 9600 baud
            if "USB-SERIAL CH340" in port.description:
                COM = str(port[0])
        try:
            self.serial = QtSerialPort.QSerialPort(
                COM,
                baudRate=QtSerialPort.QSerialPort.Baud9600
            )
        except NameError:
            self.serExceptHandler()

    def findSerial(self):
        if self.ui.serOpen.isChecked():
            self.ui.serOpen.setText("Tutup Serial")
            self.ui.StatDisplay.setText("Koneksi Serial di " + COM)
            self.ui.PTTOn.setEnabled(True)
            self.ui.PTT_Stop.setEnabled(True)
            self.ui.PB_transmit.setEnabled(True)
            if not self.serial.isOpen():
                if not self.serial.open(QIODevice.ReadWrite):
                    self.ui.serOpen.setChecked(False)
        else:
            self.ui.PTTOn.setEnabled(False)
            self.ui.PTT_Stop.setEnabled(False)
            self.ui.PB_transmit.setEnabled(False)
            self.ui.serOpen.setText("Buka Serial")
            self.ui.StatDisplay.setText("Stand By")
            self.serial.close()
    
    def OnPTT(self):
        OnPyaload = "ON"
        self.serial.write(OnPyaload.encode())

    def OffPTT(self):
        OffPyaload = "OFF"
        self.serial.write(OffPyaload.encode())

    def handleDTMF(self):
        xstring = str(self.ui.line_toneInput.text())

        ToneInvoke.InvokeStr(xstring)

    def serExceptHandler(self):
        self.ui.StatDisplay.setStyleSheet("background-color: red")
        self.ui.StatDisplay.setText("Serial Tidak Ditemukan")

if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())