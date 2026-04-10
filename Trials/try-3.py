def ReadData():
    datalist = [0] * 45
    try:
        maindata = open("/Users/dorukozudogru/Projects/IPS/Trials/Data.txt","r")
        for i in range(0,45):
            line = str(maindata.readline())
            line = line.strip("\n")
            datalist[i] = line
        maindata.close()
        return datalist
    except:
        print("Error")


def FormatString(Array):
    string = ""
    for i in range(0,len(Array)):
        string = string + Array[i] + " "
    return string


def CompareStrings(String1, String2):
        for i in range(min(len(String1), len(String2))):
            if String1[i] > String2[i]:
                return 1
            else:
                return 2


def Bubble(Array):
    for i in range(0,len(Array) - 1):
        if CompareStrings(Array[i],Array[i+1]) == 1:
            Temp = Array[i]
            Array[i] = Array[i+1]
            Array[i+1] = Temp
    return Array


Array = ReadData()
print(FormatString(Array))
SortedList = Bubble(Array)
print(FormatString(SortedList))