import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QMainWindow, QPushButton, QVBoxLayout
from PyQt6.QtCore import QSize, Qt, QTimer
import datetime
import csv

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Timer")
        self.setFixedSize(QSize(400, 300))
        layout = QVBoxLayout()
        self.start_button = QPushButton("Start timer!")
        self.start_button.setCheckable(True)
        self.start_button.clicked.connect(self.button_clicked)
        self.clear_button = QPushButton("Clear")
        self.clear_button.setCheckable(True)
        self.clear_button.clicked.connect(self.clear_clicked)
        self.save_btn = QPushButton("Save")
        self.save_btn.setCheckable(True)
        self.save_btn.clicked.connect(self.save_clicked)
        self.label = QLabel('Timer not started')
        self.save_label = QLabel('')
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        
        widgets = [self.start_button, self.label, self.save_btn, self.save_label, self.clear_button]

        for widget in widgets:
            layout.addWidget(widget)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_start)

    def button_clicked(self, started):
        if started:
            self.label.setText('Timer started')
            self.timer.start(1000)
            self.start_button.setText("Stop timer!")
        else:
            self.timer.stop()
            self.start_button.setText("Start timer!")

    def save_clicked(self):
        seconds = "00"
        minutes = "00"
        hours = "00"

        if self.seconds < 10:
            seconds = "0"+str(self.seconds)
        else:
            seconds = str(self.seconds)
        if self.minutes < 10:
            minutes = "0"+str(self.minutes)
        else:
            minutes = str(self.minutes)
        if self.hours < 10:
            hours = "0"+str(self.hours) 
        else:
            hours = str(self.hours)
        
        now = datetime.datetime.now()
        
        with open("times.csv", 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([hours, minutes, seconds, now.strftime("%d-%m-%Y, %H:%M:%S")])

    def timer_start(self):
        self.seconds += 1
        if self.seconds == 60:
            self.minutes += 1
            self.seconds = 0
        if self.minutes == 60:
            self.hours += 1
            self.minutes = 0

        seconds = "00"
        minutes = "00"
        hours = "00"

        if self.seconds < 10:
            seconds = "0"+str(self.seconds)
        else:
            seconds = str(self.seconds)
        if self.minutes < 10:
            minutes = "0"+str(self.minutes)
        else:
            minutes = str(self.minutes)
        if self.hours < 10:
            hours = "0"+str(self.hours) 
        else:
            hours = str(self.hours)

        self.label.setText(f'{hours}:{minutes}:{seconds}')

    def clear_clicked(self):
        self.seconds = 0
        self.minutes = 0
        self.hours = 0

        hours = "00"
        minutes = "00"
        seconds = "00"

        self.label.setText(f'{hours}:{minutes}:{seconds}')

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()