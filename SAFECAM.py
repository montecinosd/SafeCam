# Importamos las librerías necesarias
import numpy as np
import cv2
import time
import sys
import cv2
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PyQt5.uic import loadUi


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

class Login(QDialog):
    def __init__(self):
        self.usuario = "none"
        self.contrasenha = "none"
        super(Login,self).__init__()
##      cargo la platilla
        loadUi('Plantilla/loggin.ui',self)
##      imagen inicial
        self.Boton_Acceder.clicked.connect(self.onclickBoton_Acceder)
#Cuando presionamos el boton de acceder, guardamos y comprobamos si existe el usuario
    def onclickBoton_Acceder(self):
        self.usuario = self.Usuario.text()
        self.contrasenha = self.Contrasenha.text()
        #Verificar_Usuario(self.usuario,self.contrasenha)
        Verificar_Usuario(self.usuario,self.contrasenha,self.Label_Error)

def Verificar_Usuario(usuario,contrasenha,Label_Error):
    archivo = open("Usuarios/Usuarios.txt", "r")
    #List [0]usuario [1] contrasenha
    usuarios = archivo.readlines()
    for i in usuarios:
        i = i.rstrip('\n')
        i = i.split(';')
        aux_usuario = i[0]
        aux_contrasenha = i[1]
        if(aux_usuario == usuario and aux_contrasenha == contrasenha):
            print("loggeado")
            # app = QApplication(sys.argv)
            # window_Base = SafeCam()
            # window_Base.setWindowTitle('SafeCam')
            # window_Base.show()
            # sys.exit(app.exec_())
            return 1
        else:
            Label_Error.setText('Usuario o contrasenha invalidos.')
            return 0
def save_webcam(outPath,fps,mirror=False):
    # Capturing video from webcam:
    cap = cv2.VideoCapture(0)

    currentFrame = 0

    # Get current width of frame
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # float
    # Get current height of frame
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(outPath, fourcc, fps, (int(width), int(height)))

    while (cap.isOpened()):

        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret == True:
            if mirror == True:
                # Mirror the output video frame
                frame = cv2.flip(frame, 1)
            # Saves for video
            out.write(frame)

            # Display el frame resultante
            cv2.imshow('frame', frame)
        else:
            break
# SI APRETA Q LO CIERRA
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # To stop duplicate images
        currentFrame += 1

    # When everything done, release the capture
    cap.release()
    out.release()
    cv2.destroyAllWindows()

def main():
    app = QApplication(sys.argv)
    window_Login = Login()
    window_Login.setWindowTitle('SafeCam')
    window_Login.show()
    sys.exit(app.exec_())
    Fecha = time.strftime("%d-%m-%y")

    #save_webcam('RegistroVideo/'+Fecha+'.avi', 30.0,mirror=True)


if __name__ == '__main__':
    main()
