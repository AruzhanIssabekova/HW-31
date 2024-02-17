import sys
import os
import requests
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QWidget
class MainWindow(QMainWindow):
    def send_request(self):
        url = self.url_input.text()
        r = requests.get(url)
        if r.status_code == 200:
            self.result_text.setText(r.text)
            self.save_response(r.text)
        else:
            self.result_text.setText("Error")

    def save_response(self, text):
        folder = "papka"
        if not os.path.exists(folder):
            os.makedirs(folder)
        with open(os.path.join(folder, "papka.txt"), "w") as file:
            file.write(text)

    def __init__(self):
        super().__init__()
        self.url_l = QLabel("URL:", self)
        self.url_l.move(50, 50)

        self.url_v = QLineEdit(self)
        self.url_v.setGeometry(100, 50, 250, 50)

        self.send_b = QPushButton("Отправить", self)
        self.send_b.setGeometry(280, 50, 100, 50)
        self.send_b.clicked.connect(self.send_request)

        self.result_l = QLabel("Результат:", self)
        self.result_l.move(50, 100)

        self.result_t = QTextEdit(self)
        self.result_t.setGeometry(20, 100, 360, 150)



app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())


