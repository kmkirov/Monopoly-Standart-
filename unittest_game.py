import unittest
import random
#from game import Game
from global_variables import CHANCE, COMMUNITY_CHEST, LIST_OF_BUILDINGS
from building import *
from map import *
from game import Game
from player import Player
CRTL SHIFT R pep 8


class Game_tests(unittest.TestCase):

    def testGame(self):
        game = Game()
        # self.assertNotEqual(game.roll_dice(),[range(2,2),(True|False)])
        self.assertEqual(game.register_player('goshko'), True)
        self.assertEqual(game.register_player('peshko'), True)
        self.assertEqual(game.register_player('goshko'), False)
        self.assertEqual(game.register_player('pesh'), False)
        self.assertEqual(len(game.all_player()), 2)
        self.assertEqual(game.current_player, 0)
        self.assertEqual(game.current_position(), 0)
        self.assertEqual(game.player_Free(), True)
        game.end_turn()

        self.assertEqual(game.current_player, 1)
        self.assertEqual(game.current_player_index(), 1)
        self.assertEqual(game.icon(), 1)
        self.assertEqual(game.render_name_and_budget(), ['peshko', 1500])
        self.assertEqual(game.at(3), 'Baltic Ave.')

        self.assertEqual(game.buy_building(1, False), True)
        self.assertEqual(len(game.players[1].get_items()), 1)
        self.assertEqual(len(game.players[0].get_items()), 0)
        game.end_turn()
        self.assertEqual(game.current_player, 0)
        self.assertEqual(game.buy_building(3, False), True)
        self.assertEqual(len(game.players[0].get_items()), 1)

        # trader
        self.assertEqual(game.players[1].player_budget(), 1440)
        self.assertEqual(game.trade_buildings(
            1, [1], 2, 'peshko', [23], 123), False)
        self.assertEqual(game.trade_buildings(
            1, [3], 1000, 'peshko', [0], 123), True)
        self.assertEqual(len(game.players[1].get_items()), 2)
        self.assertEqual(game.players[1].player_budget(), 2317)
        self.assertEqual(game.players[0].player_budget(), 563)
        self.assertEqual(len(game.players[0].get_items()), 0)
        # mourtage
        self.assertEqual(game.mourtage(1), False)
        game.end_turn()
        self.assertEqual(game.mourtage(1), True)
        self.assertEqual(game.players[1].player_budget(), 2341)
        self.assertEqual(game.unmourtage(1), True)
        self.assertEqual(game.players[1].player_budget(), 2311)
        # build sell
        self.assertEqual(game.build_house(1), True)
        self.assertEqual(game.build_house(3), True)
        self.assertEqual(game.build_house(33), False)
        self.assertEqual(game.sell_house(3), True)
        self.assertEqual(game.sell_house(3), False)
        # jail test posle

        # community chest
        self.assertEqual(game.players[1].player_budget(), 2231)
        self.assertEqual(game.community_chest(
            game.players[1]), 'Advance to Go (collect $200)')
        self.assertEqual(game.current_player, 1)
        self.assertEqual(game.players[1].player_budget(), 2431)
        self.assertEqual(game.players[1].position, 0)
        self.assertEqual(game._comunity_chest_index, 1)
        #
        game._comunity_chest_index = 3
        self.assertEqual(game.community_chest(
            game.players[1]), 'Get out of jail free')
        self.assertEqual(game.players[0].player_budget(), 563)
        self.assertEqual(game.community_chest(
            game.players[1]), 'It is your birthday Collect $10 from each player')
        self.assertEqual(game.players[0].player_budget(), 553)
        self.assertEqual(game.players[1].player_budget(), 2441)  # t,n
        # chance
        self.assertEqual(
            game.Chance(game.players[1]), 'Advance to Go (collect $200)')
        self.assertEqual(game.players[1].player_budget(), 2641)

        self.assertEqual(game.move_player_by_rolled(11)[1], 11)

        # for i in range(12): #psevdo test za sintaksis
        #    game.community_chest(game.players[1])
        #    game.Chance(game.players[1])

if __name__ == '__main__':
    unittest.main()
