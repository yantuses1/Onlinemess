import socket
import threading

# Настройки клиента
SERVER_HOST = 'localhost'
SERVER_PORT = 8080

def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print(data.decode('utf-8'))
        except ConnectionResetError:
            break

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

try:
    while True:
        message = input("Введите сообщение: ")
        client_socket.sendall(message.encode('utf-8'))
except KeyboardInterrupt:
    pass
finally:
    client_socket.close()