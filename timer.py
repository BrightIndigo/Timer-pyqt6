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
        self.clear_button.clicked.connect(self.clear_clicked)

        self.save_btn = QPushButton("Save")
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

    def format_time(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def save_clicked(self):
        now = datetime.datetime.now()
        try:
            with open("times.csv", 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([self.format_time(), now.strftime("%d-%m-%Y, %H:%M:%S")])
            self.save_label.setText("Saved successfully!")
        except Exception as e:
            self.save_label.setText(f"Error: {e}")

    def timer_start(self):
        self.seconds += 1
        if self.seconds == 60:
            self.minutes += 1
            self.seconds = 0
        if self.minutes == 60:
            self.hours += 1
            self.minutes = 0

        self.label.setText(self.format_time())

    def clear_clicked(self):
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        self.label.setText(self.format_time())

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
