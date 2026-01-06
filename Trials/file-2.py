lineOfText = input("Please enter something: ")
file = open("file-2.txt", "w")
file.write(lineOfText)
file.close()

lenOfText = len(lineOfText)
print(lineOfText.lower(), " ", lenOfText)

file = open("lower-case.txt", "w")
file.write(lineOfText.lower())
file.close()
