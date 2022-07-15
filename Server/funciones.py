import os
import time
from time import sleep
import numpy as np
from matplotlib import pyplot as plt
import RPi.GPIO as gpio
import cv2

def blink_led():
    gpio.setmode(gpio.BOARD)
    
    gpio.setup(18, gpio.OUT)
    gpio.output(18, gpio.HIGH)
    print("18 true")
    sleep(1)
    print("18 false")
    gpio.output(18, gpio.LOW)
    sleep(1)
    gpio.output(18, gpio.HIGH)
   
def button():
    gpio.setmode(gpio.BOARD) # Use physical pin numbering
    gpio.setup(10, gpio.IN, pull_up_down=gpio.PUD_DOWN)
    if gpio.input(10) == gpio.HIGH:
        print("Boton imagen apretado ")
        take_image()
        blink_led()
        time.sleep(0.2)
def button2():
    gpio.setmode(gpio.BOARD) # Use physical pin numbering
    gpio.setup(12, gpio.IN, pull_up_down=gpio.PUD_DOWN)
    if gpio.input(12) == gpio.HIGH:
        print("Boton video apretado ")
        take_video()
        
def mkdir():
    directory = "tarea"
    # Parent Directory path
    parent_dir = "/home/grupo03/Documentos"
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    print("Directory '% s' created" % directory)

  
def take_image():
    cam = cv2.VideoCapture(-1)
    img_name= "imagenes/img_"+str(time.strftime("%H-%M-%S")+".jpg") 
    while True:
        ret, image = cam.read()
        #cv2.imshow('Imagetest',image)
        k = 1 #cv2.waitKey(1)
        if k != -1:
            break
    cv2.imwrite(img_name, image)
    cam.release()
    cv2.destroyAllWindows()
    print("imagen tomada")
def take_video2():
    cap=cv2.VideoCapture(0)
    
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    vid_name= "videos/vid_"+str(time.strftime("%H-%M-%S")+".avi") 
    video_cod=cv2.VideoWriter_fourcc(*"XVID")
    video_output=cv2.VideoWriter(vid_name,video_cod,10,(frame_width,frame_height))
    
    while(True):
        ret, frame = cap.read()

        if ret == True:
            video_output.write(frame)
            cv2.imshow("frame",frame)
            if cv2.waitKey(1) & 0xFF ==ord("x"):
                break
        else:
            break 
    
    cap.release()
    video_output.release()
    cv2.destroyAllWindows()

#blink_led()
#mkdir()
#while(True):
    #blink_led()
    
#    button()
#    button2()
#take_image()
#take_video2()
    


# Diseñar un sistema de captura de imagenes y video con las siguientes caracteristicas:
    # (i) El sistema debe contar con 2 botones, el primero debe ser capaz de que el sistema tome una foto a traves de una webcam conectada a 
    # las raspberry. El segundo boton debe dar inicio y fin a la toma de video 
    # (ii) Al arrancar el codigo el sistema debe prender el led, luego mientras el sistema este tomando la foto y 
    # el video el led debe estar ralizando un blink, al terminar el proceso el led se debe mantener endencido
    # (iii) Las imagenes y videos se deben guardar en carpetas diferentes, creadas por el mismo codigo, el nombre de estas carpeta es "Imagenes y  "Videos"
    # cada imagen y video debe ser guardado con el nombre img_n_d, siendo n la canditada de fotos guardas en la carpeta y d la fecha en la cual se tomo
    # analogamente los videos seran guardados como video_n_d