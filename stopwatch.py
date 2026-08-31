import sys

from PyQt5.QtCore import QTime, QTimer, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout


class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stopwatch")
        self.setWindowIcon(QIcon("clock.png"))
        self.setGeometry(600, 400, 300, 100)
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00.00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.init_ui()

    def init_ui(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        vbox.addLayout(hbox)
        self.setStyleSheet("""
            QPushButton, QLabel {
                padding: 20px;
                font-weight: bold;
            }
            QPushButton{
                font-family: Inter;
                font-size: 35px;
            }
            QLabel {
                font-size: 120px;
                background-color: hsl(200, 100%, 85%);
                font-family: Digital-7 Mono;
                border-radius: 20px;
            }
        """)
        self.start_button.clicked.connect(self.startTime)
        self.stop_button.clicked.connect(self.stopTimer)
        self.reset_button.clicked.connect(self.resetTimer)
        self.timer.timeout.connect(self.updateDisplay)

    def startTime(self):
        self.timer.start(10)

    def stopTimer(self):
        self.timer.stop()

    def resetTimer(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.formatTime(self.time))

    def formatTime(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    def updateDisplay(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.formatTime(self.time))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = Stopwatch()
    clock.show()
    sys.exit(app.exec_())
