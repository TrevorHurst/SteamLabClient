import socket
import sys
import os
import threading
import PySimpleGUI as sg
def jump():
    print("Hello")
e = sg.Input()
Connectedlist=sg.Listbox(values=[],size=(50,10))
b1 = sg.Button("R1")
b2 = sg.Button("R2")
b3 = sg.Button("R3")
b4 = sg.Button("R4")
b5 = sg.Button("R5")
b6 = sg.Button("R6")
b7 = sg.Button("R7")
b8 = sg.Button("R8")
b9 = sg.Button("R9")
sg.theme('Dark Black')
layout = [[sg.Text("""Welcome to the "Trevor Console" Menu""")],
          [sg.Text("Please enter your command below")],[e],[sg.Button("Okay",bind_return_key=True)],
          [sg.Text("Commands are:")],
          [b1,sg.Text("shutdownall - shuts down all computers")],
          [b2,sg.Text("notepad - opens notepad on all computers")],
          [b3,sg.Text("shutdown_[name] - shutsdown specific computer ex, Michelangelo, STANZ, Donatello")],
          [b4,sg.Text("logout_[name] - logout specific computerm ex, Spengler")],
          [b5,sg.Text("logoutall - log out all computers")],
          [b6,sg.Text("Diskcleanup - run disk cleanup on all computers")],
          [b7,sg.Text("Updateall - update all computers")],
          [b8,sg.Text("TTS: {text} - speak text")],
          [b9,sg.Text("""CMD: command - Run a cmd command on users computer, ex, "start www.facebook.com" """)],[Connectedlist]]

window = sg.Window('Trevor Console', resizable = True,layout=layout,margins=(10,50))
HOST = ''
PORT = 8888

def client_handler():
    global addri
    while True:
        try:
            client_data = s.recvfrom(20)
            for c in addri:
                if c[0] == client_data[1][0]:
                    addri.remove(c)
            if client_data[1] in addri:
                pass
            else:
                addri.append(client_data[1])
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

t = threading.Thread(target = client_handler)
t.start()
while 1:
    event, values = window.read()
    try:
        layout+= [sg.Checkbox(i,default=True) for i in addri]
    except:
        pass
    if event == sg.WIN_CLOSED:
        os._exit(0)
        break
    if event == 'R1':
        e("shutdownall")
    if event == 'R2':
        e("notepad")
    if event == 'R3':
        e("shutdown_")
    if event == 'R4':
        e("logout_")
    if event == 'R5':
        e("logoutall")
    if event == 'R6':
        e('Diskcleanup')
    if event == 'R7':
        e('Updateall')
    if event == 'R8':
        e("TTS: ")
    if event == 'R9':
        e("CMD: ")
    if event == 'Okay':
        reply = values[0]
        print(f"Reply: {reply}")
        if reply == "Exit":
            s.close()
            break
        for i in addri:
            try:
                print(i)
                s.sendto(reply.encode(),i)
            except:
                pass
s.close()
