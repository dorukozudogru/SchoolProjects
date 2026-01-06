# Writing to the file
file = open("G11/Classwork Answers/students.txt", "w")

for i in range(3):
    name = input(f"Enter name of student {i + 1}: ")
    file.write(name + "\n")

# Reading from the file
file = open("G11/Classwork Answers/students.txt", "r")
print("\nContents of students.txt:")
for line in file:
    print(line.strip())