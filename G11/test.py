file = open("G11/file-2.txt", "r")

readContent = file.readline()

while len(readContent) > 0:
    readContent = file.readline()
    print(readContent)

file.close()