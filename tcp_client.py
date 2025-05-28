import socket

HOST = '127.0.0.1'
PORT = 12345

# 1. Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Connect
client_socket.connect((HOST, PORT))

# 3. Send and receive
message = input("Enter message: ")
client_socket.sendall(message.encode())

data = client_socket.recv(1024)
print("[Server Echo]:", data.decode())

# 4. Close
client_socket.close()
