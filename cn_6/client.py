import socket
import threading

# Server configuration
SERVER_IP = '127.0.0.1'
TCP_PORT = 12345
UDP_PORT = 12346
BUFFER_SIZE = 1024

# Function to handle receiving TCP messages
def receive_tcp_messages(tcp_socket):
    try:
        while True:
            message = tcp_socket.recv(BUFFER_SIZE).decode('utf-8')
            if not message:
                break
            print(f"\n[TCP] {message}")
    except ConnectionResetError:
        print("Disconnected from TCP server")
    finally:
        tcp_socket.close()

# Function to send messages via TCP
def send_tcp_messages(tcp_socket):
    while True:
        message = input("Enter message for TCP: ")
        tcp_socket.sendall(message.encode('utf-8'))

# Function to send messages via UDP
def send_udp_message():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        message = input("Enter message for UDP (broadcast): ")
        udp_socket.sendto(message.encode('utf-8'), (SERVER_IP, UDP_PORT))

# Main function to start the client
def start_client():
    # Connect to server via TCP
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect((SERVER_IP, TCP_PORT))
    print("Connected to TCP server")

    # Start TCP receiver and sender threads
    threading.Thread(target=receive_tcp_messages, args=(tcp_socket,), daemon=True).start()
    threading.Thread(target=send_tcp_messages, args=(tcp_socket,), daemon=True).start()

    # Start UDP sender thread
    threading.Thread(target=send_udp_message, daemon=True).start()

    # Keep the client running
    threading.Event().wait()

# Start the client
start_client()
