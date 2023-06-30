import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 8080
server_socket.bind((host, port))
server_socket.listen(1)

client_socket, addr = server_socket.accept()

while True:
    data = client_socket.recv(64).decode()
    if not data:
        break
    print(data)

client_socket.close()
server_socket.close()
