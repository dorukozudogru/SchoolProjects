CompetitorName = [""] * 5
CompetitorScore = [[0 for i in range(5)] for j in range(5)]
Points = [0] * 5

# Takes input for competitor names and scores,
# and calculates total points for each competitor
for i in range(5):
    CompetitorName[i] = input("Enter the name of competitor: ")
    for j in range(5):
        CompetitorScore[i][j] = int(input("Enter the " + str(j + 1) + " score of competitor: "))
        while CompetitorScore[i][j] < 0 or CompetitorScore[i][j] > 100:
            print("Invalid score. Please enter a score between 0 and 100.")
            CompetitorScore[i][j] = int(input("Enter the " + str(j + 1) + " score of competitor: "))
        Points[i] = Points[i] + CompetitorScore[i][j]
        
# Calculates the highest points scored for each event
HighestPoints = [0] * 5
HighestPointsNames = [""] * 5
for j in range(5):
    for i in range(5):
        if CompetitorScore[i][j] > HighestPoints[j]:
            HighestPoints[j] = CompetitorScore[i][j]
            HighestPointsNames[j] = CompetitorName[i]

# Displays the highest points scored for each event
# and the name of the competitor who scored it
for j in range(5):
    print("The highest points scored for event " + str(j + 1) + " is " + str(HighestPoints[j]) + " by " + HighestPointsNames[j])
    
# calculates the highest total points scored for the
# five events and outputs the names of the competitors
# with the highest total points scored for the five events.
for i in range(5):
    for j in range(5):
        if Points[i] > Points[j]:
            HighestTotalPoints = Points[i]
            HighestTotalPointsName = CompetitorName[i]
        elif Points[i] == Points[j]:
            HighestTotalPoints = Points[i]
            HighestTotalPointsName = CompetitorName[i]
print("The highest total points scored for the five events is " + str(HighestTotalPoints) + " by " + HighestTotalPointsName)