from logic import allocatePoints, displayTeamsLogStanding
        

if __name__ == '__main__':
    teamsList = {}
    
    N=int(input("Enter the number of matches: "))
    for i in range(N):
        matchGame = input()
        allocatePoints(matchGame, teamsList)
        
    displayTeamsLogStanding(teamsList)
