import Conector as Conexion
import messages as Mail
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTime
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QTableWidgetItem
from VentanaInicio import Ui_VentanaInicio
from VentanaAdmin import Ui_VentanaPrincipalAdmin
from VentanaWorker import Ui_VentanaPrincipalWorker
from VentanaCliente import Ui_VentanaPrincipalCliente
from PyQt5.QtCore import QTimer
from datetime import datetime, date
import sys

timer = QTimer()
main = None
principal = None
principalCliente = None

class FormLogin(QtWidgets.QMainWindow, Ui_VentanaInicio):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

class FormPrincipal(QtWidgets.QMainWindow):
    def __init__(self):
        pass

    def updateTime(self):
        time = QTime.currentTime().toString()
        self.label_3.setText("Hora: " + time)
        return time

class FormAdmin(Ui_VentanaPrincipalAdmin, FormPrincipal):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

class FormWorker(Ui_VentanaPrincipalWorker, FormPrincipal):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

class FormCliente(Ui_VentanaPrincipalCliente, FormPrincipal):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

def generarMain():
    def validar(nick, passw):
        def cleanMain():
            main.TextUser.setText("")
            main.TextPass.setText("")
        valores = Conexion.SearchUser(nick)
        if nick != "" and passw != "":
            if len(valores) != 0:
                for val in valores:
                    if val[3] < 3:
                        if val[1] == passw:
                            Conexion.UpdateLoginSuccess(nick)
                            generarPrincipal(val[4], val[2])
                        else:
                            i = str(val[3] + 1)
                            if val[3] + 1 == 2:
                                QMessageBox.warning(main, "Cuidado", Mail.m1)
                                cleanMain()
                            QMessageBox.critical(main, "Error", Mail.m2)
                            Conexion.UpdateLoginFail(nick, i)
                            cleanMain()
                    else:
                        QMessageBox.information(main, "Cuidado", Mail.m3)
                        cleanMain()
            else:
                QMessageBox.information(main, "Error", Mail.m2)
                cleanMain()
        else:
            QMessageBox.information(main, "Error", Mail.m4)
            cleanMain()
    global main
    main = FormLogin()
    main.ButtStart.clicked.connect(lambda: validar(main.TextUser.text(), main.TextPass.text()))
    main.LabConexion.setText(Conexion.ConexionStatus())
    main.show()

def generarPrincipal(cod, rol):
    def destroyW():
        principal.destroy()

    def iniciar():
        weEditNotAdd = False
        weEditNotAdd2 = False

        def add():
            clean()
            switch(True)
            nonlocal weEditNotAdd
            weEditNotAdd = False
        def edit():
            row = principal.listProd.currentRow()
            if row != -1:
                switch(True)
                nonlocal weEditNotAdd
                weEditNotAdd = True
            else:
                QMessageBox.information(principal, "Error", Mail.m15)
        def save():
            def trans(valor):
                r = "error"
                if valor == "ACTIVO":
                        r = 0
                if valor == "EN PELIGRO":
                        r = 2
                if valor == "BLOQUEADO":
                        r = 3
                return r
            nom = principal.lineEdit.text()
            ape1 = principal.lineEdit_2.text()
            ape2 = principal.lineEdit_3.text()
            tDoc = principal.comboBox_3.currentText()
            nDoc = principal.lineEdit_6.text()
            Dir = principal.lineEdit_5.text()
            Usu = principal.lineEdit_4.text()
            pas = principal.lineEdit_12.text()
            est = principal.comboBox_2.currentText()
            rol = principal.comboBox.currentText()
            cor = principal.lineEdit_10.text()
            tel = principal.lineEdit_11.text()
            if nom != "" and ape1 != "" and ape2 != "" and tDoc != "" and nDoc != "" and Dir != "" \
                    and Usu != "" and pas != "" and est != "" and rol != "" and cor != "" and tel != "" :
                if weEditNotAdd == True:
                    item = principal.listProd.currentItem().text()
                    values = Conexion.selectNickAlone(item)
                    val = values[0]
                    Conexion.updateUsu(item, nom, ape1, ape2, tel, Dir, tDoc, nDoc, cor, Usu, pas, rol, trans(est), val)
                    clean()
                    switch(False)
                    filltable()
                else:
                    cod = Conexion.actualUser()+1
                    Conexion.addUser(nom, ape1, ape2, tel, Dir, tDoc, nDoc, cor, Usu, pas, rol, 0, cod)
                    clean()
                    switch(False)
                    filltable()
            else:
                QMessageBox.information(principal, "Error", Mail.m14)
        def delete():
            row = principal.listProd.currentRow()
            if row != -1:
                item = principal.listProd.currentItem().text()
                values = Conexion.selectNickAlone(item)
                val = values[0]
                Conexion.deleteUsu(str(val))
                QMessageBox.information(principal, "Eliminado", "El usuario '" + str(val) + "' ha sido eliminado")
                filltable()
                clean()
            else:
                QMessageBox.information(principal, "Error", Mail.m15)
        def cancel():
            switch(False)
            clean()
            filltable()
        def setTimer():
            global timer
            timer.timeout.connect(principal.updateTime)
            timer.start(1000)
        def setPrincipal(rol):
            values = Conexion.DataUser(cod)
            for val in values:
                principal.label_2.setText(val[0] + " " + val[1])
            principal.label.setText(rol)
            principal.label_41.setText(Mail.m5)
        def changeWidget(i):
            principal.stackedWidget.setCurrentIndex(i)
        def clicSet():
            def trans(valor):
                r = "error"
                if valor == 1 or valor == 0:
                        r = "ACTIVO"
                if valor == 2:
                        r = "EN PELIGRO"
                if valor == 3:
                        r = "BLOQUEADO"
                return r
            item = principal.listProd.currentItem().text()
            values = Conexion.selectNick(item)
            principal.lineEdit_4.setText(values[0])
            principal.lineEdit_12.setText(values[1])
            principal.comboBox.setCurrentIndex(principal.comboBox.findText(str(values[2])))
            combo = principal.comboBox_2.findText(trans(values[3]))
            principal.comboBox_2.setCurrentIndex(combo)
            val = values[4]
            values = Conexion.selectUsu(val)
            principal.lineEdit.setText(values[0])
            principal.lineEdit_2.setText(values[1])
            principal.lineEdit_3.setText(values[2])
            principal.lineEdit_11.setText(values[3])
            principal.lineEdit_5.setText(values[4])
            principal.comboBox_3.setCurrentIndex(principal.comboBox_3.findText(values[5]))
            principal.lineEdit_6.setText(str(values[6]))
            principal.lineEdit_10.setText(values[7])
        def filltable():
            principal.listProd.clear()
            values = Conexion.listUsu()
            for row in values:
                principal.listProd.addItem(row[0])
        def clean():
            principal.lineEdit_4.setText("")
            principal.lineEdit_12.setText("")
            principal.comboBox.setCurrentIndex(0)
            principal.comboBox_2.setCurrentIndex(0)
            principal.lineEdit.setText("")
            principal.lineEdit_2.setText("")
            principal.lineEdit_3.setText("")
            principal.lineEdit_11.setText("")
            principal.lineEdit_5.setText("")
            principal.comboBox_3.setCurrentIndex(0)
            principal.lineEdit_6.setText("")
            principal.lineEdit_10.setText("")
            filltable()
        def switch(val):
            principal.lineEdit_4.setEnabled(val)
            principal.lineEdit_12.setEnabled(val)
            principal.comboBox.setEnabled(val)
            principal.comboBox_2.setEnabled(val)
            principal.lineEdit.setEnabled(val)
            principal.lineEdit_2.setEnabled(val)
            principal.lineEdit_3.setEnabled(val)
            principal.lineEdit_11.setEnabled(val)
            principal.lineEdit_5.setEnabled(val)
            principal.comboBox_3.setEnabled(val)
            principal.lineEdit_6.setEnabled(val)
            principal.lineEdit_10.setEnabled(val)
            principal.pushButton_6.setEnabled(val)
            principal.pushButton_7.setEnabled(val)
            principal.pushButton_8.setEnabled(val)
            principal.pushButton_9.setEnabled(not val)
            principal.pushButton_10.setEnabled(not val)
            principal.pushButton_11.setEnabled(not val)
            principal.listProd.setEnabled(not val)
        def add2():
            clean2()
            switch2(True)
            nonlocal weEditNotAdd2
            weEditNotAdd2 = False
        def edit2():
            row = principal.listProd_3.currentRow()
            if row != -1:
                switch2(True)
                nonlocal weEditNotAdd2
                weEditNotAdd2 = True
            else:
                QMessageBox.information(principal, "Error", Mail.m16)
        def save2():
            nom = principal.lineEdit_25.text()
            prec = principal.lineEdit_19.text()
            tipo = principal.comboBox_9.currentText()
            desc = principal.textEdit.toPlainText()
            if nom != "" and prec != "" and tipo != "" and desc != "":
                if weEditNotAdd2 == True:
                    item = principal.listProd_3.currentItem().text()
                    Conexion.updatePlato(item, nom, prec, desc, tipo)
                    clean2()
                    switch2(False)
                    filltable2()
                else:
                    Conexion.addPlato(nom, prec, desc, tipo)
                    clean2()
                    switch2(False)
                    filltable2()
            else:
                QMessageBox.information(principal, "Error", Mail.m14)
        def delete2():
            row = principal.listProd_3.currentRow()
            if row != -1:
                item = principal.listProd_3.currentItem().text()
                Conexion.deletePlato(item)
                QMessageBox.information(principal, "Eliminado", "El usuario '" + str(item) + "' ha sido eliminado")
                filltable2()
                clean2()
            else:
                QMessageBox.information(principal, "Error", Mail.m15)
        def cancel2():
            switch2(False)
            clean2()
            filltable2()
        def clicSet2():
            item = principal.listProd_3.currentItem().text()
            values = Conexion.selectPlato(item)
            principal.lineEdit_25.setText(values[0])
            principal.lineEdit_19.setText(str(values[1]))
            combo = principal.comboBox_9.findText(str(values[3]))
            principal.comboBox_9.setCurrentIndex(combo)
            principal.textEdit.setText(values[2])
        def filltable2():
            principal.listProd_3.clear()
            values = Conexion.listPlato()
            for row in values:
                principal.listProd_3.addItem(row[0])
        def clean2():
            principal.lineEdit_25.setText("")
            principal.lineEdit_19.setText("")
            principal.comboBox_9.setCurrentIndex(0)
            principal.textEdit.setText("")
            filltable2()
        def switch2(val):
            principal.lineEdit_25.setEnabled(val)
            principal.lineEdit_19.setEnabled(val)
            principal.comboBox_9.setEnabled(val)
            principal.textEdit.setEnabled(val)
            principal.pushButton_20.setEnabled(val)
            principal.pushButton_22.setEnabled(val)
            principal.pushButton_23.setEnabled(val)
            principal.pushButton_19.setEnabled(not val)
            principal.pushButton_18.setEnabled(not val)
            principal.pushButton_21.setEnabled(not val)
            principal.listProd_3.setEnabled(not val)
        def filltablesEnvio():
            principal.listProd_3.clear()
            principal.listProd_4.clear()
            values = Conexion.listOrdenCocina()
            for row in values:
                principal.listProd_3.addItem(str(row[0]))
            values = Conexion.listOrdenEnvio()
            for row in values:
                principal.listProd_4.addItem(str(row[0]))
        def clicSetcocina():
            item = principal.listProd_3.currentItem().text()
            values = Conexion.selectEnPedido(item)
            principal.listProd_5.clear()
            for x in values:
                principal.listProd_5.addItem(str(x))
        def clicSetmesero():
            item = principal.listProd_4.currentItem().text()
            values = Conexion.selectEnPedido(item)
            principal.listProd_6.clear()
            for x in values:
                principal.listProd_6.addItem(str(x))
        def changeEst(menu, boton):
            menus = None
            opcion = ""
            if menu == "COCINA":
                menus = principal.listProd_3
                if boton == "GREEN":
                    opcion = "EN ENVIO"
                if boton == "RED":
                    opcion = "RECHAZADO"
            if menu == "MESERO":
                menus = principal.listProd_4
                if boton == "GREEN":
                    opcion = "ENTREGADO"
                if boton == "RED":
                    opcion = "EN COCINA"
            row = menus.currentRow()
            if row != -1:
                item = menus.currentItem().text()
                Conexion.updateOrden(item, opcion)

                QMessageBox.information(principal, "Exito", Mail.m18)
                filltablesEnvio()
                principal.listProd_5.clear()
                principal.listProd_6.clear()
            else:
                QMessageBox.information(principal, "Error", Mail.m17)
        def clicSet3():
            item = principal.listProd_4.currentItem().text()
            values = Conexion.selectFactura(item)
            principal.label_53.setText(values)
            pass
        def filltable3():
            principal.listProd_4.clear()
            values = Conexion.listFactura()
            for row in values:
                principal.listProd_4.addItem(str(row[0]))
        def mss():
            QMessageBox.information(principal, "Error", Mail.m19)

        global principal
        if rol == "ADMON":
            principal = FormAdmin()
            setPrincipal("Administrador")
            principal.pushButton.clicked.connect(lambda: changeWidget(1))
            principal.pushButton_2.clicked.connect(lambda: changeWidget(2))
            principal.pushButton_3.clicked.connect(lambda: changeWidget(3))
            principal.pushButton_5.clicked.connect(lambda: generarCliente())
            filltable()
            switch(False)
            principal.listProd.itemClicked.connect(lambda: clicSet())
            principal.pushButton_7.clicked.connect(lambda: clean())
            principal.pushButton_6.clicked.connect(lambda: cancel())
            principal.pushButton_9.clicked.connect(lambda: edit())
            principal.pushButton_10.clicked.connect(lambda: delete())
            principal.pushButton_11.clicked.connect(lambda: add())
            principal.pushButton_8.clicked.connect(lambda: save())
            filltable2()
            switch2(False)
            principal.listProd_3.itemClicked.connect(lambda: clicSet2())
            principal.pushButton_23.clicked.connect(lambda: clean2())
            principal.pushButton_22.clicked.connect(lambda: cancel2())
            principal.pushButton_21.clicked.connect(lambda: edit2())
            principal.pushButton_18.clicked.connect(lambda: delete2())
            principal.pushButton_19.clicked.connect(lambda: add2())
            principal.pushButton_20.clicked.connect(lambda: save2())

            filltable3()
            principal.listProd_4.itemClicked.connect(lambda: clicSet3())

        if rol == "WORKER":
            principal = FormWorker()
            setPrincipal("Trabajador")
            filltablesEnvio()
            principal.pushButton.clicked.connect(lambda: changeWidget(2))
            principal.pushButton_2.clicked.connect(lambda: changeWidget(1))
            principal.listProd_3.itemClicked.connect(lambda: clicSetcocina())
            principal.listProd_4.itemClicked.connect(lambda: clicSetmesero())
            principal.pushButton_20.clicked.connect(lambda: changeEst("COCINA", "GREEN"))
            principal.pushButton_22.clicked.connect(lambda: changeEst("COCINA", "RED"))
            principal.pushButton_21.clicked.connect(lambda: changeEst("MESERO", "GREEN"))
            principal.pushButton_23.clicked.connect(lambda: changeEst("MESERO", "RED"))
        changeWidget(0)
        principal.pushButton_4.clicked.connect(lambda: destroyW())
        setTimer()

    global main, principal
    iniciar()
    principal.show()
    main.destroy()

def generarCliente():
    global principalCliente
    principalCliente = FormCliente()
    principalCliente.stackedWidget.setCurrentIndex(0)

    def clicSet():
        item = principalCliente.listProd_3.currentItem().text().split(sep="_")
        values = Conexion.DataPlatoSelect(str(item[1]))
        principalCliente.label_62.setText(values[0])
        principalCliente.label_63.setText(str(values[1]))
        principalCliente.label_64.setText(values[3])
        principalCliente.label.setText(values[2])

    def empty_carrito():
        principalCliente.listProd_5.clear()
        principalCliente.spinCant_3.setValue(0)

    def add_carrito():
        current = principalCliente.listProd_3.currentItem()
        cant = principalCliente.spinCant.value()
        if cant != 0 and current != None:
                nombre = principalCliente.label_62.text()
                precio = principalCliente.label_63.text()
                linea = str(cant)+"--"+nombre+"--"+precio
                principalCliente.listProd_5.addItem(linea)
                principalCliente.spinCant.setValue(0)
                totalActual = principalCliente.spinCant_3.value()
                total = totalActual + (int(precio) * cant)
                principalCliente.spinCant_3.setValue(total)
        else:
            QMessageBox.information(principalCliente, "Error", Mail.m6)

    def del_prod():
        current = principalCliente.listProd_5.currentItem()
        if current != None:
            item = current.text().split("--")
            totalActual = principalCliente.spinCant_3.value()
            total = totalActual - (int(item[0]) * int(item[2]))
            principalCliente.spinCant_3.setValue(total)
            x = principalCliente.listProd_5.currentRow()
            principalCliente.listProd_5.takeItem(x)
        else:
            QMessageBox.information(principalCliente, "Error", Mail.m7)

    def filtrar():
        principalCliente.listProd_3.clear()
        index = principalCliente.comboBox_3.currentIndex()
        if index != 0:
            filtro = principalCliente.comboBox_3.currentText()
            values = Conexion.DataPlatosFiltro(filtro)
            for row in values:
                principalCliente.listProd_3.addItem("$" + str(row[1]) + "_" + row[0])
        else:
            values = Conexion.DataPlatos()
            for row in values:
                principalCliente.listProd_3.addItem("$" + str(row[1]) + "_" + row[0])

    def enviarAcocina():
        principalCliente.listProd_5.selectAll()
        rows = [index.row() for index in principalCliente.listProd_5.selectedIndexes()]
        if rows != []:
            mesa = int(principalCliente.label_66.text())
            total = principalCliente.spinCant_3.value()
            fecha = date.today().strftime("%Y-%m-%d")
            val1 = str(Conexion.generarPedido(mesa, fecha, total))
            principalCliente.label_66.setText(val1)
            cod = ""
            for row in rows:
                colum = principalCliente.listProd_5.takeItem(0)
                line = colum.text().split("--")
                cod = Conexion.platosToPedidp(int(line[0]),line[1], int(val1))
                principalCliente.listProd_4.addItem(colum)
            val2 = str(principalCliente.spinCant_3.value())
            principalCliente.label_70.setText(val2)
            principalCliente.label_75.setText(val1)
            principalCliente.stackedWidget.setCurrentIndex(1)
            actualiza()
        else:
            QMessageBox.information(principalCliente, "Error", Mail.m11)

    def actualiza():
        cod = principalCliente.label_75.text()
        estado = Conexion.getEstado(cod)
        if estado == "EN COCINA":
            principalCliente.label_53.setText(Mail.m8)
            qpm = QPixmap("./img/cooking.gif")
            principalCliente.label_72.setPixmap(qpm)
        if estado == "EN ENVIO":
            principalCliente.label_53.setText(Mail.m9)
            qpm = QPixmap("./img/waitress.png")
            principalCliente.label_72.setPixmap(qpm)
        if estado == "ENTREGADO":
            principalCliente.label_53.setText(Mail.m10)
            qpm = QPixmap("./img/eating.png")
            principalCliente.label_72.setPixmap(qpm)
            principalCliente.pushButton_21.setEnabled(True)

    def enviarApago():
        a = principalCliente.label_70.text()
        b = principalCliente.label_75.text()
        principalCliente.label_73.setText(a)
        principalCliente.label_76.setText(b)

        principalCliente.listProd_4.selectAll()
        rows = [index.row() for index in principalCliente.listProd_4.selectedIndexes()]
        if rows != []:
            for row in rows:
                colum = principalCliente.listProd_4.takeItem(0)
                principalCliente.listProd_6.addItem(colum)
        principalCliente.stackedWidget.setCurrentIndex(2)

    def vaciar():
        principalCliente.lineEdit_2.setText("")
        principalCliente.lineEdit_6.setText("")
        principalCliente.lineEdit_11.setText("")
        principalCliente.spinCant_2.setValue(0)
        principalCliente.label_22.setText("")
        principalCliente.comboBox_4.setCurrentIndex(0)
        principalCliente.comboBox_5.setCurrentIndex(0)

    def calc():
        aPagar = int(principalCliente.label_73.text())
        pagado = int(principalCliente.spinCant_2.value())
        cambio = pagado - aPagar
        principalCliente.label_22.setText(str(cambio))

    def pagar():
        calc()
        cambio = int(principalCliente.label_22.text())
        if cambio >= 0:
            nom = principalCliente.lineEdit_2.text()
            tipo = principalCliente.comboBox_4.currentText()
            cc = principalCliente.lineEdit_6.text()
            tel = principalCliente.lineEdit_11.text()
            metodo = principalCliente.comboBox_4.currentText()
            cambio = int(principalCliente.label_22.text())
            pagado = int(principalCliente.spinCant_2.value())
            codped = int(principalCliente.label_76.text())
            Conexion.makeFactura(nom, tipo, cc, tel, metodo, cambio, pagado, codped)
            QMessageBox.information(principalCliente, "Pago exitoso", Mail.m13)
            generarCliente()
        else:
            QMessageBox.information(principalCliente, "Error", Mail.m12)

    def iniciar():
        values = Conexion.DataPlatos()
        for row in values:
            principalCliente.listProd_3.addItem("$"+str(row[1]) + "_" + row[0])
        principalCliente.listProd_3.itemClicked.connect(lambda: clicSet())
        principalCliente.pushButton_27.clicked.connect(lambda: filtrar())
        principalCliente.pushButton_19.clicked.connect(lambda: add_carrito())
        principalCliente.pushButton_22.clicked.connect(lambda: empty_carrito())
        principalCliente.pushButton_26.clicked.connect(lambda: del_prod())
        principalCliente.pushButton_20.clicked.connect(lambda: enviarAcocina())
        principalCliente.pushButton_24.clicked.connect(lambda: actualiza())
        principalCliente.pushButton_21.clicked.connect(lambda: enviarApago())
        principalCliente.pushButton_21.setEnabled(False)
        principalCliente.pushButton_23.clicked.connect(lambda: vaciar())
        principalCliente.pushButton_28.clicked.connect(lambda: calc())
        principalCliente.pushButton_25.clicked.connect(lambda: pagar())

    iniciar()
    principalCliente.show()
    principal.destroy()

