import unittest
import random
#from game import Game
from global_variables import CHANCE,COMMUNITY_CHEST,LIST_OF_BUILDINGS
from building import *
from map import *
from game import Game
from player import Player

class Map_tests(unittest.TestCase):
    def ttestmap(self):  
        player = Player('pesho')
        self.assertEqual(player.player_budget(),1500)
        self.assertEqual(player.get_picture(),[None,0])
        self.assertEqual(player.playername(),'pesho')
        self.assertEqual(player.jail(),False)
        player.change_jail(True)
        self.assertEqual(player.jail(),True)
        self.assertEqual(player.move_from_to(5),[0,5])
        player.add_items(building('Mediterranean Ave.',  'Purple', 60,
                  50, 2, 10,     30,     90,  160,   250))
        player.add_items(building('Baltic Ave.',         'Purple', 60,
                  50, 4, 20,     60,    180,  320,   450))



#bug tracking game.roll_dice_new_edition
 
game = Game()
game.register_player('peshko12')
game.register_player('goshkoto')
game.register_player('joro1234')
      
       

for i in range(10):
    game.roll_dice()
    print('###########')







if __name__ == '__main__':
    unittest.main()
