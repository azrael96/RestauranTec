# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaAdmin.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VentanaPrincipalAdmin(object):
    def setupUi(self, VentanaPrincipalAdmin):
        VentanaPrincipalAdmin.setObjectName("VentanaPrincipalAdmin")
        VentanaPrincipalAdmin.resize(899, 510)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/LogoApp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("img/LogoApp.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        VentanaPrincipalAdmin.setWindowIcon(icon)
        VentanaPrincipalAdmin.setStyleSheet("QWidget#centralwidget{\n"
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
        self.centralwidget = QtWidgets.QWidget(VentanaPrincipalAdmin)
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
        self.pushButton.setGeometry(QtCore.QRect(10, 160, 151, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 200, 151, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 240, 151, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 300, 111, 61))
        self.pushButton_5.setObjectName("pushButton_5")
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
"QLineEdit, QComboBox{\n"
"    font-size: 12px;\n"
"    border-radius: 10px;\n"
"}\n"
"QComboBox::drop-down {\n"
"    width: 25px;\n"
"    border-left-width: 5px;\n"
"    border-left-color:#FF4500;\n"
"    border-left-style: groove; /* just a single line */\n"
"    border-top-right-radius: 10px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: url(C://Users/Alexander/Desktop/RestauranTEC/RestauranTec/img/arrow.png);\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"    font-size: 16px;\n"
"    color: black;\n"
"    background-color: rgba(255,127,80, 250) ;\n"
"    border: 2px ridge #FF4500;\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgba(255,127,80, 150) ;\n"
"    color: #FF4500;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:#FF4500 ;\n"
"    color:black;\n"
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
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget.addWidget(self.page_4)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_7 = QtWidgets.QLabel(self.page)
        self.label_7.setGeometry(QtCore.QRect(210, 10, 491, 20))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.listProd = QtWidgets.QListWidget(self.page)
        self.listProd.setGeometry(QtCore.QRect(10, 40, 191, 381))
        font = QtGui.QFont()
        font.setFamily("Prototype")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.listProd.setFont(font)
        self.listProd.setStyleSheet("")
        self.listProd.setAlternatingRowColors(True)
        self.listProd.setObjectName("listProd")
        self.pushButton_6 = QtWidgets.QPushButton(self.page)
        self.pushButton_6.setGeometry(QtCore.QRect(570, 380, 91, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.page)
        self.pushButton_7.setGeometry(QtCore.QRect(410, 380, 91, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.page)
        self.pushButton_8.setGeometry(QtCore.QRect(250, 380, 91, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_10 = QtWidgets.QLabel(self.page)
        self.label_10.setGeometry(QtCore.QRect(10, 20, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.lineEdit = QtWidgets.QLineEdit(self.page)
        self.lineEdit.setGeometry(QtCore.QRect(310, 150, 141, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_2.setGeometry(QtCore.QRect(310, 190, 141, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_3.setGeometry(QtCore.QRect(310, 230, 141, 20))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_5.setGeometry(QtCore.QRect(310, 350, 141, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_6.setGeometry(QtCore.QRect(310, 310, 141, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.comboBox = QtWidgets.QComboBox(self.page)
        self.comboBox.setGeometry(QtCore.QRect(560, 270, 141, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_11 = QtWidgets.QLabel(self.page)
        self.label_11.setGeometry(QtCore.QRect(210, 150, 111, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.page)
        self.label_12.setGeometry(QtCore.QRect(210, 190, 111, 21))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.page)
        self.label_13.setGeometry(QtCore.QRect(460, 350, 61, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.page)
        self.label_14.setGeometry(QtCore.QRect(210, 350, 111, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.page)
        self.label_15.setGeometry(QtCore.QRect(210, 230, 111, 21))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.page)
        self.label_16.setGeometry(QtCore.QRect(460, 310, 61, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.page)
        self.label_17.setGeometry(QtCore.QRect(210, 270, 111, 21))
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.page)
        self.label_18.setGeometry(QtCore.QRect(210, 310, 111, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.page)
        self.label_19.setGeometry(QtCore.QRect(460, 270, 61, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.page)
        self.label_20.setGeometry(QtCore.QRect(460, 150, 81, 16))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.page)
        self.label_21.setGeometry(QtCore.QRect(460, 190, 91, 16))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.page)
        self.label_22.setGeometry(QtCore.QRect(460, 230, 61, 16))
        self.label_22.setObjectName("label_22")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_4.setGeometry(QtCore.QRect(560, 150, 141, 20))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_10.setGeometry(QtCore.QRect(560, 310, 141, 20))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_11.setGeometry(QtCore.QRect(560, 350, 141, 20))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_12.setGeometry(QtCore.QRect(560, 190, 141, 20))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.comboBox_2 = QtWidgets.QComboBox(self.page)
        self.comboBox_2.setGeometry(QtCore.QRect(560, 230, 141, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, "")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.page)
        self.comboBox_3.setGeometry(QtCore.QRect(310, 270, 141, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.setItemText(0, "")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.pushButton_11 = QtWidgets.QPushButton(self.page)
        self.pushButton_11.setGeometry(QtCore.QRect(390, 50, 131, 31))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_9 = QtWidgets.QPushButton(self.page)
        self.pushButton_9.setGeometry(QtCore.QRect(220, 50, 131, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.page)
        self.pushButton_10.setGeometry(QtCore.QRect(560, 50, 131, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_39 = QtWidgets.QLabel(self.page)
        self.label_39.setGeometry(QtCore.QRect(210, 110, 491, 20))
        self.label_39.setAlignment(QtCore.Qt.AlignCenter)
        self.label_39.setObjectName("label_39")
        self.line = QtWidgets.QFrame(self.page)
        self.line.setGeometry(QtCore.QRect(210, 90, 491, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.page)
        self.line_2.setGeometry(QtCore.QRect(210, 410, 491, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_55 = QtWidgets.QLabel(self.page_2)
        self.label_55.setGeometry(QtCore.QRect(220, 170, 111, 16))
        self.label_55.setObjectName("label_55")
        self.label_44 = QtWidgets.QLabel(self.page_2)
        self.label_44.setGeometry(QtCore.QRect(220, 290, 111, 21))
        self.label_44.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_44.setObjectName("label_44")
        self.label_50 = QtWidgets.QLabel(self.page_2)
        self.label_50.setGeometry(QtCore.QRect(220, 250, 111, 21))
        self.label_50.setObjectName("label_50")
        self.line_4 = QtWidgets.QFrame(self.page_2)
        self.line_4.setGeometry(QtCore.QRect(210, 400, 491, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_54 = QtWidgets.QLabel(self.page_2)
        self.label_54.setGeometry(QtCore.QRect(220, 210, 111, 16))
        self.label_54.setObjectName("label_54")
        self.line_3 = QtWidgets.QFrame(self.page_2)
        self.line_3.setGeometry(QtCore.QRect(210, 100, 491, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_19.setGeometry(QtCore.QRect(310, 210, 201, 20))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.pushButton_22 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_22.setGeometry(QtCore.QRect(560, 360, 91, 31))
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_20 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_20.setGeometry(QtCore.QRect(250, 360, 91, 31))
        self.pushButton_20.setObjectName("pushButton_20")
        self.listProd_3 = QtWidgets.QListWidget(self.page_2)
        self.listProd_3.setGeometry(QtCore.QRect(10, 40, 191, 371))
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
        self.lineEdit_25 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_25.setGeometry(QtCore.QRect(310, 170, 201, 20))
        self.lineEdit_25.setText("")
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.pushButton_18 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_18.setGeometry(QtCore.QRect(210, 60, 131, 31))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_21 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_21.setGeometry(QtCore.QRect(560, 60, 131, 31))
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_19 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_19.setGeometry(QtCore.QRect(390, 60, 131, 31))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_23 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_23.setGeometry(QtCore.QRect(400, 360, 91, 31))
        self.pushButton_23.setObjectName("pushButton_23")
        self.label_47 = QtWidgets.QLabel(self.page_2)
        self.label_47.setGeometry(QtCore.QRect(210, 130, 491, 20))
        self.label_47.setAlignment(QtCore.Qt.AlignCenter)
        self.label_47.setObjectName("label_47")
        self.comboBox_9 = QtWidgets.QComboBox(self.page_2)
        self.comboBox_9.setGeometry(QtCore.QRect(310, 250, 201, 22))
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.setItemText(0, "")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.label_9 = QtWidgets.QLabel(self.page_2)
        self.label_9.setGeometry(QtCore.QRect(210, 20, 491, 20))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_46 = QtWidgets.QLabel(self.page_2)
        self.label_46.setGeometry(QtCore.QRect(10, 20, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_46.setFont(font)
        self.label_46.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_46.setObjectName("label_46")
        self.label_43 = QtWidgets.QLabel(self.page_2)
        self.label_43.setGeometry(QtCore.QRect(550, 210, 121, 121))
        self.label_43.setStyleSheet("")
        self.label_43.setText("")
        self.label_43.setPixmap(QtGui.QPixmap("img/Taco.png"))
        self.label_43.setScaledContents(True)
        self.label_43.setObjectName("label_43")
        self.label_56 = QtWidgets.QLabel(self.page_2)
        self.label_56.setGeometry(QtCore.QRect(560, 170, 111, 16))
        self.label_56.setObjectName("label_56")
        self.textEdit = QtWidgets.QTextEdit(self.page_2)
        self.textEdit.setGeometry(QtCore.QRect(310, 290, 201, 61))
        self.textEdit.setObjectName("textEdit")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_52 = QtWidgets.QLabel(self.page_3)
        self.label_52.setGeometry(QtCore.QRect(40, 50, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_52.setFont(font)
        self.label_52.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_52.setObjectName("label_52")
        self.pushButton_27 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_27.setGeometry(QtCore.QRect(370, 320, 271, 31))
        self.pushButton_27.setObjectName("pushButton_27")
        self.label_40 = QtWidgets.QLabel(self.page_3)
        self.label_40.setGeometry(QtCore.QRect(20, 10, 681, 31))
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.listProd_4 = QtWidgets.QListWidget(self.page_3)
        self.listProd_4.setGeometry(QtCore.QRect(40, 70, 261, 331))
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
        self.pushButton_26 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_26.setGeometry(QtCore.QRect(390, 140, 231, 31))
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_29 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_29.setGeometry(QtCore.QRect(370, 240, 271, 31))
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_30 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_30.setGeometry(QtCore.QRect(370, 280, 271, 31))
        self.pushButton_30.setObjectName("pushButton_30")
        self.label_53 = QtWidgets.QLabel(self.page_3)
        self.label_53.setGeometry(QtCore.QRect(410, 110, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_53.setFont(font)
        self.label_53.setText("")
        self.label_53.setAlignment(QtCore.Qt.AlignCenter)
        self.label_53.setObjectName("label_53")
        self.stackedWidget.addWidget(self.page_3)
        VentanaPrincipalAdmin.setCentralWidget(self.centralwidget)
        self.actionSalir = QtWidgets.QAction(VentanaPrincipalAdmin)
        self.actionSalir.setObjectName("actionSalir")

        self.retranslateUi(VentanaPrincipalAdmin)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(VentanaPrincipalAdmin)

    def retranslateUi(self, VentanaPrincipalAdmin):
        _translate = QtCore.QCoreApplication.translate
        VentanaPrincipalAdmin.setWindowTitle(_translate("VentanaPrincipalAdmin", "RestauranTEC Principal Admin"))
        self.label.setText(_translate("VentanaPrincipalAdmin", "Rol"))
        self.label_3.setText(_translate("VentanaPrincipalAdmin", "Hora"))
        self.label_2.setText(_translate("VentanaPrincipalAdmin", "Usuario"))
        self.label_41.setText(_translate("VentanaPrincipalAdmin", "Version"))
        self.pushButton_4.setText(_translate("VentanaPrincipalAdmin", " Cerrar Sesion"))
        self.label_5.setText(_translate("VentanaPrincipalAdmin", "Desarrollado por"))
        self.pushButton.setText(_translate("VentanaPrincipalAdmin", "Control Usuarios"))
        self.pushButton_2.setText(_translate("VentanaPrincipalAdmin", "Control Menu"))
        self.pushButton_3.setText(_translate("VentanaPrincipalAdmin", "Registro Ventas"))
        self.pushButton_5.setText(_translate("VentanaPrincipalAdmin", "Activar\n"
"Restaurante"))
        self.label_7.setText(_translate("VentanaPrincipalAdmin", "Menu de Control de Usuarios"))
        self.pushButton_6.setText(_translate("VentanaPrincipalAdmin", "Cancelar"))
        self.pushButton_7.setText(_translate("VentanaPrincipalAdmin", "Limpiar"))
        self.pushButton_8.setText(_translate("VentanaPrincipalAdmin", "Guardar"))
        self.label_10.setText(_translate("VentanaPrincipalAdmin", "Lista de Usuarios"))
        self.comboBox.setItemText(1, _translate("VentanaPrincipalAdmin", "ADMON"))
        self.comboBox.setItemText(2, _translate("VentanaPrincipalAdmin", "WORKER"))
        self.label_11.setText(_translate("VentanaPrincipalAdmin", "Nombre"))
        self.label_12.setText(_translate("VentanaPrincipalAdmin", "1er Apellido"))
        self.label_13.setText(_translate("VentanaPrincipalAdmin", "Telefono"))
        self.label_14.setText(_translate("VentanaPrincipalAdmin", "Direccion"))
        self.label_15.setText(_translate("VentanaPrincipalAdmin", "2nd Apellido"))
        self.label_16.setText(_translate("VentanaPrincipalAdmin", "Correo"))
        self.label_17.setText(_translate("VentanaPrincipalAdmin", "Tipo de Doc"))
        self.label_18.setText(_translate("VentanaPrincipalAdmin", "Num de Doc"))
        self.label_19.setText(_translate("VentanaPrincipalAdmin", "Rol"))
        self.label_20.setText(_translate("VentanaPrincipalAdmin", "Usuario"))
        self.label_21.setText(_translate("VentanaPrincipalAdmin", "Contraseña"))
        self.label_22.setText(_translate("VentanaPrincipalAdmin", "Estado"))
        self.comboBox_2.setItemText(1, _translate("VentanaPrincipalAdmin", "ACTIVO"))
        self.comboBox_2.setItemText(2, _translate("VentanaPrincipalAdmin", "EN PELIGRO"))
        self.comboBox_2.setItemText(3, _translate("VentanaPrincipalAdmin", "BLOQUEADO"))
        self.comboBox_3.setItemText(1, _translate("VentanaPrincipalAdmin", "Cedula Ciudadania"))
        self.comboBox_3.setItemText(2, _translate("VentanaPrincipalAdmin", "Cedula Extrangeria"))
        self.comboBox_3.setItemText(3, _translate("VentanaPrincipalAdmin", "NIT"))
        self.pushButton_11.setText(_translate("VentanaPrincipalAdmin", "Añádir Usuario"))
        self.pushButton_9.setText(_translate("VentanaPrincipalAdmin", "Editar Usuario"))
        self.pushButton_10.setText(_translate("VentanaPrincipalAdmin", "Eliminar Usuario"))
        self.label_39.setText(_translate("VentanaPrincipalAdmin", "Informacion Usuario"))
        self.label_55.setText(_translate("VentanaPrincipalAdmin", "Nombre"))
        self.label_44.setText(_translate("VentanaPrincipalAdmin", "Descripcion"))
        self.label_50.setText(_translate("VentanaPrincipalAdmin", "Tipo"))
        self.label_54.setText(_translate("VentanaPrincipalAdmin", "Precio"))
        self.pushButton_22.setText(_translate("VentanaPrincipalAdmin", "Cancelar"))
        self.pushButton_20.setText(_translate("VentanaPrincipalAdmin", "Guardar"))
        self.pushButton_18.setText(_translate("VentanaPrincipalAdmin", "Eliminar Plato"))
        self.pushButton_21.setText(_translate("VentanaPrincipalAdmin", "Editar Plato"))
        self.pushButton_19.setText(_translate("VentanaPrincipalAdmin", "Añádir Plato"))
        self.pushButton_23.setText(_translate("VentanaPrincipalAdmin", "Limpiar"))
        self.label_47.setText(_translate("VentanaPrincipalAdmin", "Informacion Usuario"))
        self.comboBox_9.setItemText(1, _translate("VentanaPrincipalAdmin", "BEBIDA"))
        self.comboBox_9.setItemText(2, _translate("VentanaPrincipalAdmin", "PRINCIPAL"))
        self.comboBox_9.setItemText(3, _translate("VentanaPrincipalAdmin", "ENTRADA"))
        self.label_9.setText(_translate("VentanaPrincipalAdmin", "Menu de Control de Menu"))
        self.label_46.setText(_translate("VentanaPrincipalAdmin", "Lista de Platos"))
        self.label_56.setText(_translate("VentanaPrincipalAdmin", "Foto"))
        self.label_52.setText(_translate("VentanaPrincipalAdmin", "Lista de Facturas"))
        self.pushButton_27.setText(_translate("VentanaPrincipalAdmin", "Generar Reporte Facturas Completo"))
        self.label_40.setText(_translate("VentanaPrincipalAdmin", "Menu de Registros de Ventas"))
        self.pushButton_26.setText(_translate("VentanaPrincipalAdmin", "Descargar Factura Selecionada"))
        self.pushButton_29.setText(_translate("VentanaPrincipalAdmin", "Generar Reporte Facturas Anual"))
        self.pushButton_30.setText(_translate("VentanaPrincipalAdmin", "Generar Reporte Facturas Mensual"))
        self.actionSalir.setText(_translate("VentanaPrincipalAdmin", "Salir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaPrincipalAdmin = QtWidgets.QMainWindow()
    ui = Ui_VentanaPrincipalAdmin()
    ui.setupUi(VentanaPrincipalAdmin)
    VentanaPrincipalAdmin.show()
    sys.exit(app.exec_())
