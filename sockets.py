import socket
from sys import stdout
from os import _exit
from threading import Thread

list_of_clients = []

class ClientThread(Thread):
    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port

    def broadcast(self, message, connection):
        for clients in list_of_clients:
            if clients != connection:
                print(conn, clients)
                try:
                    clients.send(message.encode('utf-8'))
                except:
                    clients.close()
                    self.remove(clients)

    def remove(self, connection):
        if connection in list_of_clients:
            list_of_clients.remove(connection)

    def run(self):
        while True:
            data = conn.recv(2048)
            if not data:
                break
            else:
                if data == b'Quit\n' or data == b'Quit\r\n':
                    stdout.flush()
                    _exit(0)
                    tcpsock.close()
                    break
                print(data)
                message_to_send = "<" + ip + "> " + str(data)
                self.broadcast(message_to_send, conn)

TCP_IP = '0.0.0.0'
TCP_PORT = 9876
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    tcpsock.listen(100)
    print("Waiting for incoming connections...")
    (conn, (ip, port)) = tcpsock.accept()
    list_of_clients.append(conn)
    print(ip + ": " + str(port) + " connected")
    print(list_of_clients)
    newthread = ClientThread(ip, port)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()