import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout
from PyQt6.QtCore import QSize, Qt, QTimer
import time

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Timer")
        self.setFixedSize(QSize(400, 300))
        layout = QVBoxLayout()
        start_button = QPushButton("Start timer!")
        start_button.setCheckable(True)
        start_button.clicked.connect(self.button_clicked)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)
        widgets = [start_button]

        for widget in widgets:
            layout.addWidget(widget)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def button_clicked(self, started):
        self.started = started
        print("Started?", self.started)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()