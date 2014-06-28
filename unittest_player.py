import unittest
import random
#from game import Game
from global_variables import CHANCE, COMMUNITY_CHEST, LIST_OF_BUILDINGS
from building import *
from map import *
from game import Game
from player import Player


class Player_tests(unittest.TestCase):

    def testerplay(self):
        player = Player('pesho')
        self.assertEqual(player.player_budget(), 1500)
        self.assertEqual(player.get_picture(), [None, 0])
        self.assertEqual(player.playername(), 'pesho')
        self.assertEqual(player.jail(), False)
        player.change_jail(True)
        self.assertEqual(player.jail(), True)
        self.assertEqual(player.move_from_to(5), [0, 5])
        player.add_items(building('Mediterranean Ave.',  'Purple', 60,
                                  50, 2, 10,     30,     90,  160,   250))
        player.add_items(building('Baltic Ave.',         'Purple', 60,
                                  50, 4, 20,     60,    180,  320,   450))
        self.assertEqual(player.has_line('Purple')[0], True)
        player.add_money(52)
        self.assertEqual(player.player_budget(), 1552)

        player.add_items(building('READING RAILROAD', 'STATION', 200, 25))
        self.assertEqual(player.has_line('STATION')[1], 1)
        self.assertEqual(player.house_and_hotels_counter(), [0, 0])

if __name__ == '__main__':
    unittest.main()
