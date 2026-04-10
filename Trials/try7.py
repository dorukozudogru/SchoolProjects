class Bird():
    def __init__(self, Species, DistancePerHour):
        self.DistancePerHour = DistancePerHour  # Real
        self.Species = Species  # String
        self.XPosition = 500  # Real
        self.YPosition = 500  # Real

    def GetSpecies(self):
        return self.Species

    def GetPosition(self):
        print("dsfdsfsd")
        Position = f"X = {self.XPosition} Y = {self.YPosition}"
        return Position

    def Move(self, Dirr, Time):
        DistanceTraveled = self.DistancePerHour / 60 * Time

        if Dirr == "N":
            self.YPosition += DistanceTraveled
        elif Dirr == "S":
            self.YPosition -= DistanceTraveled
        elif Dirr == "E":
            self.XPosition += DistanceTraveled
        elif Dirr == "W":
            self.XPosition -= DistanceTraveled


Bird1 = Bird("Cockatiel", 71)
Bird2 = Bird("Macaw", 56)

Bird1.GetPosition()

print(f"Bird 1 is of species: {Bird1.GetSpecies()} and is in position: {Bird1.GetPosition()}")