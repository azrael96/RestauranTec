import mysql.connector

conexionexitosa = ""
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

def ConexionStatus():
    return conexionexitosa

def SearchUser(user):
    mycursor.execute("SELECT Nick_Seg, Clav_Seg, Rol_Seg, Est_Seg, Cod_Usu FROM seguridad WHERE Nick_Seg='" + user + "'")
    valores = mycursor.fetchall()
    return valores

def UpdateLoginSuccess(user):
    mycursor.execute(
        "UPDATE seguridad SET Est_Seg=" + str(0) + " WHERE Nick_Seg='" + user + "'")
    db.commit()

def UpdateLoginFail(user, i):
    mycursor.execute("UPDATE seguridad SET Est_Seg=" + i + " WHERE Nick_Seg='" + user + "'")
    db.commit()

def DataUser(cod):
    mycursor.execute("SELECT Nom_Usu, Ape1_Usu FROM usuario WHERE Cod_Usu='" + str(cod) + "'")
    return mycursor.fetchall()

def DataPlatos():
    mycursor.execute("SELECT Nom_Pla, Prec_Pla FROM plato")
    return mycursor.fetchall()

def DataPlatosFiltro(filtro):
    mycursor.execute("SELECT Nom_Pla, Prec_Pla FROM plato WHERE Tipo_Pla = "+ "'"+filtro+"'")
    return mycursor.fetchall()

def DataPlatoSelect(selected):
    mycursor.execute("SELECT Nom_Pla, Prec_Pla, Desc_Pla, Tipo_Pla FROM plato WHERE Nom_Pla=" + "'"+selected+"'")
    return mycursor.fetchone()

def generarPedido(mesa, date, total):
    mycursor.execute("SELECT MAX(Cod_Ped) FROM pedido")
    val = mycursor.fetchone()
    mycursor.execute(
        "INSERT INTO pedido (Cod_Ped, Mesa_Ped, Est_Ped, Pago_Ped, Fec_Ped, Tot_Ped) VALUES(%s, %s, %s, %s, %s, %s)", \
        (val[0]+1, mesa, "EN COCINA", "NO PAGADO", date, total))
    db.commit()
    return (val[0]+1)

def platosToPedidp(cant, plato, codPed):
    mycursor.execute("SELECT Cod_Pla FROM plato WHERE Nom_Pla = "+ "'"+plato+"'")
    val = mycursor.fetchone()
    mycursor.execute(
        "INSERT INTO pedidoplato (Cod_Ped, Cod_Pla, Cant_PP) VALUES(%s, %s, %s)", \
        (codPed, val[0], cant))
    db.commit()
    return str(val[0])

def getEstado(cod):
    db.commit()
    mycursor.execute("SELECT Est_Ped FROM pedido WHERE Cod_Ped = "+ "'"+cod+"'")
    val = mycursor.fetchone()
    return val[0]

def makeFactura(nom, tipo, cc, tel, metodo, cambio, pagado, codped):
    mycursor.execute("UPDATE pedido SET Pago_Ped = 'PAGADO' WHERE Cod_Ped =" + str(codped))
    mycursor.execute("SELECT MAX(Cod_Fac) FROM factura")
    val = mycursor.fetchone()
    mycursor.execute(
        "INSERT INTO factura (Cod_Fac, NomC_Fac, Tipo_Fac, CC_Fac, Tel_Fac, Meto_Fac, Camb_Fac, Pagdo_Fac, Cod_Ped) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", \
        (val[0]+1, nom, tipo, cc, tel, metodo, cambio, pagado, codped))
    db.commit()

def listUsu():
    mycursor.execute("SELECT Nick_Seg FROM seguridad ORDER BY Nick_Seg ASC")
    values = mycursor.fetchall()
    return values

def selectUsu(item):
    mycursor.execute(
        "SELECT Nom_Usu, Ape1_Usu, Ape2_Usu, Tel_Usu, Dir_Usu, Tipo_Usu, CC_Usu, Mail_Usu FROM usuario WHERE Cod_Usu=" + str(item))
    values = mycursor.fetchone()
    return values

def selectNick(item):
    mycursor.execute("SELECT Nick_Seg, Clav_Seg, Rol_Seg, Est_Seg, Cod_Usu FROM seguridad WHERE Nick_Seg='" + item + "'")
    values = mycursor.fetchone()
    return values

def actualUser():
    mycursor.execute("SELECT MAX(Cod_Usu) FROM usuario")
    val = mycursor.fetchone()
    return val[0]

def addUser(nom, ape1, ape2, tel, Dir, tDoc, nDoc, cor, Usu, pas, rol, est, cod):
    mycursor.execute("INSERT INTO usuario (Cod_Usu, Nom_Usu, Ape1_Usu, Ape2_Usu, Tel_Usu, Dir_Usu, Tipo_Usu, CC_Usu, Mail_Usu) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", \
                        (cod, nom, ape1, ape2, tel, Dir, tDoc, nDoc, cor))
    db.commit()
    mycursor.execute(
        "INSERT INTO seguridad (Nick_Seg, Clav_Seg, Rol_Seg, Est_Seg, Cod_Usu) VALUES(%s, %s, %s, %s, %s)", \
        (Usu, pas, rol, est, cod))
    db.commit()

def editUser(nom, ape1, ape2, tel, Dir, tDoc, nDoc, cor, Usu, pas, rol, est, cod):
    mycursor.execute("INSERT INTO usuario (Cod_Usu, Nom_Usu, Ape1_Usu, Ape2_Usu, Tel_Usu, Dir_Usu, Tipo_Usu, CC_Usu, Mail_Usu) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", \
                        (cod, nom, ape1, ape2, tel, Dir, tDoc, nDoc, cor))
    db.commit()
    mycursor.execute(
        "INSERT INTO seguridad (Nick_Seg, Clav_Seg, Rol_Seg, Est_Seg, Cod_Usu) VALUES(%s, %s, %s, %s, %s)", \
        (Usu, pas, rol, est, cod))
    db.commit()

def selectNickAlone(item):
    mycursor.execute("SELECT Cod_Usu FROM seguridad WHERE Nick_Seg='" + item + "'")
    values = mycursor.fetchone()
    return values

def updateUsu(item, nom, ape1, ape2, tel, Dir, tDoc, nDoc, cor, Usu, pas, rol, est, cod):
    mycursor.execute(
        "UPDATE usuario SET Nom_Usu = %s, Ape1_Usu = %s, Ape2_Usu = %s, Tel_Usu = %s, Dir_Usu = %s, Tipo_Usu = %s, CC_Usu = %s, Mail_Usu = %s WHERE Cod_Usu = %s",
        (nom, ape1, ape2, tel, Dir, tDoc, nDoc, cor, item))
    db.commit()
    mycursor.execute(
        "UPDATE seguridad SET Nick_Seg = %s, Clav_Seg = %s, Rol_Seg = %s, Est_Seg = %s WHERE Cod_Usu = %s",
        (Usu, pas, rol, est, cod))
    db.commit()

def deleteUsu(item):
    mycursor.execute("DELETE FROM usuario WHERE Cod_Usu=" + str(item))
    db.commit()
    mycursor.execute("DELETE FROM seguridad WHERE Cod_Usu=" + str(item))
    db.commit()

def listPlato():
    mycursor.execute("SELECT Nom_Pla FROM plato ORDER BY Nom_Pla ASC")
    values = mycursor.fetchall()
    return values

def selectPlato(item):
    mycursor.execute("SELECT Nom_Pla, Prec_Pla, Desc_Pla, Tipo_Pla FROM plato WHERE Nom_Pla='" + item + "'")
    values = mycursor.fetchone()
    return values

def addPlato(nom, pre, des, tipo):
    mycursor.execute(
        "INSERT INTO plato (Nom_Pla, Prec_Pla, Desc_Pla, Tipo_Pla) VALUES(%s, %s, %s, %s)", \
        (nom, pre, des, tipo))
    db.commit()

def updatePlato(cod,nom, pre, des, tipo):
    mycursor.execute(
        "UPDATE plato SET Nom_Pla = %s, Prec_Pla = %s, Desc_Pla = %s, Tipo_Pla = %s WHERE Nom_Pla = %s",
        (nom, pre, des, tipo, cod))
    db.commit()

def deletePlato(item):
    mycursor.execute("DELETE FROM plato WHERE Nom_Pla= %s", (item, ))
    db.commit()

def listOrdenCocina():
    mycursor.execute("SELECT Cod_Ped FROM pedido WHERE Est_Ped='EN COCINA' ORDER BY Cod_Ped ASC")
    values = mycursor.fetchall()
    return values

def listOrdenEnvio():
    mycursor.execute("SELECT Cod_Ped FROM pedido WHERE Est_Ped='EN ENVIO' ORDER BY Cod_Ped ASC")
    values = mycursor.fetchall()
    return values

def selectEnPedido(codPed):
    mycursor.execute("SELECT Cod_Pla, Cant_PP FROM pedidoplato WHERE Cod_Ped='"+codPed+"'")
    values = mycursor.fetchall()
    lines = []
    for row in values:
        mycursor.execute("SELECT Nom_Pla FROM plato WHERE Cod_Pla = %s", (row[0],))
        nom = mycursor.fetchone()
        cant = str(row[1])
        line = cant+"--"+nom[0]
        lines.append(line)
    return lines

def updateOrden(CodPed, estado):
    mycursor.execute(
        "UPDATE pedido SET Est_Ped = %s WHERE Cod_Ped = %s",
        (estado, CodPed))
    db.commit()

def listFactura():
    mycursor.execute("SELECT Cod_Fac FROM factura ORDER BY Cod_Fac ASC")
    values = mycursor.fetchall()
    return values

def selectFactura(codPed):
    mycursor.execute("SELECT NomC_Fac FROM factura WHERE Cod_Fac='"+codPed+"'")
    values = mycursor.fetchone()
    lines = str(codPed) + "--"+str(values[0])
    return lines