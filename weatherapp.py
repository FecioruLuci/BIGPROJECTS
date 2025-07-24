import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

class Weatherapp(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,400,500)
        self.api = "baaa8a79c1275cacb8bd35ed67ae06bb"
        self.oras = QLabel("Scrie orasul",self)
        self.orasinput = QLineEdit(self)
        self.buton = QPushButton("Ia informatia",self)
        self.temp = QLabel(" ",self)
        self.emoji = QLabel("",self)
        self.desc = QLabel("",self)
        self.setWindowTitle("MyWeatherApp")
        self.requests = "baaa8a79c1275cacb8bd35ed67ae06bb"
        self.initUI()



    def initUI(self):
        vbox = QVBoxLayout()

        vbox.addWidget(self.oras, alignment=Qt.AlignCenter)
        vbox.addWidget(self.orasinput, alignment=Qt.AlignCenter)
        vbox.addWidget(self.buton)
        vbox.addWidget(self.temp, alignment=Qt.AlignCenter)
        vbox.addWidget(self.emoji, alignment=Qt.AlignCenter)
        vbox.addWidget(self.desc, alignment=Qt.AlignCenter)


        self.setLayout(vbox)

        self.oras.setObjectName("oras")
        self.orasinput.setObjectName("orasinput")
        self.buton.setObjectName("butonul")
        self.temp.setObjectName("temperatura")
        self.emoji.setObjectName("emoji")
        self.desc.setObjectName("descriere")
        self.setStyleSheet("""
#butonul{
                           color:hsl(200, 100%, 100%);
                           background-color: hsl(208, 2%, 25%);
                           font-family: Arial;
                           font-size: 20px;
                           font-weight: bold;}
QWidget{
                           background-color: hsl(208, 100%, 66%)}
#oras{
                           font-size: 30px;
                           font-family: calibri; }
#orasinput{
                            font-size: 25px;}
#temperatura{
                            font-size: 80px;
                            font-family: Arial;}
#emoji{
                            font-size: 75px;
                            font-family: "Segoe UI Emoji";}
#descriere{
                            font-size: 45px;
                            font-weight: bold;}""")
        self.buton.clicked.connect(self.weath)


    def weath(self):
        self.url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=baaa8a79c1275cacb8bd35ed67ae06bb&units=metric'.format(self.orasinput.text())
        self.res = requests.get(self.url)
        if self.res.status_code == 200:
            self.data = self.res.json()
            self.status()
        else:
            self.temp.setText(f"Oras inexistent")
            self.desc.setText(f"")
            self.emoji.setText(f"")

    def status(self):
        humidity = self.data['main']['humidity']
        pressure = self.data['main']['pressure']
        wind = self.data['wind']['speed']
        description = self.data['weather'][0]['description']
        temperature = self.data['main']['temp']
        print('Temperature:', f'{temperature}°C')
        print('Wind:',wind)
        print('Pressure: ',pressure)
        print('Humidity: ',humidity)
        print('Description:',description)
        self.temp.setText(f"{int(temperature)}℃")
        if description == "scattered clouds":
            self.desc.setText(f"Nori imprastiati")
            self.emoji.setText(f"🌥️")
        elif description == "few clouds":
            self.desc.setText(f"Cativa nori")
            self.emoji.setText(f"🌤️")
        elif description == "clear sky":
            self.desc.setText(f"Senin")
            self.emoji.setText(f"☀️")
        elif description == "broken clouds":
            self.desc.setText(f"Innorat")
            self.emoji.setText(f"☁️")
        elif description == "overcast clouds":
            self.desc.setText(f"Ploua")
            self.emoji.setText(f"🌧")
        elif description == "thunderstorm":
            self.desc.setText(f"Tunete")
            self.emoji.setText(f"🌩")
        elif description == "snow":
            self.desc.setText(f"Ninge")
            self.emoji.setText(f"🌨️")





if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = Weatherapp()
    weather_app.show()
    sys.exit(app.exec_())

