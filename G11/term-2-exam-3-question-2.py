def CreateFiles (fileName, numOfFiles):
    count = 1
    while count <= numOfFiles:
        if count < 10:
            newFileName = fileName + ".00" + str(count) + ".txt"
        else:
            newFileName = fileName + ".0" + str(count) + ".txt"
        
        print(f"Creating: {newFileName}")
        
        file = open(newFileName, "w")
        file.write("This is File " + newFileName)
        file.close()
        
        count+=1
        
# nameOfTheFile = input("Please enter a file name: ")
# number = int(input("Please enter a number: "))
CreateFiles("Atharva", 3)
print("Creating files has been finished!")