teams = [""] * 3
results = [[0 for i in range(4)] for j in range(len(teams))]
highest_points = [0]
highest_points_team = [""]

games_played = int(input("Enter the number of games played: "))
while games_played <= 0 or games_played > 18:
    print("Invalid input. Please enter a number between 1 and 18.")
    games_played = int(input("Enter the number of games played: "))
    
for i in range(len(teams)):
    teams[i] = input("Enter the name of team: ")
    results[i][0] = int(input("Enter the number of wins for team: "))
    results[i][1] = int(input("Enter the number of draws for team: "))
    results[i][2] = int(input("Enter the number of losses for team: "))
    results[i][3] = results[i][0] * 3 + results[i][1] * 1 + results[i][2] * 0
    
    while results[i][0] + results[i][1] + results[i][2] != games_played:
        print("Invalid input. The total number of wins, draws, and losses must equal the number of games played.")
        results[i][0] = int(input("Enter the number of wins for team: "))
        results[i][1] = int(input("Enter the number of draws for team: "))
        results[i][2] = int(input("Enter the number of losses for team: "))
        results[i][3] = results[i][0] * 3 + results[i][1] * 1 + results[i][2] * 0
        
for i in range(len(results)):
    for j in range(len(results) - 1):
        if results[j][3] < results[j + 1][3]:
            results[j], results[j + 1] = results[j + 1], results[j]
            teams[j], teams[j + 1] = teams[j + 1], teams[j]
            
for i in range(len(results)):
    if results[i][3] > highest_points[0]:
        highest_points = [results[i][3]]
        highest_points_team = [teams[i]]
    elif results[i][3] == highest_points[0]:
        highest_points_team.append(teams[i])
    
print("The team with the highest points is/are:")
for i in range(len(highest_points_team)):
    print(highest_points_team[i])
    
print("'-> with the highest points of " + str(highest_points[0]))