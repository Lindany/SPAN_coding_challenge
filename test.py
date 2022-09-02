from logic import *
import unittest

class Testing(unittest.TestCase):
    def test_gameOutcome(self):
        assert getGameOutcome(3,1) > 0
        assert getGameOutcome(2,4) < 0
        self.assertEqual(getGameOutcome(1,1), 0)
        
    def test_retrieveTeams(self):
        matchGame = "Tarantulas 1, FC Awesome 0"
        self.assertEqual(retrieveTeams(matchGame),("Tarantulas","FC Awesome",1) )
        
        matchGame2 = "Lions 3, Snakes 3"
        self.assertEqual(retrieveTeams(matchGame2),("Lions","Snakes",0) )

    def test_allocatePoints(self):
        teamsList = {}
        matchGame = "Tarantulas 1, FC Awesome 0"
        allocatePoints(matchGame, teamsList)
        self.assertEqual(teamsList,{"Tarantulas":[1,1,0,0,3],"FC Awesome":[1,0,1,0,0]} )
        
        matchGame2 = "Tarantulas 3, Snakes 1"
        allocatePoints(matchGame2, teamsList)
        self.assertEqual(teamsList,{"Tarantulas":[2,2,0,0,6],"FC Awesome":[1,0,1,0,0],"Snakes":[1,0,1,0,0]}  )

if __name__ == '__main__':
    unittest.main()