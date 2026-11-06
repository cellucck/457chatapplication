import socket 
import threading

#1 - Sever sets up a listening socket

#local host - a reference to the computer this is running on
HOST = "127.0.0.1"

#any number larger than 1023
PORT = 65431



#creates the listening socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    '''
    creates the listening socket, don't need s.close() because python
    will do it automatically
    args:
    socket.AF_INET - version four internet addresses
    socket.SOCK_STREAM - TCP socket streams
    '''
    #binds the socket to a specific host/port
    s.bind((HOST, PORT))

    #listen for a connection
    s.listen()

    #blocks remaining action until a connection is requested
    conn, addr = s.accept()
    #conn - a new socket object used to send/receive data on this connection
    #addr - internet address of the client


# 3 - Data is exchanged
    with conn:
        print(f'Connected by {addr}')
        def recv(connection):
            done = False
            while done is False:
                data = connection.recv(1024)
                print(f'\nUser: {data.decode('utf-8')}')
        
        threading.Thread(target=recv, args=(conn, )).start()

        message = input('You: ')
        conn.sendall(message.encode('utf-8'))

        
