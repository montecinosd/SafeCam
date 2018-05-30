import sys
import cv2
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PyQt5.uic import loadUi


class SafeCam(QDialog):
    def __init__(self):
        super(SafeCam,self).__init__()
##      cargo la platilla
        loadUi('Plantilla/base.ui',self)
##      imagen inicial
        self.image=None
        self.BotonRegistroVideo.clicked.connect(self.prender_Camara)
        
    def prender_Camara(self):

        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,1280)

        #actualizamos
        self.timer=QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        

        self.timer.start(5)
        

    def update_frame(self):
        
        ret,self.image=self.capture.read()
        self.image=cv2.flip(self.image,1)
        self.displayImage(self.image,1)

    def displayImage(self,img,window=1):
        qformat = QImage.Format_Indexed8
        print(qformat)
        if len(img.shape)==3: #[0] = filas [1]=columna [2] canales
            if img.shape[2]==4:
                qformat=QImage.Format_RGBA8888
            else:

                qformat = QImage.Format_RGB888
        #Saco con formato
        outImage=QImage(img,img.shape[1],img.shape[0],img.strides[0],qformat)
        #BGR>>RGB        
        outImage=outImage.rgbSwapped()

            
        if(window==1):
            print("hola")

            self.MostrarCamara.setPixmap(Qpixmap.fromImage(outImage))

            #self.MostrarCamara.setScaledContents(True)

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = SafeCam()
    window.setWindowTitle('SafeCam')
    window.show()
    sys.exit(app.exec_())
