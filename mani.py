from PyQt5 import QtWidgets, QtGui, QtCore, uic 
import sys
import time
import cv2
import os
import pymysql
import socket
def send_takeimage():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('192.168.1.1', 10000)
    print('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)

    try:

        # Send data
        #imageName="Imagenes/"+string_textInput_imageName+str(time.strftime("%H-%M-%S"))+".jpg"
        message = b'takeimage'
        
        #my_str = str(time.strftime("%H-%M-%S"))
        #message = str.encode(my_str)
        
        print('sending {!r}'.format(message))
        sock.sendall(message)

        # Look for the response
        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print('received {!r}'.format(data))

    finally:
        print('closing socket')
    sock.close()
def send_takevideo():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('192.168.1.1', 10000)
    print('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)

    try:

        # Send data
        #imageName="Imagenes/"+string_textInput_imageName+str(time.strftime("%H-%M-%S"))+".jpg"
        message = b'takevideo'
        
        #my_str = str(time.strftime("%H-%M-%S"))
        #message = str.encode(my_str)
        
        print('sending {!r}'.format(message))
        sock.sendall(message)

        # Look for the response
        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print('received {!r}'.format(data))

    finally:
        print('closing socket')
    sock.close()

class MainWindow(QtWidgets.QMainWindow): #class una forma de ordenar el codigo
    def __init__(self):
        super(MainWindow, self).__init__() #Super inicializa de manera inteligente y ordenada las cosas definidas en class MainWindow
        self.window = uic.loadUi("interfaz.ui", self) 
        print("Bienvenido!")
        var_label_counterImageTempVar=0
        self.window.button_connectSession.clicked.connect(self.fun_conectar)
        self.window.button_imagen.clicked.connect(self.fun_takeimage)
        self.window.button_startvideo.clicked.connect(self.fun_startvideo)
        self.window.button_stopvideo.clicked.connect(self.fun_stopvideo)
        
        self.window.tab_image.setEnabled(False)
        self.window.tab_session.setEnabled(False)
        self.window.tab_video.setEnabled(True)
        self.window.button_stopvideo.setEnabled(True)
        
    def fun_conectar(self):
        try:
            
            self.window.tab_image.setEnabled(True)
            self.window.tab_video.setEnabled(True)
            self.window.button_connectSession.setEnabled(False)
            self.window.label_userError.setText("Conectado!")
        except Exception as e:
            self.window.label_userError.setText("Error Usuario o Contraseña")
            print(e)
            
    def fun_takeimage(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('192.168.1.1', 10000)
        print('connecting to {} port {}'.format(*server_address))
        sock.connect(server_address)
        try:
            message = b'takeimage'
            print('sending {!r}'.format(message))
            sock.sendall(message)
            amount_received = 0
            amount_expected = len(message)
            while amount_received < amount_expected:
            	data = sock.recv(16)
            	amount_received += len(data)
            	print('received {!r}'.format(data))
        finally:
            print('closing socket')
            sock.close()

    #   send_takeimage()
    def fun_startvideo(self):
        send_takevideo()
        
        
    def fun_stopvideo(self):
        string_textInput_videoName= self.window.textInput_videoName.toPlainText()
	
        message = str.encode(string_textInput_videoName)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('192.168.1.1', 10000)
        print('connecting to {} port {}'.format(*server_address))
        sock.connect(server_address)
        try:
            #message = b'This is the message.  It will be repeated.'
            print('sending {!r}'.format(message))
            sock.sendall(message)
            amount_received = 0
            amount_expected = len(message)
            while amount_received < amount_expected:
            	data = sock.recv(16)
            	amount_received += len(data)
            	print('received {!r}'.format(data))
        finally:
            print('closing socket')
            sock.close()
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) #Maneja todas las variables del sistema
    window = MainWindow()
    window.show() #Muestra la MainWindow
    sys.exit(app.exec_())
            
            
"""
Programar en la raspberry:
- Un sensor Dht11 (temperatura y humedad), el cual muestreo con una tasa configurable.
- Un led que cambia de estado (inicial apagada) a parpadeando (encendido y apagado con un
delta de tiempo configurable) cuando se inicie la medición del DHT11.

- Cámara que tome video y fotos LISTOOOOOOOOOOO
- Realizar que la raspberry se convierta en una estación de WiFI (con un SSID y PSS)
- Socket TCP cliente, el cual envié los datos del sensor al TCP servidor.
Realizar interfaz gráfica que se ejecute en sus respectivos notebooks. Esta interfaz debe realizar:
- Que controle las acciones de las raspberry (cambiar tiempo de muestreo, tiempo del blink
del led, acción de tomar fotos y video) y graficas Temperatura y humedad.
- Que se conecte a la raspberry a través del socket TCP client.
- Todos los códigos asociados deberán estar ingresados a un Github Publico.
Fecha de entrega viernes 15 de julio 
"""
            
            
            
            
            
            
            
            
