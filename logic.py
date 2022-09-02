def getGameOutcome(firstTeamScore, secondTeamScore):
    """ 
    Receives two scores, 
    Return the difference, if > 0 win, if < 0 loss else it's a draw
    """
    return int(firstTeamScore) - int(secondTeamScore)


def retrieveTeams(matchGame):
    """
    Receives a game with teams and their scores separated by a comma
    Returns a tupple of ( team_1, team_2, gameOutCome)
    """
    twoTeamsWithScores = matchGame.split(',') 
    index_score1 = twoTeamsWithScores[0].rindex(" ") + 1
    index_score2 = twoTeamsWithScores[1].rindex(" ") + 1
    
    team_1  = twoTeamsWithScores[0][:index_score1].strip()   #Get team 1's name
    score_1 = twoTeamsWithScores[0][index_score1:]
    team_2  = twoTeamsWithScores[1][:index_score2].strip() 
    score_2 = twoTeamsWithScores[1][index_score2:]
    
    scoreOutcome = getGameOutcome(score_1, score_2)
    
    return (team_1, team_2, scoreOutcome)


def allocatePoints(matchGame, teamsList):
    """
    Receives the match results and immediately allocates points accordingly
    - if team 1 won, allocate 3 pts
    - if team 1 lose allocate 0 pts
    - Otherwiae 1 pts allocated. 
    """
    (team_1, team_2, scoreOutcome) = retrieveTeams(matchGame)
    
    if(team_1 not in teamsList):
        teamsList[team_1]=[0,0,0,0,0] #Keps track of Match Played, Won, Lost, Draw and Points
        
    if(team_2 not in teamsList):
        teamsList[team_2]=[0,0,0,0,0]   
    
    #Now having the assurance that they're on the list
    if(team_1 in teamsList and team_2 in teamsList):
        teamsList[team_1][0]+=1
        teamsList[team_2][0]+=1
        
        if(scoreOutcome > 0): #Team 1, won
           teamsList[team_1][1]+=1 #Increase wins for tean 1
           teamsList[team_2][2]+=1 #Increase loses for tean 2
        elif(scoreOutcome < 0): #Team 1, lost
            teamsList[team_1][2]+=1 #Increase loses for tean 1
            teamsList[team_2][1]+=1 #Increase win for tean 2
        else:
            teamsList[team_1][3]+=1 #Increase draws
            teamsList[team_2][3]+=1 #Increase draws

    #Calculating points
    for team in teamsList: 
        teamsList[team][4] = teamsList[team][1]*3+teamsList[team][3]  # Multiply wins by 3 and simply add draws
     
            
def displayTeamsLogStanding(teamsList):
    """Display the leauge standing"""
    indexRanking = 1 
    previousPoints = 0
    sameRank = 1
    points = 0
    print("\n\n")
    for team in (sorted(teamsList.items(), key = lambda points: points[1][4],reverse=True)):
        points = team[1][4]
        if(points != previousPoints): sameRank = indexRanking
        isOnePoint ="pts"
        if(points == 1): isOnePoint = "pt"
        ouput = f'{sameRank}. {team[0]}, {points} {isOnePoint}'
        print(ouput)
        indexRanking += 1
        previousPoints = points