import sys

from PyQt5.QtWidgets import QLabel, QMainWindow, QApplication, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.rezultat = ""
        self.rezultat1 = 0
        self.button = QPushButton("=",self)
        self.button2 = QPushButton("Sterge", self)
        self.button0 = QPushButton("0",self)
        self.button1 = QPushButton("1",self)
        self.button3 = QPushButton("2",self)
        self.button4 = QPushButton("3", self)
        self.button5 = QPushButton("4", self)
        self.button6 = QPushButton("5", self)
        self.button7 = QPushButton("6", self)
        self.button8 = QPushButton("7", self)
        self.button9 = QPushButton("8", self)
        self.button10 = QPushButton("9", self)
        self.button11 = QPushButton("-",self)
        self.button12 = QPushButton("+", self)
        self.label = QLabel("Rezultatul", self)
        self.labelfinal = QLabel(" ",self)
        self.setGeometry(200,200,500,500)
        self.setWindowTitle("Calculator Digital")
        self.initUI()



    def initUI(self):
        width = 160
        height = 100
        x = ((self.width() - width ))
        y = ((self.height() - height))
        x1 = 0
        y2 = ((self.height() - height))
        self.button.setGeometry(x,y, width, height)
        self.button2.setGeometry(x1,y2,width, height)

        x0 = (self.width() - width) // 2
        y0 = (self.height() - height)
        self.button0.setGeometry(x0,y0,width,height)

        x11 = 0
        y11 = 65
        self.button1.setGeometry(x11,y11,width,height)

        x33 = (self.width() - width) // 2
        y33 = 65
        self.button3.setGeometry(x33,y33,width,height)

        x44 = self.width() - width
        y44 = 65
        self.button4.setGeometry(x44,y44,width,height)

        x55 = 0
        y55 = y11 + height + 10
        self.button5.setGeometry(x55,y55, width, height)

        x66 = (self.width() - width) // 2
        y66 = 65 + height + 10
        self.button6.setGeometry(x66,y66,width,height)

        x77 = self.width() - width
        y77 = 65 + height + 10
        self.button7.setGeometry(x77,y77,width,height)

        x88 = 0
        y88 = y55 + height + 10
        self.button8.setGeometry(x88,y88,width,height)

        x99 = (self.width() - width) // 2
        y99 = y77 + height + 10
        self.button9.setGeometry(x99,y99,width,height)

        x100 = self.width() - width
        y100 = y77 + height + 10
        self.button10.setGeometry(x100,y100,width,height)

        self.label.setGeometry(0,0, 100, 50)
        self.label.setStyleSheet("font-size: 20px;")

        width = 50
        height = 50
        x111 = self.width() - width
        y111 = 0
        self.button11.setGeometry(x111,y111,width,height)

        x122 = 400
        y122 = 0
        self.button12.setGeometry(x122,y122,width,height)
        self.button.clicked.connect(self.on_click)
        self.button0.clicked.connect(self.on_click0)
        self.button1.clicked.connect(self.on_click1)
        self.button2.clicked.connect(self.on_click2)
        self.button3.clicked.connect(self.on_click3)
        self.button4.clicked.connect(self.on_click4)
        self.button5.clicked.connect(self.on_click5)
        self.button6.clicked.connect(self.on_click6)
        self.button7.clicked.connect(self.on_click7)
        self.button8.clicked.connect(self.on_click8)
        self.button9.clicked.connect(self.on_click9)
        self.button10.clicked.connect(self.on_click10)
        self.button11.clicked.connect(self.on_click11)
        self.button12.clicked.connect(self.on_click12)

        self.labelfinal.setGeometry(200,0,80,50)









        

    def on_click(self):
        try:
            rezultat_final = eval(self.rezultat)
            self.labelfinal.setText(str(rezultat_final))
            self.rezultat1 = rezultat_final
        except Exception:
            self.labelfinal.setText("Eroare")
        self.display()
    def on_click0(self):
        self.rezultat += "0"
        self.labelfinal.setText(self.rezultat)
        self.display()
    def on_click1(self):
        self.rezultat += "1"
        self.labelfinal.setText(self.rezultat)
        self.display()
    def on_click2(self):
        self.rezultat = ""
        self.labelfinal.setText(self.rezultat)
    def on_click3(self):
        self.rezultat += "2"
        self.labelfinal.setText(self.rezultat)
        self.display()
    def on_click4(self):
        self.rezultat += "3"
        self.labelfinal.setText(self.rezultat)
        self.display()
    def on_click5(self):
        self.rezultat += "4"
        self.labelfinal.setText(self.rezultat)
        self.display()
    def on_click6(self):
        self.rezultat += "5"
        self.labelfinal.setText(self.rezultat)
        self.display()
    def on_click7(self):
        self.rezultat += "6"
        self.labelfinal.setText(self.rezultat)
        self.display()
    def on_click8(self):
        self.rezultat += "7"
        self.labelfinal.setText(self.rezultat)
        self.display()
    def on_click9(self):
        self.rezultat += "8"
        self.labelfinal.setText(self.rezultat)
        self.display()
    def on_click10(self):
        self.rezultat += "9"
        self.labelfinal.setText(self.rezultat)
        self.display()
    def on_click11(self):
        self.rezultat += "-"
        self.labelfinal.setText(self.rezultat)

    def on_click12(self):
        self.rezultat += "+"
        self.labelfinal.setText(self.rezultat)




    def display(self):

        print(f"{self.rezultat1}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())