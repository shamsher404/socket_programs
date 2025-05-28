import socket

# 1. Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. Bind to IP and port
server_socket.bind(('127.0.0.1', 12345))
print("[+] UDP Server listening on port 12345...")

# 3. Receive messages
while True:
    data, addr = server_socket.recvfrom(1024)  # Buffer size
    print(f"[{addr}] says: {data.decode()}")
    server_socket.sendto(data, addr)  # Echo back
