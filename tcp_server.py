import socket

HOST = '127.0.0.1'  # Localhost
PORT = 12345        # Non-privileged port > 1023

# 1. Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Bind
server_socket.bind((HOST, PORT))

# 3. Listen
server_socket.listen()
print(f"[+] Server listening on {HOST}:{PORT}")

# 4. Accept connection
conn, addr = server_socket.accept()
print(f"[+] Connected by {addr}")

# 5. Receive and send data
while True:
    data = conn.recv(1024)
    if not data:
        break
    print("[Client]:", data.decode())
    conn.sendall(data)  # Echo back

# 6. Close
conn.close()
server_socket.close()
