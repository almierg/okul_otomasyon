from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow9(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 600)
        MainWindow.setMaximumSize(QtCore.QSize(950, 600))
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 981, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 460, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 490, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 520, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 60, 941, 41))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 110, 801, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 140, 861, 41))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 180, 841, 41))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 220, 771, 31))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 260, 691, 21))
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "STAJ İŞLEMLERİ"))
        self.label.setText(_translate("MainWindow", "UYARI: 2021-2022 Yaz staj döneminden itibaren, öğrenciler İŞYERİ STAJI yapacaklardır. Ödev şeklinde staj yapılabilmesi uygulamasına son verilmiştir."))
        self.label_2.setText(_translate("MainWindow", "İLETİŞİM:"))
        self.label_3.setText(_translate("MainWindow", "Tel: 0 258 713 86 00 Dahili: 137"))
        self.label_4.setText(_translate("MainWindow", "E-posta: oznuru@pau.edu.tr"))
        self.label_5.setText(_translate("MainWindow", "Adım 1: http://pusula.pau.edu.tr adresinde “Öğrenci Bilgi Sistemi”ne girilir. “Staj İşlemleri” menüsünden “Staj Başvuru” linkine tıklanarak başvuru ekranına girilir."))
        self.label_6.setText(_translate("MainWindow", "Adım 2: “Yeni Başvuru” butonuna tıklanır.  Stajın yapılacağı yerin bilgileri kısmında “Kurum Stajı” seçeneği seçilmelidir."))
        self.label_7.setText(_translate("MainWindow", "Adım 3: Yapılacak Staj Türü seçilir. (1.Sınıf stajı için kodu 150 ile başlayan Yaz Stajı-I, 2. Sınıf stajı için kodu 250 ile başlayan Yaz Stajı-II seçilmelidir.)"))
        self.label_8.setText(_translate("MainWindow", "Adım 4: İstenilen bilgiler eksiksiz ve doğru biçimde ilgili alanlara girilir. (Staj yapılacak işyerine ait bilgiler girilmelidir. Sigorta bilgileri girilmelidir."))
        self.label_9.setText(_translate("MainWindow", "Adım 5: Staj yapılacak tarihler takvim üzerinden tek tek seçilir. (Staj başlangıç ve bitiş tarihleri yukarıda açıklanan tarihler olmalıdır.)"))
        self.label_10.setText(_translate("MainWindow", "Adım 6: “Kaydet” butonuna tıklanarak staj kaydedilir. (Kaydet butonuna basıldığında staj başvurunuz sisteme kaydedilir.)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow9()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
