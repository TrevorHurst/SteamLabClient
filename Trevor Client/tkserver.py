import socket
import sys
import os
import threading
import tkinter as tk

def send(*kwargs):
    reply = e1.get().encode()
    print(reply)
    for i in addri:
        try:
            s.sendto(reply,i)
        except:
            print("Failed to send to",i)

def bttn(text):
    global bcount
    bcount+=1
    return tk.Button(window, text=text,
                     command=lambda: [svar.set(text),e1.focus_set(),
                                      e1.icursor("end")]).place(x="5",y=f"{bcount*30+60}")

HOST = ''
PORT = 8888

def client_handler():
    global addri
    while True:
        try:
            client_data = s.recvfrom(10)
            print('a')
            if client_data[0] == b'Hello':
                for c in addri:
                    if c[0] == client_data[1][0]:
                        addri.remove(c)
                if client_data[1] in addri:
                    pass
                else:
                    addri.append(client_data[1])
                    print("Connect")
            else:
                print("SC recieved")

        except:
            pass

try :
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	print('Socket created')
except socket.error as msg :
	print('Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
	sys.exit()


# Bind socket to local host and port
try:
	s.bind((HOST, PORT))
except socket.error as msg:
	print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
	sys.exit()
	
print('Socket bind complete')

addri = []
bcount = 0

t = threading.Thread(target = client_handler)
t.start()
print(t,"Started")

window = tk.Tk()
window.title('Trevor Console')
window.geometry('500x800')
window.bind('<Return>', send)

tk.Label(window, text="Welcome to Trevor Console!").pack()
tk.Label(window, text="Enter your command below and it will send out!").pack()

svar = tk.StringVar()

e1 = tk.Entry(window, textvariable=svar, font=('Comic Sans',14))
e1.place(x="10",y="50")
e1.icursor("end")
e1.focus_set()
b1 = bttn("Updateall")
b2 = bttn("shutdownall")
b3 = bttn("logoutall")
b4 = bttn("shutdown_")
b5 = bttn("logout_")
b6 = bttn("Diskcleanup")
b7 = bttn("notepad")
b8 = bttn("TTS: ")
b9 = bttn("CMD: ")
b10 = bttn("Sendscreenshots")
window.mainloop()
while 1:
    e1.icursor("end")

    
s.close()
