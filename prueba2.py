import numpy as np
from multiprocessing import Process, Queue
import cv2
from PIL import Image, ImageTk
import tkinter as tk
 
#define funcao para terminar processo
def quit_(root, process):
   process.terminate()
   root.destroy()
#define funcao que pega o frame, converte para o formato correto e atualiza nosso label
def update_image(image_label, queue):
    frame = queue.get()
    im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    a = Image.fromarray(im)
    b = ImageTk.PhotoImage(image=a)
    image_label.configure(image=b)
    image_label._image_cache = b
    root.update()
 
#responsavel por chamar a funcao que converte a imagem e criar o loop
def update_all(root, image_label, queue):
   update_image(image_label, queue)
   root.after(0, func=lambda: update_all(root, image_label, queue))
 
# responsavel pela captura de video
def image_capture(queue):
   vidFile = cv2.VideoCapture(0)
   while True:
      try:
         flag, frame=vidFile.read()
         if flag==0:
             break
         queue.put(frame)
         cv2.waitKey(20)
      except:
         continue

queue = Queue()
root = tk.Tk()
image_label = tk.Label(master=root)
image_label.pack()
p = Process(target=image_capture, args=(queue,))
p.start()
quit_button = tk.Button(master=root, text='Sair',command=lambda: quit_(root,p))
quit_button.pack()
root.after(0, func=lambda: update_all(root, image_label, queue))
root.protocol('WM_DELETE_WINDOW', lambda: quit_(root,p))
print("HOLA")

root.mainloop()
p.join()
