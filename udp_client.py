import socket

# 1. Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. Send message
server_address = ('127.0.0.1', 12345)
message = input("Enter message: ")
client_socket.sendto(message.encode(), server_address)

# 3. Receive response
data, _ = client_socket.recvfrom(1024)
print("[Server Echo]:", data.decode())

# 4. Close socket
client_socket.close()
