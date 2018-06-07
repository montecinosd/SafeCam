import numpy as np
import time
import sys
import cv2

import os

def Crear_carpeta(ruta):
    DirectoryPath = ruta
    os.makedirs(DirectoryPath,exist_ok=True)

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

        # Fecha = time.strftime("%d-%m-%y")
        # if (Fecha == )
        # print(time.strftime("%d-%m-%y %H:%M:%S"))

        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret == True:
            if mirror == True:
                # Mirror the output video frame
                frame = cv2.flip(frame, 1)
            # Saves for video
            # out.write(frame)

            # Display el frame resultante
            cv2.imshow('frame', frame)
        # if ()
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

Fecha = time.strftime("%d-%m-%y")
Hora = time.strftime("%H-%M")
# print(time.strftime("%d-%m-%y"))
# print(Hora)
Crear_carpeta('RegistroVideo/'+Fecha)
save_webcam('RegistroVideo/'+Fecha+'/'+Hora+'.avi', 30.0,mirror=True)

# Fecha_inicial =time.strftime("%d-%m-%y")
# minuto_inicial = time.strftime("%M")
# while(Hora_inicial == Hora_actual):
#     pass
