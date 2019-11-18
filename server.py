import socket
import sys
import time
import socketserver
from threading import Thread
from os.path import exists
 
HOST = '192.168.1.6'
PORT = 9090
#sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def fileName():
    dte = time.localtime()
    Year = dte.tm_year
    Mon = dte.tm_mon
    Day = dte.tm_mday
    WDay = dte.tm_wday
    Hour = dte.tm_hour
    Min = dte.tm_min
    Sec = dte.tm_sec
    imgFileName = '  ' + str(Year) + '_' + str(Mon) + '_' + str(Day) + ' ' + str(Hour) + '_' + str(Min) + '_' + str(Sec)
    return imgFileName

class MyTcpHandler(socketserver.BaseRequestHandler):
    def handle(self):        
        data_transferred = 0
        print('[%s] linking' %self.client_address[0])
        filename = 'image_yolo_out_py'
        data = self.request.recv(65564)
        print(data)
        
        if not data:
            time.sleep(10)
            print('not dangerous')            
        
        '''
        sock.bind((HOST,PORT))
        sock.listen(3)
        conn,addr = sock.accept()
        t = Thread(target=diff,args=(self.client_address[0],data,))
        t.start()
           '''         
        
        print('street light connect!!')                     
        with open('Street_light _save/' + filename + fileName() + '.jpg', 'wb') as f:
            try:                         
                while data:
                    f.write(data)
                    data_transferred += len(data)
                    data = self.request.recv(65564)
                    print(data)
                    if not data_transferred > 0:
                     break
            except Exception as e:
                 print(e)


      
     
        if data_transferred > 0: 
            print('파일[%s] 전송종료. 전송량 [%d]' %(filename + fileName() + '.jpg', data_transferred))


    
def runServer():
    print('++++++client start++++++')
    print("+++ if end 'Ctrl + C' touch.")
 
    try:
        server = socketserver.TCPServer((HOST,PORT),MyTcpHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print('++++++ client end.++++++')        
    

    
runServer() 
 
