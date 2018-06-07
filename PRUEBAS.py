import sys, time
from PyQt5.QtWidgets import QApplication, QDialog, QTreeWidgetItem
from PyQt5 import uic
from os import listdir, path, stat
from mimetypes import MimeTypes

class Dialogo(QDialog):
 def __init__(self):
  QDialog.__init__(self)
  uic.loadUi("treewidget.ui", self)
  self.boton.clicked.connect(self.getDir)

 def getDir(self):
  #Eliminar todas las filas de la búsqueda anterior
  self.directorio.clear()
  #Ruta indicada por el usuario
  dir = self.ruta.text()
  #Si es un directorio
  if path.isdir(dir):
   #Recorrer sus elementos
   for element in listdir(dir):
    name = element
    pathinfo = dir + "\\" + name
    informacion = stat(pathinfo)
    #Si es un directorio
    if path.isdir(pathinfo):
     type = "Carpeta de archivos"
     size = ""
    else:
     mime = MimeTypes()
     type = mime.guess_type(pathinfo)[0]
     size = str(informacion.st_size) + " bytes"
    #Fecha de modificación
    date = str(time.ctime(informacion.st_mtime))
    #Crear un array para crear la fila con los items
    row = [name, date, type, size]
    #Insertar la fila
    self.directorio.insertTopLevelItems(0, [QTreeWidgetItem(self.directorio, row)])

app = QApplication(sys.argv)
dialogo = Dialogo()
dialogo.show()
app.exec_()
