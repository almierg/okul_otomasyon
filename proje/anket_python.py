from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser

class Ui_MainWindow10(object):
    def tanisma(self):
        webbrowser.open('https://forms.gle/Tirf8kVQLDyn2zuz7', new=2)

    def etkinlik(self):
        webbrowser.open('https://forms.gle/dZQHufRDC41orBx56', new=2)

    def sosyal(self):
        webbrowser.open('https://forms.gle/FWGHicUV6yxKXH449', new=2)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 600)
        MainWindow.setMaximumSize(QtCore.QSize(950, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 361, 81))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 160, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 220, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 280, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 160, 81, 21))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.tanisma)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 230, 81, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.etkinlik)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 300, 81, 21))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.sosyal)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ANKET"))
        self.label.setText(_translate("MainWindow", "Yapmanız gereken anketler"))
        self.label_2.setText(_translate("MainWindow", "Tanışma zamanı"))
        self.label_3.setText(_translate("MainWindow", "Nasıl bir etkinlik istersin?"))
        self.label_4.setText(_translate("MainWindow", "Sosyal sorumluluk projesi"))
        self.pushButton.setText(_translate("MainWindow", "Göz At"))
        self.pushButton_2.setText(_translate("MainWindow", "Göz At"))
        self.pushButton_3.setText(_translate("MainWindow", "Göz At"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow10()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
