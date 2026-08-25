from socket import *

# server address
server_ip = "localhost"
server_port = 12000

# create UDP socket
client_socket = socket(AF_INET, SOCK_DGRAM)

# send message to server
message = input("Client: ")
client_socket.sendto(message.encode(), (server_ip, server_port))

# receive reply from server
reply, _ = client_socket.recvfrom(1024)

# print reply
print("Server:", reply.decode())

# close client
client_socket.close()