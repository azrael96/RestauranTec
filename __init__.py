import sys
import mysql.connector

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QTableWidgetItem
from RestauranTec.VentanaInicio import Ui_VentanaInicio
from RestauranTec.VentanaPrincipal import Ui_VentanaPrincipalAdmin

conexionexitosa = ""
inicio = False

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="deathangel96",
        database="restaurantec"
    )
    mycursor = db.cursor()
    conexionexitosa = "Conectado a la BD correctamente"
except:
  conexionexitosa = "Error de conexion a BD"

class FormLogin(QtWidgets.QMainWindow, Ui_VentanaInicio):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

class FormAdmin(QtWidgets.QMainWindow, Ui_VentanaPrincipalAdmin):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

    def updateTime(self):
        time = QTime.currentTime().toString()
        self.label_3.setText("Hora: " + time)
        return time

def generarMain():
    def validar(user, passw):
        def cleanMain():
            global main
            main.TextUser.setText("")
            main.TextPass.setText("")

        mycursor.execute("SELECT Nick_Seg, Clav_Seg, Rol_Seg, Est_Seg FROM seguridad WHERE Nick_Seg='" + user + "'")
        valores = mycursor.fetchall()

        if user != "" and passw != "":
            if len(valores) != 0:
                for val in valores:
                    if val[3] < 3:
                        if val[1] == passw:
                            mycursor.execute(
                                "UPDATE seguridad SET Est_Seg=" + str(0) + " WHERE Nick_Seg='" + user + "'")
                            db.commit()
                            generarPrincipal(val[2], val[0])
                        else:
                            i = str(val[3] + 1)

                            if val[3] + 1 == 2:
                                QMessageBox.warning(main, "Cuidado", "Si scribe la contraseña erronea una vez mas "
                                                                     "\nSe bloqueara el Usuario")
                                cleanMain()

                            QMessageBox.critical(main, "Error", "Datos Incorrectos")
                            mycursor.execute("UPDATE seguridad SET Est_Seg=" + i + " WHERE Nick_Seg='" + user + "'")
                            db.commit()
                            cleanMain()
                    else:
                        QMessageBox.information(main, "Cuidado", "El usuario ha sido bloqueado "
                                                                 "\n Contacte el Administrador para desbloquearlo")
                        cleanMain()
            else:
                QMessageBox.information(main, "Error", "Datos Incorrectos")
                cleanMain()
        else:
            QMessageBox.information(main, "Error", "Complete todos los campos")
            cleanMain()

    global main
    global principal
    main = FormLogin()
    main.ButtStart.clicked.connect(lambda: validar(main.TextUser.text(), main.TextPass.text()))
    main.label_3.setText(conexionexitosa)
    main.show()

def generarPrincipal(rol, nick):
    def setTimer():
        global timer
        timer.timeout.connect(principal.updateTime)
        timer.start(1000)

    global main
    global principal
    principal = FormAdmin()
    principal.show()
    main.destroy()

    principal.label.setText(rol)
    principal.label_2.setText(nick)
    setTimer()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = None
    principal = None
    generarMain()
    timer = QTimer()
    sys.exit(app.exec_())
