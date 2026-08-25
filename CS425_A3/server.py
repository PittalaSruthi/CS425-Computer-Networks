from socket import *

# server address and port
server_ip = "localhost"
server_port = 12000

# create UDP socket
server_socket = socket(AF_INET, SOCK_DGRAM)

# bind socket to port
server_socket.bind((server_ip, server_port))

print("Server waiting...")

# receive one message from client
message, client_address = server_socket.recvfrom(1024)

# print client message
print("Client:", message.decode())

# server sends one reply
reply = input("Server: ")
server_socket.sendto(reply.encode(), client_address)

# close server
server_socket.close()