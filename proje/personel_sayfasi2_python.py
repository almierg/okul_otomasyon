from PyQt5 import QtCore, QtGui, QtWidgets
from anket_python import Ui_MainWindow10
from p_duyuru2_python import Ui_MainWindow11
from p_anket_python import Ui_MainWindow12
from p_profil_python import Ui_MainWindow15
from PyQt5.QtWidgets import qApp
from sinav3 import Ui_MainWindow23
from nakil2 import Ui_MainWindow28
from p_program import Ui_MainWindow24



class Ui_MainWindow5(object):
    def program(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow24()
        self.ui.setupUi(self.window)
        self.window.show()

    def nakil2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow28()
        self.ui.setupUi(self.window)
        self.window.show()

    def sinav(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow23()
        self.ui.setupUi(self.window)
        self.window.show()

    def cikis2(self):
        qApp.quit()

    def profil2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow15()
        self.ui.setupUi(self.window)
        self.window.show()

    def duyuru2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow11()
        self.ui.setupUi(self.window)
        self.window.show()

    def anket(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow10()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1328, 795)
        MainWindow.setMaximumSize(QtCore.QSize(1367, 858))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 420, 211, 111))
        self.pushButton_5.setStyleSheet("background-color: rgb(56, 103, 190);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.program)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 200, 211, 111))
        self.pushButton_2.setStyleSheet("background-color: rgb(56, 103, 190);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.anket)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1371, 91))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 310, 211, 111))
        self.pushButton_3.setStyleSheet("background-color: rgb(56, 103, 190);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.sinav)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 90, 211, 111))
        self.pushButton.setStyleSheet("background-color: rgb(56, 103, 190);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.duyuru2)

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 530, 211, 111))
        self.pushButton_6.setStyleSheet("background-color: rgb(56, 103, 190);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.nakil2)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1170, 20, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1130, 50, 71, 21))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.profil2)

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(1220, 50, 81, 21))
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.cikis2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PERSONEL BİLGİ SİSTEMİ"))
        self.pushButton_5.setText(_translate("MainWindow", "DERS PROGRAMI"))
        self.pushButton_2.setText(_translate("MainWindow", "ANKETLER"))
        self.label.setText(_translate("MainWindow", "             AKIL OKULLARI "))
        self.pushButton_3.setText(_translate("MainWindow", "SINAV TARİHLERİ"))
        self.pushButton.setText(_translate("MainWindow", "DUYURULAR"))
        self.pushButton_6.setText(_translate("MainWindow", "NAKİL İŞLEMLERİ"))
        self.label_2.setText(_translate("MainWindow", " Hilal YILMAZ"))
        self.pushButton_4.setText(_translate("MainWindow", "SAYFAM"))
        self.pushButton_7.setText(_translate("MainWindow", "ÇIKIŞ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow5()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
