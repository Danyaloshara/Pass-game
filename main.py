from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
import random

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Generation_password.clicked.connect(self.example)
    def example(self):
        sings = ''
        if self.ui.use_bukvi.isChecked():
            sings = 'wertyuiopasdfghjklzxcvbnm'
        if self.ui.Use_Cifri.isChecked():
            sings += '1234567890'

        result = ''
        number = random.randint(8, 16)
        for i in range(number):
            result += random.choice(sings)
        self.ui.result.setText(result)

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
