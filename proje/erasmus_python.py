from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser

class Ui_MainWindow8(object):
    def bilgi(self):
        webbrowser.open('https://www.pau.edu.tr/uluslararasi/tr/haber/2022-2023-akademik-yili-erasmus-ka131-ogrenim-hareketliligi-basvuru-ve-yerlestirme-takvimi', new=2)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 600)
        MainWindow.setMaximumSize(QtCore.QSize(950, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 120, 431, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 190, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 200, 93, 28))
        self.pushButton.clicked.connect(self.bilgi)

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ERASMUS"))
        self.label.setText(_translate("MainWindow", "Erasmus başvurusu süresi doldu."))
        self.label_2.setText(_translate("MainWindow", "Başvuru süreci için "))
        self.pushButton.setText(_translate("MainWindow", "tıklayınız."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow8()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
