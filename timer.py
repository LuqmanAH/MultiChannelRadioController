import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.time_label = QLabel(self)
        self.time_label.setText("Start")
        self.time_label.move(50, 50)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.change_text)
        self.timer.start(1000)

        self.show()

    def change_text(self):
        text = self.time_label.text()
        if text == "Start":
            self.time_label.setText("Stop")
        else:
            self.time_label.setText("Start")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
