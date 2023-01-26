from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from kisisel_sayfa4_python import Ui_MainWindow12
import sqlite3
import time

class Ui_MainWindow22(object):
    def baglanti_yap(self):
        baglanti = sqlite3.connect("kayitlar2.db")
        self.cursor = baglanti.cursor()
        self.cursor.execute("CREATE TABLE If not exists ogrenci (kuladi TEXT,sifre TEXT)")
        baglanti.commit()

    def onay(self):
        adi = self.lineEdit.text()
        par = self.lineEdit_2.text()

        self.cursor.execute("SELECT*FROM ogrenci where kuladi=? and sifre=?", (adi, par))

        data = self.cursor.fetchall()

        if len(data) == 0:
            self.label_4.setText("Böyle bir kullanıcı yok\n Tekrar deneyin")
        else:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow12()
            self.ui.setupUi(self.window)
            self.window.show()

    def gizli(self):
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

    def setupUi(self, MainWindow):
        self.baglanti_yap()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 545)
        MainWindow.setMaximumSize(QtCore.QSize(950, 545))
        MainWindow.setMaximumSize(QtCore.QSize(950, 545))
        MainWindow.setStyleSheet("background-color: rgb(56, 103, 190);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 380, 121, 41))
        self.pushButton.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.onay)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 130, 161, 91))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 260, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 1041, 71))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(380, 210, 141, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(218, 218, 218);;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(380, 300, 141, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.lineEdit_2.setObjectName("lineEdit_2")

        #self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(390, 350, 121, 20))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 310, 16, 16))
        self.pushButton_2.setStyleSheet("background-color: rgb(159, 159, 159);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.gizli)

        self.lineEdit_2.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.lineEdit.raise_()
        self.label_4.raise_()
        self.pushButton_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ÖĞRENCİ GİRİŞİ"))
        self.pushButton.setText(_translate("MainWindow", "Giriş Yap"))
        self.label.setText(_translate("MainWindow", "Kullanıcı adı :"))
        self.label_2.setText(_translate("MainWindow", "Şİfre"))
        self.label_3.setText(_translate("MainWindow", "                                                       ÖĞRENCİ BİLGİ SİSTEMİ"))
        self.pushButton_2.setText(_translate("MainWindow", "G"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow22()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
