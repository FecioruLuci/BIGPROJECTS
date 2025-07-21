import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer
import datetime

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,700,400)
        self.setWindowTitle("MyClockwatch")
        self.buton1 = QPushButton("START",self)
        self.buton2 = QPushButton("STOP",self)
        self.buton3 = QPushButton("RESET",self)
        self.buton1.clicked.connect(self.startul)
        self.buton2.clicked.connect(self.stopul)
        self.buton3.clicked.connect(self.resetul)
        self.label1 = QLabel("00:00")
        self.acuma = QTimer()
        self.acuma.timeout.connect(self.update_timer)
        self.secunde = 0
        self.minute = 0



        self.initUI()



    def initUI(self):
        widgetul = QWidget()
        self.setCentralWidget(widgetul)
        vbox = QVBoxLayout()
        vbox.addWidget(self.label1, alignment=Qt.AlignHCenter)
        vbox.addStretch()
        widgetul.setLayout(vbox)
        self.label1.setStyleSheet("font-size: 40px;" \
        "font-family: Arial;")
        self.buton1.setGeometry(10, 250, 150,100)
        self.buton2.setGeometry(270,250,150,100)
        self.buton3.setGeometry(540,250,150,100)
        self.buton1.raise_()
        self.buton2.raise_()
        self.buton3.raise_()
        self.buton1.setStyleSheet("""
QPushButton{
                                  background-color: hsl(136, 72%, 37%);}
QPushButton:hover{
                                  background-color: hsl(136, 83%, 58%);}""")
        self.buton2.setStyleSheet("""
QPushButton{
                                  background-color: hsl(0, 96%, 26%)}
QPushButton:hover{
                                  background-color: hsl(0, 87%, 48%)}""")
        self.buton3.setStyleSheet("""
QPushButton{
                                  background-color: hsl(52, 94%, 33%)}
QPushButton:hover{
                                  background-color: hsl(52, 96%, 49%)}""")
        self.setStyleSheet("background-color: hsl(0, 0%, 44%);")

        

    def startul(self):
        self.acuma.start(1000)

    def stopul(self):
        self.acuma.stop()

    def resetul(self):
        self.acuma.stop()
        self.minute = 0
        self.secunde = 0
        self.label1.setText("00:00")
    def update_timer(self):
        self.secunde += 1
        if self.secunde == 60:
            self.minute += 1
            self.secunde = 0
        self.label1.setText(f"{self.minute:02d}:{self.secunde:02d}")

"""    def timerul(self):
        acu = datetime.datetime.now().strftime("%M:%S")
        minute = int(datetime.datetime.now().strftime("%M"))
        minute = 0
        secunde = int(datetime.datetime.now().strftime("%S"))
        secunde = 0
        if secunde == 60:
            minute += 1
            secunde = 0
"""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())