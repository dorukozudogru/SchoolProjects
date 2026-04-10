class Bird():
    def __init__(self, Species, DistancePerHour):
        self.DistancePerHour = DistancePerHour #Real
        self.Species = Species #String
        self.XPosition = 500.0 #Real
        self.YPosition = 500.0 #Real

    def GetSpecies(self):
        return self.Species
    def GetPosition(self):
        Position = f"X = {self.XPosition} Y = {self.YPosition}" 
        return Position
    def Move(self, Dirr, Time):
        DistanceTraveled = self.DistancePerHour/60 * Time
        if Dirr == "N":
            self.YPosition += DistanceTraveled
        elif Dirr == "S":
            self.YPosition -= DistanceTraveled
        elif Dirr == "E":
            self.XPosition += DistanceTraveled
        elif Dirr == "W":
            self.XPosition -= DistanceTraveled

Bird1 = Bird("Cockatiel", 71.0)
Bird2 = Bird("Macaw", 56.0)

print(f"Bird 1 is of species: {Bird1.GetSpecies()} and is in position: {Bird1.GetPosition()}")
print(f"Bird 2 is of species: {Bird2.GetSpecies()} and is in position: {Bird2.GetPosition()}")
result = input("Pick which bird to move by entering 1 or 2: ")
if result == "1":
    Bird1.Move(input("Enter N, E, W or S to determine in which direction to move the bird: "), float(input("Enter the time the bird flew for to the nearest minute: ")))
elif result == "2":
    Bird2.Move(input("Enter N, E, W or S to determine in which direction to move the bird: "), float(input("Enter the time the bird flew for to the nearest minute: ")))

print(f"Bird 1 is now in position: {Bird1.GetPosition()}")
print(f"Bird 2 is now in position: {Bird2.GetPosition()}")

