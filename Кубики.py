import random
import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QListWidget, QMainWindow, QLabel, QVBoxLayout, QGridLayout, QWidget, \
    QLineEdit, QPushButton, QMessageBox


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.centralwidget = QWidget(self)

        self.bat = QPushButton(self)
        self.bat2 = QPushButton(self)
        self.bat2.move(0, 380)

        self.pro = QLineEdit(self)
        self.pro.setText("0")
        self.pro.move(0, 400)
        self.bat2.setText("Расчитать 1 ")
        self.bat.setText("Расчитать")

        self.rull = QLineEdit(self)
        self.rull.setText("2")
        self.rull.move(0, 40)
        self.rull.adjustSize()
        self.coll = QLineEdit(self)
        self.coll.setText("1")
        self.coll.move(0, 60)
        self.coll.adjustSize()
        self.rez = QListWidget(self)
        self.rez.addItems(["Результат:"])
        self.rez.move(0, 80)
        self.bat2.clicked.connect(self.prower)
        self.bat.clicked.connect(self.prow)
        self.rez.adjustSize()

    def prow(self):
        self.rez.clear()
        self.rez.addItems(["Результат:"])
        self.rulls = int(self.rull.text())
        self.colls = int(self.coll.text())
        print(self.rulls, self.colls)
        self.spis = []
        for i in range(self.rulls):
            sum = 0

            for i in range(self.colls):
                x = random.randint(1, 6)
                sum += x
            self.spis.append(sum)
        chis = 0
        Otv = ""
        for n in range(6 * (self.colls)):
            chis += 1
            a = self.spis.count(chis)
            print(chis, '=', float((a / self.rulls) * 100), '%')
            Otv = str(chis) + '=' + str(float((a / len(self.spis)) * 100)) + '%'
            self.rez.addItem(str(Otv))

    def prower(self):
        self.rez.clear()
        self.rez.addItems(["Результат:"])
        a = self.spis.count(int(self.pro.text()))
        print(len(self.spis))
        kol = str(self.pro.text()) + '=' + str(float((a / len(self.spis)) * 100)) + '%'
        self.rez.addItem(str(kol))


def applic():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    applic()