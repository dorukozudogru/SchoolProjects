readList = []

def ReadData():
    fileName = input("Please enter a file name: ")
    with open(fileName, "r") as file:
        for line in file:
            readList.append(line)
    return readList

def SplitData(dataArray):
    red = []
    green = []
    blue = []
    orange = []
    yellow = []
    pink = []
    
    for item in dataArray:
        temp = item.strip().split(",")
        if temp[1] == "red":
            red.append(temp[0])
        elif temp[1] == "green":
            green.append(temp[0])
        elif temp[1] == "blue":
            blue.append(temp[0])
        elif temp[1] == "orange":
            orange.append(temp[0])
        elif temp[1] == "yellow":
            yellow.append(temp[0])
        elif temp[1] == "pink":
            pink.append(temp[0])

        StoreData(red, "Red.txt")
        StoreData(green, "Green.txt")
        StoreData(blue, "Blue.txt")
        StoreData(orange, "Orange.txt")
        StoreData(yellow, "Yellow.txt")
        StoreData(pink, "Pink.txt")
    
def StoreData(dataToStore, fileName):
    try:
        with open("/Users/dorukozudogru/Projects/IPS/G12/may-june-2025-41/" + fileName, "w") as file:
            for item in dataToStore:
                file.write(item + "\n")
    except:
        print("Something Wrong!")
            

readData = ReadData()
print("The array is: ", readData)
SplitData(readData)