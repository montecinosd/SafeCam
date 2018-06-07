import threading
import time
import numpy as np
import sys
import cv2
from PyQt5 import QtWidgets
import os

# from PyQt5.QtCore import *
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QPixmap

from PyQt5.uic import loadUi
from SAFECAM import *
# from SAFECAM_CAMARA import *


def Ejecutar_Interfaz():
    exec(open('SAFECAM.py').read())

def Ejecutar_Camara():
    threading.Timer(120.0, Ejecutar_Camara).start() # called every minute
    exec(open('SAFECAM_CAMARA.py').read())


# hilo1 = threading.Thread(target=Ejecutar_Camara)
hilo2 = threading.Thread(target=Ejecutar_Interfaz)
hilo2.start()
# hilo1.start()


def hello_world():
    threading.Timer(02.0, hello_world).start() # called every minute
    print("Hello, World!")

# hello_world()
Ejecutar_Camara()
