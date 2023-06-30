import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname(socket.gethostname())
port = 8080
client_socket.connect((host, port))

while True:
    message = input('Enter Message: ')
    client_socket.send(message.encode())

client_socket.close()
