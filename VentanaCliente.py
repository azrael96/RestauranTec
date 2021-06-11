# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaCliente.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VentanaPrincipalCliente(object):
    def setupUi(self, VentanaPrincipalCliente):
        VentanaPrincipalCliente.setObjectName("VentanaPrincipalCliente")
        VentanaPrincipalCliente.resize(899, 510)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/LogoApp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("img/LogoApp.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        VentanaPrincipalCliente.setWindowIcon(icon)
        VentanaPrincipalCliente.setStyleSheet("QWidget#centralwidget{\n"
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
        VentanaPrincipalCliente.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(VentanaPrincipalCliente)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 881, 491))
        self.stackedWidget.setStyleSheet("QWidget{\n"
"    font-size: 16px;\n"
"}\n"
"QWidget#stackedWidget{\n"
"    background-color:rgba(0, 0, 0, 0) ;\n"
"}\n"
"QLabel#label_54{\n"
"    font-size: 20px;\n"
"}\n"
"QLabel#label_9, QLabel#label_40, QLabel#label_10{\n"
"    font-size: 25px;\n"
"}\n"
"QLabel#label_66, QLabel#label_75, QLabel#label_76{\n"
"    color: rgba(0,0,0, 0) ;\n"
"}\n"
"QLineEdit, QSpinBox{\n"
"    font-size: 12px;\n"
"    border-radius: 10px;\n"
"}\n"
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
"QPushButton#pushButton_20, QPushButton#pushButton_21, QPushButton#pushButton_25{\n"
"    background-color: #D0F0C0;\n"
"    border-color: #0b6623;\n"
"}\n"
"QPushButton:hover#pushButton_20, QPushButton:hover#pushButton_21, QPushButton:hover#pushButton_25{\n"
"    background-color: #98FB98;\n"
"    color: #0b6623;\n"
"}\n"
"QPushButton:pressed#pushButton_20, QPushButton:pressed#pushButton_21, QPushButton:pressed#pushButton_25{\n"
"    background-color:#0b6623;\n"
"    color: #98FB98;\n"
"}\n"
"QPushButton#pushButton_22, QPushButton#pushButton_23, QPushButton#pushButton_26{\n"
"    background-color: #f5a49a;\n"
"    border-color: #b51a00;\n"
"}\n"
"QPushButton:hover#pushButton_22, QPushButton:hover#pushButton_23, QPushButton:hover#pushButton_26{\n"
"    background-color: #FA8072;\n"
"    color: #FF2400;\n"
"}\n"
"QPushButton:pressed#pushButton_22, QPushButton:pressed#pushButton_23, QPushButton:pressed#pushButton_26{\n"
"    background-color:#FF2400;\n"
"    color: #FA8072;\n"
"}\n"
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
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.pushButton_22 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_22.setGeometry(QtCore.QRect(670, 440, 71, 31))
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_20 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_20.setGeometry(QtCore.QRect(750, 440, 121, 31))
        self.pushButton_20.setObjectName("pushButton_20")
        self.listProd_3 = QtWidgets.QListWidget(self.page_2)
        self.listProd_3.setGeometry(QtCore.QRect(20, 90, 261, 381))
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
        self.label_47.setGeometry(QtCore.QRect(290, 50, 311, 31))
        self.label_47.setAlignment(QtCore.Qt.AlignCenter)
        self.label_47.setObjectName("label_47")
        self.label_9 = QtWidgets.QLabel(self.page_2)
        self.label_9.setGeometry(QtCore.QRect(0, 10, 881, 31))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_46 = QtWidgets.QLabel(self.page_2)
        self.label_46.setGeometry(QtCore.QRect(20, 70, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_46.setFont(font)
        self.label_46.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_46.setObjectName("label_46")
        self.listProd_5 = QtWidgets.QListWidget(self.page_2)
        self.listProd_5.setGeometry(QtCore.QRect(610, 30, 251, 371))
        font = QtGui.QFont()
        font.setFamily("Prototype")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.listProd_5.setFont(font)
        self.listProd_5.setStyleSheet("")
        self.listProd_5.setAlternatingRowColors(True)
        self.listProd_5.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listProd_5.setObjectName("listProd_5")
        self.label_48 = QtWidgets.QLabel(self.page_2)
        self.label_48.setGeometry(QtCore.QRect(510, 50, 181, 31))
        self.label_48.setText("")
        self.label_48.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_48.setObjectName("label_48")
        self.comboBox_3 = QtWidgets.QComboBox(self.page_2)
        self.comboBox_3.setGeometry(QtCore.QRect(70, 30, 191, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.setItemText(0, "")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_57 = QtWidgets.QLabel(self.page_2)
        self.label_57.setGeometry(QtCore.QRect(20, 30, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_57.setFont(font)
        self.label_57.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_57.setObjectName("label_57")
        self.label_58 = QtWidgets.QLabel(self.page_2)
        self.label_58.setGeometry(QtCore.QRect(380, 80, 121, 121))
        self.label_58.setStyleSheet("")
        self.label_58.setText("")
        self.label_58.setPixmap(QtGui.QPixmap("img/Taco.png"))
        self.label_58.setScaledContents(True)
        self.label_58.setObjectName("label_58")
        self.label_59 = QtWidgets.QLabel(self.page_2)
        self.label_59.setGeometry(QtCore.QRect(290, 230, 111, 16))
        self.label_59.setObjectName("label_59")
        self.label_60 = QtWidgets.QLabel(self.page_2)
        self.label_60.setGeometry(QtCore.QRect(290, 260, 111, 16))
        self.label_60.setObjectName("label_60")
        self.label_44 = QtWidgets.QLabel(self.page_2)
        self.label_44.setGeometry(QtCore.QRect(290, 320, 111, 21))
        self.label_44.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_44.setObjectName("label_44")
        self.label_61 = QtWidgets.QLabel(self.page_2)
        self.label_61.setGeometry(QtCore.QRect(290, 290, 111, 21))
        self.label_61.setObjectName("label_61")
        self.label_62 = QtWidgets.QLabel(self.page_2)
        self.label_62.setGeometry(QtCore.QRect(380, 230, 201, 20))
        self.label_62.setText("")
        self.label_62.setObjectName("label_62")
        self.label_63 = QtWidgets.QLabel(self.page_2)
        self.label_63.setGeometry(QtCore.QRect(380, 260, 201, 20))
        self.label_63.setText("")
        self.label_63.setObjectName("label_63")
        self.label_64 = QtWidgets.QLabel(self.page_2)
        self.label_64.setGeometry(QtCore.QRect(380, 290, 201, 20))
        self.label_64.setText("")
        self.label_64.setObjectName("label_64")
        self.pushButton_19 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_19.setGeometry(QtCore.QRect(390, 420, 131, 31))
        self.pushButton_19.setObjectName("pushButton_19")
        self.label = QtWidgets.QLabel(self.page_2)
        self.label.setGeometry(QtCore.QRect(380, 320, 201, 51))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_45 = QtWidgets.QLabel(self.page_2)
        self.label_45.setGeometry(QtCore.QRect(290, 390, 111, 21))
        self.label_45.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_45.setObjectName("label_45")
        self.label_65 = QtWidgets.QLabel(self.page_2)
        self.label_65.setGeometry(QtCore.QRect(620, 410, 51, 21))
        self.label_65.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_65.setObjectName("label_65")
        self.label_67 = QtWidgets.QLabel(self.page_2)
        self.label_67.setGeometry(QtCore.QRect(610, 10, 251, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_67.setFont(font)
        self.label_67.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_67.setObjectName("label_67")
        self.label_68 = QtWidgets.QLabel(self.page_2)
        self.label_68.setGeometry(QtCore.QRect(560, 130, 21, 21))
        self.label_68.setStyleSheet("")
        self.label_68.setText("")
        self.label_68.setPixmap(QtGui.QPixmap("img/Arrow_Right.png"))
        self.label_68.setScaledContents(True)
        self.label_68.setObjectName("label_68")
        self.label_69 = QtWidgets.QLabel(self.page_2)
        self.label_69.setGeometry(QtCore.QRect(300, 130, 21, 21))
        self.label_69.setStyleSheet("")
        self.label_69.setText("")
        self.label_69.setPixmap(QtGui.QPixmap("img/Arrow_Right.png"))
        self.label_69.setScaledContents(True)
        self.label_69.setObjectName("label_69")
        self.spinCant = QtWidgets.QSpinBox(self.page_2)
        self.spinCant.setGeometry(QtCore.QRect(380, 380, 201, 31))
        self.spinCant.setAlignment(QtCore.Qt.AlignCenter)
        self.spinCant.setMaximum(10000000)
        self.spinCant.setObjectName("spinCant")
        self.spinCant_3 = QtWidgets.QSpinBox(self.page_2)
        self.spinCant_3.setEnabled(True)
        self.spinCant_3.setGeometry(QtCore.QRect(680, 410, 151, 20))
        self.spinCant_3.setFrame(True)
        self.spinCant_3.setAlignment(QtCore.Qt.AlignCenter)
        self.spinCant_3.setReadOnly(True)
        self.spinCant_3.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinCant_3.setMaximum(10000000)
        self.spinCant_3.setObjectName("spinCant_3")
        self.pushButton_26 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_26.setGeometry(QtCore.QRect(590, 440, 71, 31))
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_27 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_27.setGeometry(QtCore.QRect(260, 30, 31, 21))
        self.pushButton_27.setObjectName("pushButton_27")
        self.label_66 = QtWidgets.QLabel(self.page_2)
        self.label_66.setGeometry(QtCore.QRect(10, 0, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_66.setFont(font)
        self.label_66.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_66.setObjectName("label_66")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_52 = QtWidgets.QLabel(self.page_3)
        self.label_52.setGeometry(QtCore.QRect(20, 60, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_52.setFont(font)
        self.label_52.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_52.setObjectName("label_52")
        self.label_40 = QtWidgets.QLabel(self.page_3)
        self.label_40.setGeometry(QtCore.QRect(20, 10, 851, 41))
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.listProd_4 = QtWidgets.QListWidget(self.page_3)
        self.listProd_4.setGeometry(QtCore.QRect(20, 90, 281, 351))
        font = QtGui.QFont()
        font.setFamily("Prototype")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.listProd_4.setFont(font)
        self.listProd_4.setStyleSheet("")
        self.listProd_4.setAlternatingRowColors(True)
        self.listProd_4.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listProd_4.setObjectName("listProd_4")
        self.pushButton_21 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_21.setGeometry(QtCore.QRect(440, 420, 321, 31))
        self.pushButton_21.setObjectName("pushButton_21")
        self.label_70 = QtWidgets.QLabel(self.page_3)
        self.label_70.setGeometry(QtCore.QRect(90, 450, 111, 21))
        self.label_70.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_70.setObjectName("label_70")
        self.label_71 = QtWidgets.QLabel(self.page_3)
        self.label_71.setGeometry(QtCore.QRect(30, 450, 51, 21))
        self.label_71.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_71.setObjectName("label_71")
        self.line = QtWidgets.QFrame(self.page_3)
        self.line.setGeometry(QtCore.QRect(320, 60, 20, 421))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_53 = QtWidgets.QLabel(self.page_3)
        self.label_53.setGeometry(QtCore.QRect(350, 110, 511, 71))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_53.setFont(font)
        self.label_53.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_53.setWordWrap(True)
        self.label_53.setObjectName("label_53")
        self.label_54 = QtWidgets.QLabel(self.page_3)
        self.label_54.setGeometry(QtCore.QRect(340, 70, 531, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_54.setFont(font)
        self.label_54.setAlignment(QtCore.Qt.AlignCenter)
        self.label_54.setObjectName("label_54")
        self.label_72 = QtWidgets.QLabel(self.page_3)
        self.label_72.setGeometry(QtCore.QRect(520, 190, 161, 161))
        self.label_72.setStyleSheet("")
        self.label_72.setText("")
        self.label_72.setScaledContents(True)
        self.label_72.setObjectName("label_72")
        self.pushButton_24 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_24.setGeometry(QtCore.QRect(560, 360, 91, 31))
        self.pushButton_24.setObjectName("pushButton_24")
        self.label_75 = QtWidgets.QLabel(self.page_3)
        self.label_75.setGeometry(QtCore.QRect(10, 10, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_75.setFont(font)
        self.label_75.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_75.setObjectName("label_75")
        self.stackedWidget.addWidget(self.page_3)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_73 = QtWidgets.QLabel(self.page)
        self.label_73.setGeometry(QtCore.QRect(140, 60, 161, 31))
        self.label_73.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_73.setObjectName("label_73")
        self.label_74 = QtWidgets.QLabel(self.page)
        self.label_74.setGeometry(QtCore.QRect(20, 60, 111, 31))
        self.label_74.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_74.setObjectName("label_74")
        self.listProd_6 = QtWidgets.QListWidget(self.page)
        self.listProd_6.setGeometry(QtCore.QRect(20, 120, 291, 351))
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
        self.label_55 = QtWidgets.QLabel(self.page)
        self.label_55.setGeometry(QtCore.QRect(20, 90, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_55.setFont(font)
        self.label_55.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_55.setObjectName("label_55")
        self.label_10 = QtWidgets.QLabel(self.page)
        self.label_10.setGeometry(QtCore.QRect(0, 20, 881, 31))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.page)
        self.label_11.setGeometry(QtCore.QRect(350, 120, 111, 16))
        self.label_11.setObjectName("label_11")
        self.label_13 = QtWidgets.QLabel(self.page)
        self.label_13.setGeometry(QtCore.QRect(350, 240, 111, 16))
        self.label_13.setObjectName("label_13")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_6.setGeometry(QtCore.QRect(500, 200, 361, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_18 = QtWidgets.QLabel(self.page)
        self.label_18.setGeometry(QtCore.QRect(350, 200, 171, 16))
        self.label_18.setObjectName("label_18")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_11.setGeometry(QtCore.QRect(500, 240, 361, 20))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.comboBox_4 = QtWidgets.QComboBox(self.page)
        self.comboBox_4.setGeometry(QtCore.QRect(500, 160, 361, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.setItemText(0, "")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_2.setGeometry(QtCore.QRect(500, 120, 361, 20))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_17 = QtWidgets.QLabel(self.page)
        self.label_17.setGeometry(QtCore.QRect(350, 160, 141, 21))
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_17.setObjectName("label_17")
        self.label_19 = QtWidgets.QLabel(self.page)
        self.label_19.setGeometry(QtCore.QRect(350, 280, 121, 21))
        self.label_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_19.setObjectName("label_19")
        self.comboBox_5 = QtWidgets.QComboBox(self.page)
        self.comboBox_5.setGeometry(QtCore.QRect(500, 280, 361, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.setItemText(0, "")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.label_20 = QtWidgets.QLabel(self.page)
        self.label_20.setGeometry(QtCore.QRect(350, 320, 141, 21))
        self.label_20.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.page)
        self.label_21.setGeometry(QtCore.QRect(350, 360, 111, 21))
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_21.setObjectName("label_21")
        self.pushButton_23 = QtWidgets.QPushButton(self.page)
        self.pushButton_23.setGeometry(QtCore.QRect(420, 420, 151, 31))
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_25 = QtWidgets.QPushButton(self.page)
        self.pushButton_25.setGeometry(QtCore.QRect(650, 420, 151, 31))
        self.pushButton_25.setObjectName("pushButton_25")
        self.line_2 = QtWidgets.QFrame(self.page)
        self.line_2.setGeometry(QtCore.QRect(320, 100, 20, 381))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_22 = QtWidgets.QLabel(self.page)
        self.label_22.setGeometry(QtCore.QRect(500, 360, 361, 21))
        self.label_22.setText("")
        self.label_22.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_22.setObjectName("label_22")
        self.label_56 = QtWidgets.QLabel(self.page)
        self.label_56.setGeometry(QtCore.QRect(550, 70, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_56.setFont(font)
        self.label_56.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_56.setObjectName("label_56")
        self.spinCant_2 = QtWidgets.QSpinBox(self.page)
        self.spinCant_2.setGeometry(QtCore.QRect(500, 320, 361, 21))
        self.spinCant_2.setMaximum(10000000)
        self.spinCant_2.setObjectName("spinCant_2")
        self.label_76 = QtWidgets.QLabel(self.page)
        self.label_76.setGeometry(QtCore.QRect(10, 10, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_76.setFont(font)
        self.label_76.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_76.setObjectName("label_76")
        self.pushButton_28 = QtWidgets.QPushButton(self.page)
        self.pushButton_28.setGeometry(QtCore.QRect(790, 350, 71, 31))
        self.pushButton_28.setObjectName("pushButton_28")
        self.stackedWidget.addWidget(self.page)
        VentanaPrincipalCliente.setCentralWidget(self.centralwidget)
        self.actionSalir = QtWidgets.QAction(VentanaPrincipalCliente)
        self.actionSalir.setObjectName("actionSalir")

        self.retranslateUi(VentanaPrincipalCliente)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(VentanaPrincipalCliente)

    def retranslateUi(self, VentanaPrincipalCliente):
        _translate = QtCore.QCoreApplication.translate
        VentanaPrincipalCliente.setWindowTitle(_translate("VentanaPrincipalCliente", "RestauranTEC Principal Worker"))
        self.pushButton_22.setText(_translate("VentanaPrincipalCliente", "Vaciar"))
        self.pushButton_20.setText(_translate("VentanaPrincipalCliente", "Realizar Pedido"))
        self.label_47.setText(_translate("VentanaPrincipalCliente", "Producto Seleccionado"))
        self.label_9.setText(_translate("VentanaPrincipalCliente", "Mesa #X"))
        self.label_46.setText(_translate("VentanaPrincipalCliente", "Lista de Platos"))
        self.listProd_5.setSortingEnabled(True)
        self.comboBox_3.setItemText(1, _translate("VentanaPrincipalCliente", "BEBIDA"))
        self.comboBox_3.setItemText(2, _translate("VentanaPrincipalCliente", "PRINCIPAL"))
        self.comboBox_3.setItemText(3, _translate("VentanaPrincipalCliente", "ENTRADA"))
        self.label_57.setText(_translate("VentanaPrincipalCliente", "Filtro:"))
        self.label_59.setText(_translate("VentanaPrincipalCliente", "Nombre"))
        self.label_60.setText(_translate("VentanaPrincipalCliente", "Precio"))
        self.label_44.setText(_translate("VentanaPrincipalCliente", "Descripcion"))
        self.label_61.setText(_translate("VentanaPrincipalCliente", "Tipo"))
        self.pushButton_19.setText(_translate("VentanaPrincipalCliente", "Añádir Plato"))
        self.label.setText(_translate("VentanaPrincipalCliente", "<html><head/><body><p><br/></p></body></html>"))
        self.label_45.setText(_translate("VentanaPrincipalCliente", "Cantidad"))
        self.label_65.setText(_translate("VentanaPrincipalCliente", "Total"))
        self.label_67.setText(_translate("VentanaPrincipalCliente", "Pedido del Cliente"))
        self.pushButton_26.setText(_translate("VentanaPrincipalCliente", "Eliminar"))
        self.pushButton_27.setText(_translate("VentanaPrincipalCliente", "Go"))
        self.label_66.setText(_translate("VentanaPrincipalCliente", "1"))
        self.label_52.setText(_translate("VentanaPrincipalCliente", "Pedidos del Cliente"))
        self.label_40.setText(_translate("VentanaPrincipalCliente", "Restaurante \"XXXXX\""))
        self.listProd_4.setSortingEnabled(True)
        self.pushButton_21.setText(_translate("VentanaPrincipalCliente", "Confirmar que el Pedido fue Recibido"))
        self.label_70.setText(_translate("VentanaPrincipalCliente", "0"))
        self.label_71.setText(_translate("VentanaPrincipalCliente", "Total"))
        self.label_53.setText(_translate("VentanaPrincipalCliente", "Pedidos del Cliente"))
        self.label_54.setText(_translate("VentanaPrincipalCliente", "Estado del Pedido"))
        self.pushButton_24.setText(_translate("VentanaPrincipalCliente", "Refresh"))
        self.label_75.setText(_translate("VentanaPrincipalCliente", "1"))
        self.label_73.setText(_translate("VentanaPrincipalCliente", "0"))
        self.label_74.setText(_translate("VentanaPrincipalCliente", "Total a Pagar"))
        self.label_55.setText(_translate("VentanaPrincipalCliente", "Productos Comprados"))
        self.label_10.setText(_translate("VentanaPrincipalCliente", "Pago del Pedido"))
        self.label_11.setText(_translate("VentanaPrincipalCliente", "Nombre"))
        self.label_13.setText(_translate("VentanaPrincipalCliente", "Telefono"))
        self.label_18.setText(_translate("VentanaPrincipalCliente", "Numero Documento"))
        self.comboBox_4.setItemText(1, _translate("VentanaPrincipalCliente", "Cedula Ciudadania"))
        self.comboBox_4.setItemText(2, _translate("VentanaPrincipalCliente", "Cedula Extrangeria"))
        self.comboBox_4.setItemText(3, _translate("VentanaPrincipalCliente", "NIT"))
        self.label_17.setText(_translate("VentanaPrincipalCliente", "Tipo de Documento"))
        self.label_19.setText(_translate("VentanaPrincipalCliente", "Metodo de Pago"))
        self.comboBox_5.setItemText(1, _translate("VentanaPrincipalCliente", "Efectivo"))
        self.comboBox_5.setItemText(2, _translate("VentanaPrincipalCliente", "Tarjeta"))
        self.label_20.setText(_translate("VentanaPrincipalCliente", "Cantidad Pagada"))
        self.label_21.setText(_translate("VentanaPrincipalCliente", "Cambio"))
        self.pushButton_23.setText(_translate("VentanaPrincipalCliente", "Vaciar Formulario"))
        self.pushButton_25.setText(_translate("VentanaPrincipalCliente", "Confirmar Pago"))
        self.label_56.setText(_translate("VentanaPrincipalCliente", "Datos de Facturacion"))
        self.label_76.setText(_translate("VentanaPrincipalCliente", "1"))
        self.pushButton_28.setText(_translate("VentanaPrincipalCliente", "Calcular"))
        self.actionSalir.setText(_translate("VentanaPrincipalCliente", "Salir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaPrincipalCliente = QtWidgets.QMainWindow()
    ui = Ui_VentanaPrincipalCliente()
    ui.setupUi(VentanaPrincipalCliente)
    VentanaPrincipalCliente.show()
    sys.exit(app.exec_())
