#2 - Client initiates a connection

import socket 
import threading

HOST = "127.0.0.1"
PORT = 65431



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))


#3 - Data is exchanged   
    def send(server):
        done = False
        while done is False:
            message = input('You: ')
            bytes_message = message.encode('utf-8')
            server.sendall(bytes_message)

    threading.Thread(target=send, args=(s, )).start()
    data = s.recv(1024)
    print(f'\nServer: {data.decode('utf-8')}')




    