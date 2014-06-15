import unittest
import random
#from game import Game
from global_variables import CHANCE,COMMUNITY_CHEST,LIST_OF_BUILDINGS
from building import *
from map import *
from game import Game
from player import Player

import pdb
class Map_tests(unittest.TestCase):
    def testGameFee(self):
        game = Game()
        
        
       
        game.register_player('kirakis')
        game.register_player('goshko1')

        self.assertEqual(game.buy_building(0,0),False)
        self.assertEqual(game.buy_building(1,0),True)
        self.assertEqual(game.buy_building(10,0),False)
        self.assertEqual(game.buy_building(11,0),True)
        #self.assertEqual(game.buy_building(1,0),True)
        self.assertEqual(str(game.mapa[1].owner.player_name),'kirakis')
        #self.assertEqual(game.players[0].budget,'kirakis')
        
        game.current_player=1
        for i in range(0):
            print(i,game.mapa[i].owner)
        print(game.players[0].get_items())
        for i in range(0):
            print(i,game.mapa[i].color_street)
        self.assertEqual(game.take_fee(1),'pay_player')
        self.assertEqual(game.players[1].budget,1700)
#ready
if __name__ == '__main__':
    pdb.run(unittest.main())
