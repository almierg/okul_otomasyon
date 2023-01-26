from PyQt5 import QtCore, QtGui, QtWidgets
from dersler8 import Ui_MainWindow24
from duyurular_python import Ui_MainWindow7
from erasmus_python import Ui_MainWindow8
from staj_python import Ui_MainWindow9
from profil_python import Ui_MainWindow11
from PyQt5.QtWidgets import qApp
from not_goruntule import Ui_MainWindow13
from harc2 import Ui_MainWindow14
from anket_python import Ui_MainWindow10

class Ui_MainWindow12(object):
    def anket(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow10()
        self.ui.setupUi(self.window)
        self.window.show()

    def para(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow14()
        self.ui.setupUi(self.window)
        self.window.show()

    def not_goruntule(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow13()
        self.ui.setupUi(self.window)
        self.window.show()

    def sayfa(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow11()
        self.ui.setupUi(self.window)
        self.window.show()

    def cikis(self):
        qApp.quit()

    def staj(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow9()
        self.ui.setupUi(self.window)
        self.window.show()

    def dersler(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow24()
        self.ui.setupUi(self.window)
        self.window.show()

    def duyuru(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow7()
        self.ui.setupUi(self.window)
        self.window.show()

    def erasmus(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow8()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1367, 888)
        MainWindow.setMaximumSize(QtCore.QSize(1367, 858))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1371, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 80, 211, 111))
        self.pushButton.setStyleSheet("background-color: rgb(56, 103, 190);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.dersler)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 190, 211, 111))
        self.pushButton_2.setStyleSheet("background-color: rgb(56, 103, 190);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.not_goruntule)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 300, 211, 111))
        self.pushButton_3.setStyleSheet("background-color: rgb(56, 103, 190);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.duyuru)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 410, 211, 111))
        self.pushButton_4.setStyleSheet("background-color: rgb(56, 103, 190);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.erasmus)

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 520, 211, 111))
        self.pushButton_5.setStyleSheet("background-color: rgb(56, 103, 190);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.staj)

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 630, 211, 111))
        self.pushButton_6.setStyleSheet("background-color: rgb(56, 103, 190);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.para)

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 740, 211, 111))
        self.pushButton_7.setStyleSheet("background-color: rgb(56, 103, 190);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.anket)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1210, 20, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(1260, 50, 81, 21))
        self.pushButton_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.cikis)

        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(1170, 50, 81, 21))
        self.pushButton_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.sayfa)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ÖĞRENCİ BİLGİ SİSTEMİ"))
        self.label.setText(_translate("MainWindow", "             AKIL OKULLARI "))
        self.pushButton.setText(_translate("MainWindow", "DERSLER"))
        self.pushButton_2.setText(_translate("MainWindow", "NOT GÖRÜNTÜLE"))
        self.pushButton_3.setText(_translate("MainWindow", "DUYURULAR"))
        self.pushButton_4.setText(_translate("MainWindow", "ERASMUS"))
        self.pushButton_5.setText(_translate("MainWindow", "STAJ İŞLEMLERİ"))
        self.pushButton_6.setText(_translate("MainWindow", "HARÇ YATIRMA"))
        self.pushButton_7.setText(_translate("MainWindow", "ANKET"))
        self.label_2.setText(_translate("MainWindow", "ALMİLA ERGİN"))
        self.pushButton_8.setText(_translate("MainWindow", "ÇIKIŞ"))
        self.pushButton_9.setText(_translate("MainWindow", "SAYFAM"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow12()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
