# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VentanaPrincipalAdmin(object):
    def setupUi(self, VentanaPrincipalAdmin):
        VentanaPrincipalAdmin.setObjectName("VentanaPrincipalAdmin")
        VentanaPrincipalAdmin.resize(899, 511)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/LogoApp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        VentanaPrincipalAdmin.setWindowIcon(icon)
        VentanaPrincipalAdmin.setStyleSheet("QWidget{\n"
"    font-size: 18px;\n"
"}\n"
"QWidget#centralwidget{\n"
"    background-color: \n"
"        qlineargradient(spread:pad, x1:0.181, y1:0, x2:0.858, y2:0, stop:0#fbe6c2, stop:0.511364 #F9E7E7, stop:1 #fbe6c2);\n"
"}\n"
"\n"
"QFrame#frame_1{\n"
"    background-color:rgb(255, 157, 77, 200) ;\n"
"}\n"
"\n"
"QLabel{\n"
"    background-color:rgba(0, 0, 0, 0);\n"
"}  \n"
"")
        self.centralwidget = QtWidgets.QWidget(VentanaPrincipalAdmin)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_1 = QtWidgets.QFrame(self.centralwidget)
        self.frame_1.setGeometry(QtCore.QRect(0, 0, 901, 71))
        self.frame_1.setStyleSheet("QLabel{\n"
"    background-color:rgba(0, 0, 0, 0);\n"
"    color: rgb(255, 232, 99);\n"
"}  ")
        self.frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1.setObjectName("frame_1")
        self.label = QtWidgets.QLabel(self.frame_1)
        self.label.setGeometry(QtCore.QRect(380, 10, 141, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_1)
        self.label_2.setGeometry(QtCore.QRect(110, 10, 261, 41))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.frame_1)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 71, 71))
        self.label_4.setStyleSheet("background-color: rgb(255, 232, 99);")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 480, 101, 16))
        self.label_3.setObjectName("label_3")
        VentanaPrincipalAdmin.setCentralWidget(self.centralwidget)
        self.actionSalir = QtWidgets.QAction(VentanaPrincipalAdmin)
        self.actionSalir.setObjectName("actionSalir")

        self.retranslateUi(VentanaPrincipalAdmin)
        QtCore.QMetaObject.connectSlotsByName(VentanaPrincipalAdmin)

    def retranslateUi(self, VentanaPrincipalAdmin):
        _translate = QtCore.QCoreApplication.translate
        VentanaPrincipalAdmin.setWindowTitle(_translate("VentanaPrincipalAdmin", "RestauranTEC Principal"))
        self.label.setText(_translate("VentanaPrincipalAdmin", "Rol"))
        self.label_2.setText(_translate("VentanaPrincipalAdmin", "Usuario"))
        self.label_4.setText(_translate("VentanaPrincipalAdmin", "ggg"))
        self.label_3.setText(_translate("VentanaPrincipalAdmin", "Hora:"))
        self.actionSalir.setText(_translate("VentanaPrincipalAdmin", "Salir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaPrincipalAdmin = QtWidgets.QMainWindow()
    ui = Ui_VentanaPrincipalAdmin()
    ui.setupUi(VentanaPrincipalAdmin)
    VentanaPrincipalAdmin.show()
    sys.exit(app.exec_())
