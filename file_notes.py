file = open("notes.txt", "w")
file.write("Привет, мир!")
file.close()

file = open("notes.txt", "r")
print(file.read())
file.close()