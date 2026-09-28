import socket

# Используем IPv4 и TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Сервер работает на личном ПК
server.bind(("localhost", 8080))

# Слушаем подключения
server.listen(1)
print("Сервер запущен. Ожидание клиента...")

# Принимаем клиента
client, address = server.accept()
print(f"Клиент подключился: {address}")

# Общение с клиентом
while True:
    message = client.recv(1024).decode("utf-8")
    if not message:
        break
    print(f"Клиент: {message}")

    response = input("Вы: ")
    client.send(response.encode("utf-8"))

client.close()
server.close()