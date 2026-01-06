class NewRecord:
    def __init__(self, key: int, item1: int, item2: int):
        self.Key = key
        self.Item1 = item1
        self.Item2 = item2

def Initialise():
    global HashTable
    global Spare
    
    for i in range(200):
        HashTable.append(NewRecord(-1, -1, -1))
        
    for i in range(100):
        Spare.append(NewRecord(-1, -1, -1))

def CalculateHash(key: int):
    return int(key) % 200

def InsertIntoHash(record: NewRecord):
    global HashTable
    global Spare
    
    calculatedHash = CalculateHash(record.Key)
    if HashTable[calculatedHash].Key != -1:
        for i in range(100):
            if Spare[i].Key == -1:
                Spare[i] = record
                break
    else:
        HashTable[calculatedHash] = record

def CreateHashTable():
    try:
        file = open("G12/may-june-2025-42/HashData.txt", "r")

        for line in file:
            TempData = line.strip().split(",")
            InsertIntoHash(NewRecord(TempData[0], TempData[1], TempData[2]))

        file.close()
        
    except Exception as e:
        print("File cannot be opened!", e)
    
def PrintSpare():
    global Spare

    for i in range(len(Spare)):
        if Spare[i].Key != -1:
            print(Spare[i].Key)

HashTable = []
Spare = []

Initialise()
CreateHashTable()
PrintSpare()