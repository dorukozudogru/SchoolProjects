CompetitorName = []

numberOfTeams = int(input("Please enter the number of the teams: "))
count = 0

CompetitorScores = [[0 for i in range(numberOfTeams)] for j in range(6)]

while count < numberOfTeams:
    CompetitorName.append(input("Please enter the competitor's name: "))
    count = count + 1
    for i in range (5):
        CompetitorScores[count][i] = int(input("Please enter the score: "))
        while CompetitorScores[count][i] < 0 or CompetitorScores[count][i] > 100:
            CompetitorScores[count][i] = int(input("Please re-enter the score: "))


for i in range(numberOfTeams):
    for j in range