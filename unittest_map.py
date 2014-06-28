import unittest
import random
#from game import Game
from global_variables import CHANCE,COMMUNITY_CHEST,LIST_OF_BUILDINGS
from building import *
from map import *
from game import Game
from player import Player

class Map_tests(unittest.TestCase):
    def testmap(self):  
        player = Player('pesho')
        player2= Player('pesho1')
        
        map1 = mapa()
        self.assertEqual(map1.buy_building(0,player,0),False)#in frobiden
        self.assertEqual(map1.buy_building(1,player,0),True)
        self.assertEqual(map1.buy_building(1,player2,0),False)
        self.assertEqual(map1.buy_building(3,player2,0),True)
        map1.trade_buildings(player,[1],1200,player2,[0],0)
        self.assertEqual(player.player_budget(),240)
        self.assertEqual(player2.player_budget(),2640)
        self.assertEqual(player.get_items(),[])
        self.assertEqual(len(player2.get_items()),2)
        #mnogo stranno neshto sum napisal...
        position = player.move_from_to(0)[1]
        self.assertEqual(map1.move_player_by_roll(player,10), None)
        self.assertEqual(map1.move_player_to_position(player,9),38)

        # ne sum testval move

if __name__ == '__main__':
    unittest.main()
