class Horse:
    def __init__(self, name, maxfenceheight, percentagesuccess):
        self.name = name
        self.MaxFenceHeight = maxfenceheight
        self.PercentageSuccess = percentagesuccess

    def getName(self):
        return self.name
    def getMaxFenceHeight(self):
        return self.MaxFenceHeight

def success(loop1, loop2, Course, Horses):
    while loop1 < 2:
        while loop2 < 4:
            if (Course[i].height) < Horses[b].MaxFenceHeight:
                if Course[i].risk == 1:
                    newpercentagesuccess = Horses[b].PercentageSuccess * 1
                    return round(newpercentagesuccess)
                elif Course[i].risk == 2:
                    newpercentagesuccess = Horses[b].PercentageSuccess * 0.9
                    return round(newpercentagesuccess)
                elif Course[i].risk == 3:
                    newpercentagesuccess = Horses[b].PercentageSuccess * 0.8
                    return round(newpercentagesuccess)
                elif Course[i].risk == 4:
                    newpercentagesuccess = Horses[b].PercentageSuccess * 0.7
                    return round(newpercentagesuccess)
                elif Course[i].risk == 5:
                    newpercentagesuccess = Horses[b].PercentageSuccess * 0.6
                    return round(newpercentagesuccess)
            else:
                break
            break
        break


class Fence:
    def __init__(self,height, risk):
        # self.height = height Integer
        # self.risk = risk Integer
        self.height = height
        self.risk = risk

    def getHeight(self):
        return self.height
    def getRisk(self):
        return self.risk



Horses = []

Course = []

Beauty = Horse("Beauty", 150, 72)
Jet = Horse("Jet", 160, 65)

Horses.append(Beauty)
Horses.append(Jet)
print(Horses[0].name, Horses[0].MaxFenceHeight)
print(Horses[1].name, Horses[1].MaxFenceHeight)

counter = 0

while counter < 4:
    height = float(input(f"enter height for fence {counter + 1}: "))
    if 69 < height < 181:
        risk = int(input(f"enter risk for fence {counter + 1}: "))
        if 0 < risk < 6:
            Course.append(Fence(height, risk))
            counter += 1

        else:
            print("risk must be between 1 and 5")
    else:
        print("height must be between 70 and 180")

HorsePList1 = []
HorsePList2 = []
ListTotal = 0

for b in range(0, 2):
    for i in range(0, 4):
        if success(b,i,Course,Horses) is  not None:
            print('the horse', Horses[b].name, 'has a success rate of', success(b,i,Course,Horses), '% at fence', i+1)
            if b == 0:
                HorsePList1.append(success(b,i,Course,Horses))
            else:
                HorsePList2.append(success(b,i,Course,Horses))
        else:
            print('fence', i+1, 'is too tall for', Horses[b].name)
    if b == 0 and len(HorsePList1) == 4:
        for j in range(len(HorsePList1)):
            ListTotal = ListTotal + HorsePList1[j]
        print("the average for", Horses[b].name, 'is', ListTotal/len(HorsePList1), "%")
    elif b == 1 and len(HorsePList2) == 4:
        for k in range(len(HorsePList2)):
            ListTotal = ListTotal + HorsePList2[k]
        print("the average for", Horses[b].name, 'is', ListTotal/len(HorsePList2), "%")
    else:
        print(Horses[b].name, 'has not jumped all 4 fences')