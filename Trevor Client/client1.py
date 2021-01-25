#TODO: Chunkify the image in screen grab 1480 bytes
#Then Un-chunck in the server side


import socket
import sys
from gtts import gTTS
import os
import io
import time
from playsound import playsound
import subprocess
from threading import Timer, Thread
from PIL import ImageGrab, Image

def screengrab():
        global host, port
        print("Screengrab")
        im = ImageGrab.grab().resize((240,135),)
        bim1 = im.tobytes()
        a = im.convert(mode='L')
        bim2 = a.tobytes()
        print(len(bim1),len(bim2))
        #sends = [len(a/6)]
        s.sendto(bim2,(host,port))
        print('sent')
        
def reconnect():
        while True:
                time.sleep(10)
                global s
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                except socket.error:
                        print('Failed to create socket')
                        sys.exit()
                s.sendto("Hello".encode(), (host, port))
                connected = True
                print("A")
name = socket.gethostname()
HEADERSIZE = 10
try:
        int(name[-1])
        name_string = name[:-1]
except:
        name_string = name
currentuser = os.getlogin()

a = Timer(10,reconnect)
a.start()

while True:


        st = time.time()
        host = '192.168.1.50';
        port = 8888;
        connected = False
        while(1):
            try :
                if not connected:
                        try:
                                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        except socket.error:
                                print('Failed to create socket')
                                sys.exit()
                        s.sendto("Hello".encode(), (host, port))
                        connected = True
                        print("A")
                else:
                        s.settimeout(2.0)
                        d = s.recvfrom(1024)
                        reply = d[0].decode()
                        addr = d[1]
                        print(reply)
                        
                        if reply == "notepad": #Open notepad
                                subprocess.Popen("notepad")
                        if reply == "Updateall":
                                print("Update")
                                subprocess.Popen("start ms-settings:windowsupdate", shell=True)

                        if reply == "Sendscreenshots":
                                a = Thread(target=screengrab)
                                a.start()
                                
                        if reply == "shutdownall": #Shutdown all cpus
                                print("SHUTDOWN")
                                subprocess.Popen("shutdown /s")
                                
                        if reply == f"shutdown_{name_string}": #Shutdown specific cpu
                                subprocess.Popen("shutdown /s")
                                
                        if reply == f"logout_{name_string}": #logout specific cpu
                                subprocess.Popen("shutdown /l")
                                
                        if reply == "logoutall": #logout all cpus
                                print("LOGOUT")
                                subprocess.Popen("shutdown /l")
                                
                        if reply == "Diskcleanup": #Disk cleanup
                                subprocess.Popen("cleanmgr")

                        if reply[:5] == "TTS: ": #Text to speech!
                                print("TTS")
                                tts = gTTS(text=reply[5:], lang='en')
                                tts.save(f"C:\\Users\\{currentuser}\\Desktop\\HAL.mp3")
                                playsound(f"C:\\Users\\{currentuser}\\Desktop\\HAL.mp3")
                                os.remove(f"C:\\Users\\{currentuser}\\Desktop\\HAL.mp3")
                        if reply[:5] == "CMD: ":
                                print(reply[5:])
                                subprocess.Popen(reply[5:],shell=True)
            except:
                pass
