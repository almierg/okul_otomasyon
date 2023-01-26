from PyQt5 import QtCore, QtGui, QtWidgets
from personel_sayfasi2_python import Ui_MainWindow5
import sqlite3

class Ui_MainWindow3(object):

    def baglanti_yap(self):
        baglanti = sqlite3.connect("kayitlar2.db")
        self.cursor = baglanti.cursor()
        self.cursor.execute("CREATE TABLE If not exists personel (kuladi TEXT,sifre TEXT)")
        baglanti.commit()

    def onay2(self):
            adi = self.lineEdit.text()
            par = self.lineEdit_2.text()

            self.cursor.execute("SELECT*FROM personel where kuladi=? and sifre=?", (adi, par))

            data = self.cursor.fetchall()

            if len(data) == 0:
                self.label_4.setText("Böyle bir kullanıcı yok\n Tekrar deneyin")
            else:
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_MainWindow5()
                self.ui.setupUi(self.window)
                self.window.show()


    def otomatik(self):
        pass


    def gizli2(self):
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

    def setupUi(self, MainWindow):
        self.baglanti_yap()


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 545)
        MainWindow.setMaximumSize(QtCore.QSize(950, 545))
        MainWindow.setStyleSheet("background-color: rgb(56, 103, 190);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 951, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 150, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(390, 260, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(390, 320, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(56, 103, 190);")
        self.label_4.setObjectName("label_4")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(380, 200, 131, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(380, 290, 131, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.lineEdit_2.setObjectName("lineEdit_2")


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 360, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.onay2)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 300, 16, 16))
        self.pushButton_2.setStyleSheet("background-color: rgb(159, 159, 159);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.gizli2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PERSONEL GİRİŞİ"))
        self.label.setText(_translate("MainWindow", "                                                                    PERSONEL GİRİŞİ"))
        self.label_2.setText(_translate("MainWindow", "Kullanıcı adı :"))
        self.label_3.setText(_translate("MainWindow", "Şifre :"))
        self.pushButton.setText(_translate("MainWindow", "Giriş Yap"))
        self.label_4.setText(_translate("MainWindow", ""))
        self.pushButton_2.setText(_translate("MainWindow", "G"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow3()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
