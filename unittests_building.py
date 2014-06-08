import unittest
import random
#from game import Game
from global_variables import CHANCE,COMMUNITY_CHEST,LIST_OF_BUILDINGS
from building import *
from map import *
from game import Game
from player import Player

class Building_tests(unittest.TestCase):
    def testBuildings(self): 
        test_building = building('Mediterranean Ave.',  'Purple', 60,
                         50, 2, 10,     30,     90,  160,   250)
        test_building2 = building('Baltic Ave.',         'Purple', 60,
                  50, 4, 20,     60,    180,  320,   450)
        test_player = Player('kirakis')
        gosho = Player('goshko')
        self.assertEqual(test_building.get_color(),'Purple')
        test_building.mourtage(test_player)
        self.assertEqual(test_player.player_budget(),1500)
        test_building.buy_building(test_player,0)
        self.assertEqual(test_player.player_budget(),1440)
        test_building.mourtage(test_player)
        self.assertEqual(test_player.player_budget(), 1464)
        test_building.unmourtage(test_player)
        self.assertEqual(test_player.player_budget(), 1434)
        # ne mi trqbva da raboti
        self.assertEqual(len(test_building.all_players()), 1)
        test_building.delete_player(test_player)
        self.assertEqual(len(test_building.all_players()), 0)
        # auction prices for building
        test_building2.buy_building(test_player,200)
        self.assertEqual(test_player.player_budget(), 1234)
        #bancrupt
        
        go_go = building('GO', 'FREE', 0, 0, 0)
        go_go.buy_building(gosho)
        self.assertEqual(test_player.player_budget(), 1234)
        self.assertEqual(gosho.player_budget(), 1500)
        self.assertEqual(test_building.have_owner(),test_player)
        test_building.change_owner(gosho)
        self.assertEqual(test_building.have_owner(),gosho)
        test_building.change_owner(test_player)
        self.assertEqual(test_building2.have_owner(),test_player)
        test_player.add_items(test_building2)
        test_player.add_items(test_building)
        #print(test_player.get_items())

        go_go.bancrupt(test_player)
        #print(gosho.get_items())
        ch = building('Ventnor Ave.', 'Yellow',  260,
                  150, 22, 110,     330,  800,   975,  1150)
        ch.buy_building(test_player)
        test_player.add_items(ch)
        #print(test_player.get_items())
        ch.bancrupt(gosho)
        #print(test_player.get_items())
    #def testBuild_sell(self):
        self.assertEqual(test_building.house_and_hotels_list(),[0,0])
        ch.change_owner(test_player)
        self.assertEqual(ch.have_owner(),test_player) #;)
        self.assertEqual(test_building.build_house(gosho),False)
        test_player.pay_money(8)
        self.assertEqual(test_player.player_budget(), 3700)

        self.assertEqual(test_building.build_house(test_player),True)
        self.assertEqual(test_building.build_house(test_player),True)
        self.assertEqual(test_building.build_house(test_player),True)
        self.assertEqual(test_building.build_house(test_player),True)
        self.assertEqual(test_building.house_and_hotels_list(),[4,0])
        self.assertEqual(test_building.build_house(test_player),True)
        self.assertEqual(test_building.house_and_hotels_list(),[0,1])
        self.assertEqual(test_building.build_house(test_player),False)
        self.assertEqual(test_building.build_house(test_player),False)
        self.assertEqual(test_player.player_budget(), 3450)
        self.assertEqual(test_building.sell_house(test_player),True)
        self.assertEqual(test_building.sell_house(test_player),True)
        self.assertEqual(test_building.sell_house(test_player),True)
        self.assertEqual(test_building.sell_house(test_player),True)
        self.assertEqual(test_building.sell_house(test_player),True)
        self.assertEqual(test_building.sell_house(test_player),False)

        self.assertEqual(test_player.player_budget(), 3550)
        self.assertEqual(gosho.player_budget(), 2734)
        self.assertEqual(test_building.take_fee(gosho),'fee')
        self.assertEqual(gosho.player_budget(), 2732)



if __name__ == '__main__':
    unittest.main()
