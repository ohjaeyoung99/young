import SocketServer
from os.path import exists
import os 
import sys
import socket
import time
from threading import Thread

HOST = '203.255.77.210'
PORT = 9090


def getFileFromClient():
	data_transferred = 0
	filename = 'image_yolo_no_py' + '.jpg'
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((HOST,PORT)) 
	print('+++++++connect 2+++++++')
	
	
	if not exists(filename):
			time.sleep(100)
			print('not danger')
			return 
	
		
	with open(filename, 'rb') as f:
		try:
			data = f.read(1024)					
			while data:
				data_transferred += sock.send(data)
				data = f.read(1024)
					
		except Exception as e:
			print(e)
			
	print('file_2[%s] send [%d]' %(filename, data_transferred))
	'''
	street_name = 'street_light'  
	sock.sendall(street_name)'''          
	os.remove('/home/pi/Downloads/yolo-object-detection/yolo-object-detection/' + 'image_yolo_no_py' + '.jpg')
						         
    	
while True:
	try:	
		getFileFromClient()

	except KeyboardInterrupt:
		print('++++++ client end ++++++')
		exit()
						
	
      



	
              

