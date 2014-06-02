#gui unit tests !
import unittest
from game import Game
from GUI_process_fun import *



class TestMonopolyGUI(unittest.TestCase):
    def ttestRegistration(self):#prints on console
        game = Game()
        self.assertEqual(register_player(game),None)
        self.assertEqual(game.get_all_players(),['kirakis'])
        self.assertEqual(len(game.player_list),1)
        register_player(game)#gosho false
        register_player(game)#gopeto True
        self.assertEqual(game.get_all_players(),['kirakis','gopeto'])
        self.assertEqual(len(game.player_list),2)

    def ttestTrade(self):pass
    
    def ttestMourtage(self):
        game = Game()
        game.register_player('goshkoto')
        game.buy_building('goshkoto',1)
        self.assertEqual(mourtage(game,'goshkoto'),None)
        self.assertEqual(game.mourtage('goshkoto',1),False)
        game.unmourtage('goshkoto',1)              
        self.assertEqual(game.mourtage('goshkoto',1),True)
        self.assertEqual(game.player_balance('goshkoto'),1470)
        self.assertEqual(game._deck[1].is_mourtage(),True)
        
    def ttestUnmourtage(self):
        game = Game()
        game.register_player('goshkoto')
        game.buy_building('goshkoto',1)
        game.mourtage('goshkoto',1)
        self.assertEqual(unmourtage(game,'goshkoto'),None)
        self.assertEqual(game.mourtage('goshkoto',1),True)
        self.assertEqual(game.player_balance('goshkoto'),1470)
        
    def ttestBuild_house(self):
        game = Game()
        game.register_player('goshkoto')
        game.buy_building('goshkoto',1)
        game.buy_building('goshkoto',3)
        self.assertEqual(build_house(game,'goshkoto'),None)
        self.assertEqual(game.player_balance('goshkoto'),1330)
        self.assertEqual(game.house_count('goshkoto'),1)

    def ttestSell_house(self):
        game = Game()
        game.register_player('goshkoto')
        game.buy_building('goshkoto',1)
        game.buy_building('goshkoto',3)
        self.assertEqual(game.build_house('goshkoto',1),True)
        self.assertEqual(game.player_balance('goshkoto'),1330)
        self.assertEqual(game.house_count('goshkoto'),1)
        self.assertEqual(sell_house(game,'goshkoto'),None)
        self.assertEqual(game.house_count('goshkoto'),0)

    def ttestTrade(self):
        game = Game()
        game.register_player('goshkoto')
        game.register_player('kirakis')
        game.buy_building('goshkoto',1)
        game.buy_building('goshkoto',3)
        game.buy_building('kirakis',5)
        
        
        self.assertEqual(trade(game,'kirakis'), None)
        self.assertEqual(len(game.player_items_names('kirakis')),2)
        self.assertEqual(len(game.player_items_names('goshkoto')),1)
        #self.assertEqual(game.player_balance('kirakis'),800)
        #self.assertEqual(game.player_balance('goshkoto'),1000)

   def ttestBuy(self):#nr
        game = Game()
        game.register_player('goshkoto')
        game.register_player('kirakis')
        game.buy_building('goshkoto',1)
        game.buy_building('goshkoto',3)
        game.buy_building('kirakis',5)
   def testAuction(self): pass
        






if __name__ == '__main__':
    unittest.main()
