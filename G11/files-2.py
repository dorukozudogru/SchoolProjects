# file = open("G11/file-2.txt", "r")
# line = file.read()
# print(line)
# file.close()

file = open("G11/file-2.txt", "r")
line = file.readline()
print(line)

while len(line) > 0:
    line = file.readline()
    if "1" not in line:
        print("there is no 1 in this line")
    else:
        print(line)

file.close()