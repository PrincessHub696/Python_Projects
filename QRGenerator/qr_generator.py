import qrcode

data = input("Введите текст или ссылку для QR-кода: ")
img = qrcode.make(data)
img.save("qrcode.png")
print("QR-код сохранен как qrcode.png")