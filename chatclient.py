import socket
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP_address = 'localhost'
Port = 9876
server.connect((IP_address, Port))

while True:
    sockets_list = [sys.stdin, server]
    read_sockets,write_socket, error_socket = select.select(sockets_list, [], [])
    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            print (message)
        else:
            message = sys.stdin.readline()
            server.sendall(message.encode('utf-8'))
            print("<You>")
            print(message)
            sys.stdout.flush()
server.close()