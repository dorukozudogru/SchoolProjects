file = open("students.txt","w")
for i in range(3):
    name = input("Please enter a name: ")
    file.write(name + "\n")
file.close()

file = open("students.txt","r")
print(file.read())
file.close()
