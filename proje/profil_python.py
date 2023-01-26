from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import filedialog
from PyQt5.QtWidgets import QFileDialog, QLabel, QWidget
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
import os
import sys
import sqlite3 as sql
from PIL import Image, ImageTk


class Ui_MainWindow11(object):
    #def baglanti_yap2(self):
     #   baglanti = sql.connect("bilgiler.db")
      #  self.cursor = baglanti.cursor()
      #  self.cursor.execute("CREATE TABLE If not exists ogrenci (ad_soyad TEXT,bolum TEXT, mez_dur TEXT)")
      #  baglanti.commit()
    def veri(self):
        adsoyad = self.label_3.text()
        bolum = self.label_4.text()
        mezdur= self.label_6.text()

        con = sql.connect('iletisim.db')
        cur = con.cursor()
        cur.execute("CREATE TABLE If not exists ogrenci(ad_soyad TEXT,bolum TEXT, mez_dur TEXT)")
        cur.execute("INSERT INTO ogrenci VALUES(?,?,?)", (adsoyad,bolum,mezdur))

    def baglanti_yap(self):
        baglanti = sql.connect("iletisim.db")
        self.cursor = baglanti.cursor()
        self.cursor.execute("CREATE TABLE If not exists ogrenci (kuladi TEXT,sifre TEXT)")
        baglanti.commit()

    def kayit4(self):
        telno = self.lineEdit.text()
        e_posta = self.lineEdit_2.text()

        con = sql.connect('iletisim.db')
        cur = con.cursor()
        cur.execute("CREATE TABLE If not exists ogrenci(telno TEXT,e_posta TEXT)")
        cur.execute("INSERT INTO ogrenci VALUES(?,?)", (telno, e_posta))

        con.commit()
        con.close()
        self.label_12.setText("Bilgiler Güncellendi")


    def resim_ekle(self):
       # path = filedialog.askopenfilename(title="Select an Image",
        #                                   filetype=(('image    files', '*.jpg'), ('all files', '*.*')))
        #self.open(path)
        #my_image = ImageTk.PhotoImage(Image.open(root.path))
        #my_image_label = Label(image=my_image).pack()
        #self.label_10.setText(my_image_label)

        #path = filedialog.askopenfilename(title="Select an Image",
         #                                 filetype=(('image    files', '*.jpg'), ('all files', '*.*')))
        #self.Image.open(path, 'r')
        #self.ImageTk.PhotoImage(img)
        #self.label_10.setText(img.read())

        #dosya_yolu = tk.filedialog.askopenfilename()
        #etiket = QLabel(self)
        #dosya = etiket.setPixmap(QtGui.QPixmap(dosya_yolu))
        #self.label_10.setText(dosya)

        dosya_yolu = tk.filedialog.askopenfilename()
        self.dosya = ImageTk.PhotoImage(Image.open(dosya_yolu))
        self.label_10.setText(dosya)

    def setupUi(self, MainWindow):
        self.baglanti_yap()
        #self.baglanti_yap2()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1367, 888)
        MainWindow.setMaximumSize(QtCore.QSize(1367, 888))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(610, 300, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.resim_ekle)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(530, 350, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(570, 410, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(690, 350, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(690, 420, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(500, 470, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(690, 480, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 580, 431, 261))
        self.groupBox.setObjectName("groupBox")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 190, 141, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.kayit4)

        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(0, 70, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(80, 120, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(200, 70, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 120, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(570, 100, 191, 181))
        self.label_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(0, 0, 1361, 71))
        self.label_11.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")

        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(80, 150, 100, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SAYFAM"))
       # self.pushButton.setText(_translate("MainWindow", "RESMİNİZİ EKLEYİN"))
        self.label.setText(_translate("MainWindow", "AD VE SOYAD :"))
        self.label_2.setText(_translate("MainWindow", "BÖLÜMÜ :"))
        self.label_3.setText(_translate("MainWindow", "Almila ERGİN"))
        self.label_4.setText(_translate("MainWindow", "Bilgisayar Programcılığı"))
        self.label_5.setText(_translate("MainWindow", "MEZUN DURUMU :"))
        self.label_6.setText(_translate("MainWindow", "Aktif"))
        self.groupBox.setTitle(_translate("MainWindow", ""))
        self.pushButton_2.setText(_translate("MainWindow", "BİLGİLERİMİ GÜNCELLE"))
        self.label_9.setText(_translate("MainWindow", "TELEFON NUMARASI:"))
        self.label_8.setText(_translate("MainWindow", "E-POSTA:"))
        self.label_7.setText(_translate("MainWindow", "İLETİŞİM :"))
        self.label_12.setText(_translate("MainWindow", ""))
        self.label_10.setText(_translate("MainWindow", ""))
        self.pushButton.setText(_translate("MainWindow", "Resim Ekle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow11()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
