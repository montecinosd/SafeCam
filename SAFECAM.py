# Importamos las librerías necesarias
from PyQt5 import QtWidgets
import sys
# from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QDialog, QTreeWidgetItem
from PyQt5.QtGui import QPixmap
    #
from PyQt5.uic import loadUi
import time
from PyQt5 import uic
from os import listdir, path, stat, startfile
from mimetypes import MimeTypes
import os

from PyQt5.QtCore import QObject, pyqtSignal


class Persona:
    def __init__(Nombre,Rut,Direccion,Telefono):
        self.Nombre = Nombre
        self.Rut = Rut
        self.Direccion = Direccion
        self.Telefono = Telefono

class Encargado_de_seguridad(Persona):
    def __init__(Nombre,Rut,Direccion,Telefono,Horario):
        Persona.__init__(Nombre,Rut,Direccion,Telefono)
        self.Horario = Horario

class duenho(Persona):
    def __init__(Nombre,Rut,Direccion,Telefono,DireccionComercial):
        Persona.__init__(Nombre,Rut,Direccion,Telefono)
        self.DireccionComercial = DireccionComercial

class SafeCam(QDialog):
    def __init__(self):
        super(SafeCam,self).__init__()
##      cargo la platilla
        loadUi('Plantilla/base.ui',self)
        r=''+os.getcwd()
        # print(r+'\RegistroVideo')
        r_RegistroVideo = r+'\RegistroVideo'
        r_RegistroAlerta = r+'\RegistroAlerta'
        r_RegistroAcceso = r+'\RegistroAcceso'
        #Para enviar en OpenElement
        _rutaAuxliar = ''

        print("RIUTA AUX"+_rutaAuxliar)
        #Hago los ifs solamente para guardar la ruta y poder abrir las carpetas despues.
        if(self.BotonRegistroVideo.clicked):
            print("VIDEO...")
            self.directorio.clear()

            _rutaAuxliar = ''
            _rutaAuxliar = r_RegistroVideo
            self.BotonRegistroVideo.clicked.connect(lambda: self.getDir(r_RegistroVideo))

        if(self.BotonRegistoAlertas.clicked):
            self.directorio.clear()
            print("REGISTRO...")

            _rutaAuxliar = ''
            _rutaAuxliar = r_RegistroAlerta
            self.BotonRegistoAlertas.clicked.connect(lambda: self.getDir(r_RegistroAlerta))

        if(self.BotonRegistroAcceso.clicked):
            print("ACCESO...")
            self.directorio.clear()

            _rutaAuxliar = ''
            _rutaAuxliar = r_RegistroAcceso
            self.BotonRegistroAcceso.clicked.connect(lambda: self.getDir(r_RegistroAcceso))

        self.directorio.itemDoubleClicked.connect(lambda: self.OpenElement(_rutaAuxliar))
    def getDir(self,ruta):
            #delete filas de lo que estaba
            self.directorio.clear()
            #ruta nueva
            dir = ruta
            for element in listdir(dir):
                name = element
                a="\ "
                a = a[0]

                pathinfo = dir + a + name
                informacion = stat(pathinfo)
                if path.isdir(pathinfo):
                    type = "Carpeta de archivos"
                    size = ""
                else:
                    mime = MimeTypes()
                    type = mime.guess_type(pathinfo)[0]
                    size = str(informacion.st_size)+"bytes"
                #Fehca
                date = str(time.ctime(informacion.st_mtime))
                #array para crear filas
                row = [name,date,type,size]
                #insertar filas
                self.directorio.insertTopLevelItems(0,[QTreeWidgetItem(self.directorio,row)])
    def OpenElement(self,ruta):
        #Obtener item del user
        print("HOLAasdas")
        _ruta = ruta
        item = self.directorio.currentItem()
        #Crear Ruta(Carpeta o archivo)
        a="\ "
        a = a[0]
        elemento = _ruta +a+ item.text(0)

        if path.isdir(elemento):
            _ruta = elemento
            self.getDir(_ruta)
        else:
            startfile(elemento)

class Login(QDialog):
    def __init__(self):
        self.usuario = "none"
        self.contrasenha = "none"
        super(Login,self).__init__()
##      cargo la platilla
        loadUi('Plantilla/loggin.ui',self)
##      imagen inicial
        pixmap = QPixmap('Plantilla/Logo_SafeCam.png')
        self.image_SafeCam.setPixmap(pixmap)

        self.Boton_Acceder.clicked.connect(self.onclickBoton_Acceder)
#Cuando presionamos el boton de acceder, guardamos y comprobamos si existe el usuario
    def onclickBoton_Acceder(self):
        self.usuario = self.Usuario.text()
        self.contrasenha = self.Contrasenha.text()

        #Verificar_Usuario(self.usuario,self.contrasenha)
        self.Verificar_Usuario()

    def Verificar_Usuario(self):
        archivo = open("Usuarios/Usuarios.txt", "r")
        #List [0]usuario [1] contrasenha [2] 1 = Encargado_de_seguridad 2 = duenho
        usuarios = archivo.readlines()
        for i in usuarios:
            i = i.rstrip('\n')
            i = i.split(';')
            aux_usuario = i[0]
            aux_contrasenha = i[1]
            aux_tipoUsuario = i[2]
            if(aux_usuario == self.usuario and aux_contrasenha == self.contrasenha):
                print("loggeado con privilegios:" + aux_tipoUsuario)

                f=open("RegistroAcceso/Accesos.txt","a")
                Fecha = time.strftime("%d-%m-%y")
                Hora = time.strftime("%H:%M")
                str = 'Usuario: '+self.usuario +' - Fecha: '+Fecha+' Hora: '+Hora+'\n'
                print(str)
                f.write(str)
                f.close()

                self.accept()

                return 1
            else:
                self.Label_Error.setText('Usuario o contrasenha invalidos.')
                return 0


def main():
    app = QtWidgets.QApplication(sys.argv)
    login = Login()


    if login.exec_() == QtWidgets.QDialog.Accepted:
        window = SafeCam()
        window.show()
        sys.exit(app.exec_())


    # app = QApplication(sys.argv)
    # window_Login = Login()
    # window_Login.setWindowTitle('SafeCam')
    # window_Login.show()
    # sys.exit(app.exec_())


if __name__ == '__main__':
    main()
