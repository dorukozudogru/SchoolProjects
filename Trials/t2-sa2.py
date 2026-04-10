Animal = [None] * 20
Colour = [None] * 10
AnimalTopPointer = 0
ColourTopPointer = 0

def PushAnimal(DataToPush):
    global Animal, AnimalTopPointer
    if AnimalTopPointer == 20:
        return False
    else:
        Animal[AnimalTopPointer] = DataToPush
        AnimalTopPointer = AnimalTopPointer + 1
        return True

def PopAnimal():
    ReturnData = None
    global Animal, AnimalTopPointer
    if AnimalTopPointer == 0:
        return ""
    else:
        ReturnData = Animal[AnimalTopPointer - 1]
        AnimalTopPointer = AnimalTopPointer - 1
        return ReturnData

def ReadData():
    global Animal, AnimalTopPointer
    try:
        animalfile = open("/Users/dorukozudogru/Projects/IPS/Trials/AnimalData.txt", "r")
        for line in animalfile:
            PushAnimal(line.rstrip())
        animalfile.close()
    except FileNotFoundError:
        print("animal file not here :(")
    try:
        colourfile = open("/Users/dorukozudogru/Projects/IPS/Trials/ColourData.txt", "r")
        for line2 in colourfile:
            PushColour(line2.rstrip())
        colourfile.close()
    except FileNotFoundError:
        print("colour file not here :(")


def PushColour(DataToPush):
    global Colour, ColourTopPointer
    if ColourTopPointer == 10:
        return False
    else:
        Colour[ColourTopPointer] = DataToPush
        ColourTopPointer = ColourTopPointer + 1
        return True

def PopColour():
    global Colour, ColourTopPointer
    ReturnData = None
    if ColourTopPointer == 0:
        return ""
    else:
        ReturnData = Colour[ColourTopPointer - 1]
        ColourTopPointer = ColourTopPointer - 1
        return ReturnData

def OutputItem():
    global Animal, AnimalTopPointer, Colour, ColourTopPointer
    animal = PopAnimal()
    colour = PopColour()
    if animal == "":
        print("No animal")
        PushColour(colour)
    elif colour == "":
        print("No colour")
        PushAnimal(animal)
    else:
        print(animal, colour)

ReadData()
OutputItem()
OutputItem()
OutputItem()
OutputItem()
