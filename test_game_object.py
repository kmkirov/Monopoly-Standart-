import unittest
import random
#from game import Game
from global_variables import CHANCE,COMMUNITY_CHEST,LIST_OF_BUILDINGS
from building import deck_building
from playing_deck import playing_deck
from game import Game
from player import Player

class TestMonopolyGameONLY(unittest.TestCase):
    def testGame1ss(self):
        game = Game()
        game.register_player('kirakis')
        game.register_player('goshko1')
        self.assertEqual(game.player_index('kirakis'),0)
        self.assertEqual(game.player_index('goshko1'),1)
        
        self.assertEqual(game.community_chest('kirakis'),'Advance to Go (collect $200)')
        self.assertEqual(game.player_position('kirakis'),0)
        self.assertEqual(game.can_pay('kirakis',1700),True)
        self.assertEqual(game.player_balance('kirakis'),1700)
        self.assertEqual(game.player_balance('goshko1'),1500)
        game._comunity_chest_index=4
        self.assertEqual(game.community_chest('kirakis'),'It is your birthday Collect $10 from each player')
        self.assertEqual(game.player_balance('kirakis'),1710)
        self.assertEqual(game.player_balance('goshko1'),1490)


        
        










if __name__ == '__main__':
    unittest.main()
