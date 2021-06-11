# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaWorker.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VentanaPrincipalWorker(object):
    def setupUi(self, VentanaPrincipalWorker):
        VentanaPrincipalWorker.setObjectName("VentanaPrincipalWorker")
        VentanaPrincipalWorker.resize(899, 510)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/LogoApp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("img/LogoApp.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        VentanaPrincipalWorker.setWindowIcon(icon)
        VentanaPrincipalWorker.setStyleSheet("QWidget#centralwidget{\n"
"    background-color: \n"
"        qlineargradient(spread:pad, x1:0.181, y1:0, x2:0.858, y2:0, stop:0#fbe6c2, stop:0.511364 #F9E7E7, stop:1 #fbe6c2);\n"
"}\n"
"QFrame#frame_1{\n"
"    background-color:rgb(255, 157, 77, 200) ;\n"
"}\n"
"QFrame#frame_2\n"
"{\n"
"    background-color: #ffdb6e;\n"
"    border-right: 3px solid #a98600;\n"
"}  \n"
"")
        self.centralwidget = QtWidgets.QWidget(VentanaPrincipalWorker)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_1 = QtWidgets.QFrame(self.centralwidget)
        self.frame_1.setGeometry(QtCore.QRect(170, 0, 731, 81))
        self.frame_1.setStyleSheet("QWidget{\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    color: red;\n"
"    background-color: rgba(0,0,0, 0) ;\n"
"    border-bottom: 2px solid red;\n"
"    border-top: 2px solid red;\n"
"    border-radius: 1px;\n"
"}\n"
"QPushButton:hover{\n"
"    color: #c20d00;\n"
"     border-color: #c20d00;\n"
"}\n"
"QPushButton:pressed{\n"
"    color: #ff41330;\n"
"     border-color: #ff4133;\n"
"}\n"
"\n"
"QLabel#label_2{\n"
"    font-size: 25px;\n"
"}\n"
"QLabel#label, QLabel#label_3{\n"
"    font-size: 15px;\n"
"}")
        self.frame_1.setObjectName("frame_1")
        self.label = QtWidgets.QLabel(self.frame_1)
        self.label.setGeometry(QtCore.QRect(400, 40, 221, 21))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.frame_1)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 161, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.frame_1)
        self.label_2.setGeometry(QtCore.QRect(400, 10, 221, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_41 = QtWidgets.QLabel(self.frame_1)
        self.label_41.setGeometry(QtCore.QRect(200, 30, 201, 21))
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.frame_1)
        self.label_42.setGeometry(QtCore.QRect(650, 0, 61, 81))
        self.label_42.setStyleSheet("")
        self.label_42.setText("")
        self.label_42.setPixmap(QtGui.QPixmap("img/User_icon.png"))
        self.label_42.setScaledContents(True)
        self.label_42.setObjectName("label_42")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_1)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 30, 161, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/Red_cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_4.setObjectName("pushButton_4")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 171, 511))
        self.frame_2.setStyleSheet("QWidget{\n"
"\n"
"}\n"
"QLabel{\n"
"    font-size: 12px;\n"
"}\n"
"QPushButton{\n"
"    font-size: 16px;\n"
"    color: black;\n"
"    background-color: rgba(255,249,174, 150) ;\n"
"    border: 2px ridge #808000;\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:#fff9ae ;\n"
"    color: #a98600;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:#a98600 ;\n"
"    color: #FFFF00;\n"
"}\n"
"")
        self.frame_2.setObjectName("frame_2")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(30, 400, 101, 101))
        self.label_4.setStyleSheet(" border: 2px solid rgb(0, 0, 0);")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("img/logoWM.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(30, 380, 101, 21))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(10, 170, 141, 71))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 280, 141, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(20, 10, 131, 131))
        self.label_6.setStyleSheet("")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("img/LogoApp.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(180, 80, 711, 431))
        self.stackedWidget.setStyleSheet("QWidget{\n"
"    font-size: 16px;\n"
"}\n"
"QWidget#stackedWidget{\n"
"    background-color:rgba(0, 0, 0, 0) ;\n"
"}\n"
"\n"
"QLabel#label_7, QLabel#label_9, QLabel#label_40{\n"
"    font-size: 20px;\n"
"}\n"
"QLineEdit{\n"
"    font-size: 12px;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    font-size: 16px;\n"
"    color: black;\n"
"    border: 2px ridge;\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton#pushButton_20, QPushButton#pushButton_21{\n"
"    background-color: #D0F0C0;\n"
"    border-color: #0b6623;\n"
"}\n"
"QPushButton:hover#pushButton_20, QPushButton:hover#pushButton_21{\n"
"    background-color: #98FB98;\n"
"    color: #0b6623;\n"
"}\n"
"QPushButton:pressed#pushButton_20, QPushButton:pressed#pushButton_21{\n"
"    background-color:#0b6623;\n"
"    color: #98FB98;\n"
"}\n"
"QPushButton#pushButton_22, QPushButton#pushButton_23{\n"
"    background-color: #f5a49a;\n"
"    border-color: #b51a00;\n"
"}\n"
"QPushButton:hover#pushButton_22, QPushButton:hover#pushButton_23{\n"
"    background-color: #FA8072;\n"
"    color: #FF2400;\n"
"}\n"
"QPushButton:pressed#pushButton_22, QPushButton:pressed#pushButton_23{\n"
"    background-color:#FF2400;\n"
"    color: #FA8072;\n"
"}\n"
"\n"
"\n"
"QListWidget {\n"
"    background: white;\n"
"}\n"
"QListView::item { \n"
"    background-color:#fff9ae;\n"
"    color:#a98600;\n"
" }\n"
"QListView::item:alternate {\n"
"     background-color:#a98600;\n"
"    color: rgb(255, 232, 99);\n"
" } \n"
"QListView::item:selected {\n"
"    background-color: rgba(255,127,80, 250);\n"
"    color:  black;\n"
" }\n"
"\n"
"")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_52 = QtWidgets.QLabel(self.page_3)
        self.label_52.setGeometry(QtCore.QRect(20, 40, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_52.setFont(font)
        self.label_52.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_52.setObjectName("label_52")
        self.label_40 = QtWidgets.QLabel(self.page_3)
        self.label_40.setGeometry(QtCore.QRect(20, 10, 681, 31))
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.listProd_6 = QtWidgets.QListWidget(self.page_3)
        self.listProd_6.setGeometry(QtCore.QRect(290, 100, 401, 271))
        font = QtGui.QFont()
        font.setFamily("Prototype")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.listProd_6.setFont(font)
        self.listProd_6.setStyleSheet("")
        self.listProd_6.setAlternatingRowColors(True)
        self.listProd_6.setObjectName("listProd_6")
        self.label_49 = QtWidgets.QLabel(self.page_3)
        self.label_49.setGeometry(QtCore.QRect(290, 50, 221, 31))
        self.label_49.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_49.setObjectName("label_49")
        self.label_50 = QtWidgets.QLabel(self.page_3)
        self.label_50.setGeometry(QtCore.QRect(510, 50, 181, 31))
        self.label_50.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_50.setObjectName("label_50")
        self.listProd_4 = QtWidgets.QListWidget(self.page_3)
        self.listProd_4.setGeometry(QtCore.QRect(20, 60, 231, 351))
        font = QtGui.QFont()
        font.setFamily("Prototype")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.listProd_4.setFont(font)
        self.listProd_4.setStyleSheet("")
        self.listProd_4.setAlternatingRowColors(True)
        self.listProd_4.setObjectName("listProd_4")
        self.pushButton_21 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_21.setGeometry(QtCore.QRect(530, 380, 151, 31))
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_23 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_23.setGeometry(QtCore.QRect(290, 380, 151, 31))
        self.pushButton_23.setObjectName("pushButton_23")
        self.label_51 = QtWidgets.QLabel(self.page_3)
        self.label_51.setGeometry(QtCore.QRect(290, 70, 221, 31))
        self.label_51.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_51.setObjectName("label_51")
        self.label_54 = QtWidgets.QLabel(self.page_3)
        self.label_54.setGeometry(QtCore.QRect(260, 140, 21, 21))
        self.label_54.setStyleSheet("")
        self.label_54.setText("")
        self.label_54.setPixmap(QtGui.QPixmap("img/Arrow_Right.png"))
        self.label_54.setScaledContents(True)
        self.label_54.setObjectName("label_54")
        self.label_55 = QtWidgets.QLabel(self.page_3)
        self.label_55.setGeometry(QtCore.QRect(260, 170, 21, 21))
        self.label_55.setStyleSheet("")
        self.label_55.setText("")
        self.label_55.setPixmap(QtGui.QPixmap("img/Arrow_Right.png"))
        self.label_55.setScaledContents(True)
        self.label_55.setObjectName("label_55")
        self.label_56 = QtWidgets.QLabel(self.page_3)
        self.label_56.setGeometry(QtCore.QRect(260, 200, 21, 21))
        self.label_56.setStyleSheet("")
        self.label_56.setText("")
        self.label_56.setPixmap(QtGui.QPixmap("img/Arrow_Right.png"))
        self.label_56.setScaledContents(True)
        self.label_56.setObjectName("label_56")
        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.pushButton_22 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_22.setGeometry(QtCore.QRect(310, 380, 151, 31))
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_20 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_20.setGeometry(QtCore.QRect(510, 380, 151, 31))
        self.pushButton_20.setObjectName("pushButton_20")
        self.listProd_3 = QtWidgets.QListWidget(self.page_2)
        self.listProd_3.setGeometry(QtCore.QRect(20, 60, 231, 351))
        font = QtGui.QFont()
        font.setFamily("Prototype")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.listProd_3.setFont(font)
        self.listProd_3.setStyleSheet("")
        self.listProd_3.setAlternatingRowColors(True)
        self.listProd_3.setObjectName("listProd_3")
        self.label_47 = QtWidgets.QLabel(self.page_2)
        self.label_47.setGeometry(QtCore.QRect(290, 50, 221, 31))
        self.label_47.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_47.setObjectName("label_47")
        self.label_9 = QtWidgets.QLabel(self.page_2)
        self.label_9.setGeometry(QtCore.QRect(10, 9, 691, 31))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_46 = QtWidgets.QLabel(self.page_2)
        self.label_46.setGeometry(QtCore.QRect(20, 40, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_46.setFont(font)
        self.label_46.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_46.setObjectName("label_46")
        self.listProd_5 = QtWidgets.QListWidget(self.page_2)
        self.listProd_5.setGeometry(QtCore.QRect(290, 80, 401, 291))
        font = QtGui.QFont()
        font.setFamily("Prototype")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.listProd_5.setFont(font)
        self.listProd_5.setStyleSheet("")
        self.listProd_5.setAlternatingRowColors(True)
        self.listProd_5.setObjectName("listProd_5")
        self.label_43 = QtWidgets.QLabel(self.page_2)
        self.label_43.setGeometry(QtCore.QRect(260, 110, 21, 21))
        self.label_43.setStyleSheet("")
        self.label_43.setText("")
        self.label_43.setPixmap(QtGui.QPixmap("img/Arrow_Right.png"))
        self.label_43.setScaledContents(True)
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.page_2)
        self.label_44.setGeometry(QtCore.QRect(260, 140, 21, 21))
        self.label_44.setStyleSheet("")
        self.label_44.setText("")
        self.label_44.setPixmap(QtGui.QPixmap("img/Arrow_Right.png"))
        self.label_44.setScaledContents(True)
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.page_2)
        self.label_45.setGeometry(QtCore.QRect(260, 170, 21, 21))
        self.label_45.setStyleSheet("")
        self.label_45.setText("")
        self.label_45.setPixmap(QtGui.QPixmap("img/Arrow_Right.png"))
        self.label_45.setScaledContents(True)
        self.label_45.setObjectName("label_45")
        self.stackedWidget.addWidget(self.page_2)
        VentanaPrincipalWorker.setCentralWidget(self.centralwidget)
        self.actionSalir = QtWidgets.QAction(VentanaPrincipalWorker)
        self.actionSalir.setObjectName("actionSalir")

        self.retranslateUi(VentanaPrincipalWorker)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(VentanaPrincipalWorker)

    def retranslateUi(self, VentanaPrincipalWorker):
        _translate = QtCore.QCoreApplication.translate
        VentanaPrincipalWorker.setWindowTitle(_translate("VentanaPrincipalWorker", "RestauranTEC Principal Worker"))
        self.label.setText(_translate("VentanaPrincipalWorker", "Rol"))
        self.label_3.setText(_translate("VentanaPrincipalWorker", "Hora"))
        self.label_2.setText(_translate("VentanaPrincipalWorker", "Usuario"))
        self.label_41.setText(_translate("VentanaPrincipalWorker", "Version"))
        self.pushButton_4.setText(_translate("VentanaPrincipalWorker", " Cerrar Sesion"))
        self.label_5.setText(_translate("VentanaPrincipalWorker", "Desarrollado por"))
        self.pushButton.setText(_translate("VentanaPrincipalWorker", "Control\n"
"Cocina"))
        self.pushButton_2.setText(_translate("VentanaPrincipalWorker", "Control\n"
"Entregas"))
        self.label_52.setText(_translate("VentanaPrincipalWorker", "Lista de Ordenes"))
        self.label_40.setText(_translate("VentanaPrincipalWorker", "Menu de Control de Entregas"))
        self.label_49.setText(_translate("VentanaPrincipalWorker", "Entregar a Mesa #"))
        self.label_50.setText(_translate("VentanaPrincipalWorker", "1"))
        self.pushButton_21.setText(_translate("VentanaPrincipalWorker", "Entregar Orden"))
        self.pushButton_23.setText(_translate("VentanaPrincipalWorker", "Devolver Orden"))
        self.label_51.setText(_translate("VentanaPrincipalWorker", "Lista de Productos en Orden"))
        self.pushButton_22.setText(_translate("VentanaPrincipalWorker", "Devolver Orden"))
        self.pushButton_20.setText(_translate("VentanaPrincipalWorker", "Entregar Orden"))
        self.label_47.setText(_translate("VentanaPrincipalWorker", "Lista de Productos en Orden"))
        self.label_9.setText(_translate("VentanaPrincipalWorker", "Menu de Control de Cocina"))
        self.label_46.setText(_translate("VentanaPrincipalWorker", "Lista de Ordenes"))
        self.actionSalir.setText(_translate("VentanaPrincipalWorker", "Salir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaPrincipalWorker = QtWidgets.QMainWindow()
    ui = Ui_VentanaPrincipalWorker()
    ui.setupUi(VentanaPrincipalWorker)
    VentanaPrincipalWorker.show()
    sys.exit(app.exec_())
