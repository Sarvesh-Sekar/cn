import socket
import threading

# Server configuration
TCP_PORT = 12345
UDP_PORT = 12346
BUFFER_SIZE = 1024

# Dictionary to store connected TCP clients
clients = []

# TCP handler for each client
def handle_tcp_client(client_socket, client_address):
    print(f"TCP client connected from {client_address}")
    clients.append(client_socket)

    try:
        while True:
            message = client_socket.recv(BUFFER_SIZE).decode('utf-8')
            if not message:
                break
            print(f"Received TCP message from {client_address}: {message}")

            # Broadcast message to all other TCP clients
            for client in clients:
                if client != client_socket:
                    client.sendall(f"{client_address} says: {message}".encode('utf-8'))
    except ConnectionResetError:
        print(f"TCP client disconnected from {client_address}")
    finally:
        clients.remove(client_socket)
        client_socket.close()

# UDP handler to receive broadcast messages
def udp_handler():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(('0.0.0.0', UDP_PORT))
    print(f"UDP server listening on port {UDP_PORT}")

    while True:
        message, client_address = udp_socket.recvfrom(BUFFER_SIZE)
        print(f"Received UDP message from {client_address}: {message.decode('utf-8')}")

# Main server function to handle TCP connections
def start_tcp_server():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind(('0.0.0.0', TCP_PORT))
    tcp_socket.listen(5)
    print(f"TCP server listening on port {TCP_PORT}")

    # Start UDP listener in a separate thread
    threading.Thread(target=udp_handler, daemon=True).start()

    while True:
        client_socket, client_address = tcp_socket.accept()
        threading.Thread(target=handle_tcp_client, args=(client_socket, client_address)).start()

# Start the server
start_tcp_server()
