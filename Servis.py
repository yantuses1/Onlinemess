import socket
import threading

# Настройки сервера
HOST = 'localhost'  # Адрес хоста
PORT = 8080       # Порт для подключения клиентов

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            print(f"Принято сообщение: {message.decode('utf-8')}")
            broadcast(message, client_socket)
        except Exception as e:
            print(e)
            break

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            client.send(message)

clients = []
sockets_lock = threading.Lock()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print("Сервер запущен.")

while True:
    client_socket, addr = server_socket.accept()
    with sockets_lock:
        clients.append(client_socket)
    print(f"Подключился новый клиент: {addr}")
    thread = threading.Thread(target=handle_client, args=(client_socket,))
    thread.start()