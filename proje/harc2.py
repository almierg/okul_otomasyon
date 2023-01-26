from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3 as sql

class Ui_MainWindow14(object):
    def baglanti_yap(self):
        baglanti = sql.connect("harc4.db")
        self.cursor = baglanti.cursor()
        self.cursor.execute("CREATE TABLE If not exists ogrenci (İsim soyisim TEXT,IBAN TEXT)")
        baglanti.commit()

    def kayit5(self):
        isim = self.lineEdit_2.text()
        money = self.lineEdit.text()

        con = sql.connect('harc4.db')
        cur = con.cursor()
        cur.execute("CREATE TABLE If not exists ogrenci(isim Text,money TEXT)")
        cur.execute("INSERT INTO ogrenci VALUES(?,?)", (isim, money))

        con.commit()
        con.close()
        self.label_5.setText("İşlem Tamamlandı")

    def setupUi(self, MainWindow):
        self.baglanti_yap()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(994, 632)
        MainWindow.setMaximumSize(QtCore.QSize(950, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 90, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(170, 90, 251, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 140, 601, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 170, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 290, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 290, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 290, 81, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.kayit5)

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 340, 231, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 260, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 260, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HARÇ YATIRMA"))
        self.label.setText(_translate("MainWindow", "Banka:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Türkiye Cumhuriyeti Ziraat Bankası A.Ş."))
        self.comboBox.setItemText(1, _translate("MainWindow", "Türkiye Cumhuriyeti Ziraat Bankası A.Ş."))
        self.comboBox.setItemText(2, _translate("MainWindow", "Türkiye Halk Bankası A.Ş."))
        self.comboBox.setItemText(3, _translate("MainWindow", "Türkiye İş Bankası A.Ş."))
        self.comboBox.setItemText(4, _translate("MainWindow", "Vakıf Bank"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Türk Eximbank"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Türkiye Kalkınma Bankası A.Ş."))
        self.label_2.setText(_translate("MainWindow", "  -->Girdiğiniz IBAN numarası kendinize ait olmak zorundadır. Yoksa iade yapılamamaktadır."))
        self.label_3.setText(_translate("MainWindow", "-->Yaz okulu ücret iadeleri IBAN girişi için bu sayfayı kullanmayınız."))
        self.label_4.setText(_translate("MainWindow", "İBAN no:    TR"))
        self.pushButton.setText(_translate("MainWindow", "GÖNDER"))
        self.label_5.setText(_translate("MainWindow", ""))
        self.label_6.setText(_translate("MainWindow", "İsim Soyisim:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow14()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
