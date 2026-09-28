import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 8080))
print("Вы подключились к серверу!")

while True:
    message = input("Вы: ")
    client.send(message.encode("utf-8"))

    response = client.recv(1024).decode("utf-8")
    if not response:
        break
    print(f"Сервер: {response}")

client.close()