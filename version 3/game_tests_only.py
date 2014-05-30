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
        #comunity_chest + balance
        self.assertEqual(game.community_chest('kirakis'),'Advance to Go (collect $200)')
        self.assertEqual(game.player_position('kirakis'),0)
        self.assertEqual(game.can_pay('kirakis',1700),True)
        self.assertEqual(game.player_balance('kirakis'),1700)
        self.assertEqual(game.player_balance('goshko1'),1500)
        game._comunity_chest_index=4
        self.assertEqual(game.community_chest('kirakis'),'It is your birthday Collect $10 from each player')
        self.assertEqual(game.player_balance('kirakis'),1710)
        self.assertEqual(game.player_balance('goshko1'),1490)
        #roll dice
        self.assertIn(game.roll_dice()[0],range(2,13))
        self.assertIn(game.roll_dice()[1],[True,False])
        #test move_player_by rolled and new_position
        game.new_position('kirakis',10)
        self.assertEqual(game.player_position('kirakis'),10)
        game.move_player_by_rolled(10,'goshko1')
        self.assertEqual(game.player_position('goshko1'),10)
        #test items
        self.assertEqual(game.player_items_names('kirakis'), [])
        self.assertEqual(game.player_items_names('goshko1'), [])
        #test house + hotel
        self.assertEqual(game.house_count('kirakis'),0)
        self.assertEqual(game.hotel_count('kirakis'),0)
        #money
        self.assertEqual(game.add_money('kirakis',90),None)
        self.assertEqual(game.player_balance('kirakis'),1800)
        
        self.assertEqual(game.pay_money('kirakis',1801),None)
        self.assertEqual(game.player_balance('kirakis'),-1)

        game.player_pay_player('goshko1','kirakis',101)
        self.assertEqual(game.player_balance('kirakis'),100)
        self.assertEqual(game.player_balance('goshko1'),1389)
        
        self.assertEqual(game.can_pay('goshko1',1500),False)
        self.assertEqual(game._Game__nearest_pos_from_list(2,[0,5,12]),5)
        #ownership
        self.assertEqual(game.is_owned(0,'BANK'),True)
        self.assertEqual(game.building_owner(0),'BANK')
        # buy go possition fail
        self.assertEqual(game.buy_building('kirakis',0),False)
        self.assertEqual(game.player_items_names('kirakis'), [])
        # buy normal
        self.assertEqual(game.add_money('kirakis',9000),None)
        self.assertEqual(game.buy_building('kirakis',39),True)
        self.assertEqual(game.player_balance('kirakis'),8700)
        
        self.assertEqual(game.player_items_names('kirakis'), ['Boardwalk'])
        self.assertEqual(len(game.player_items('kirakis')), 1)
        self.assertEqual(game.player_balance('kirakis'),8700)

        self.assertEqual(game.buy_building('kirakis',1),True)
        self.assertEqual(game.player_items_names('kirakis'), ['Boardwalk', 'Mediterranean Ave.'])
        self.assertEqual(len(game.player_items('kirakis')), 2)
        self.assertEqual(game.player_balance('kirakis'),8640)
        
        #mourtage building

        
        game.mourtage('kirakis',39)
        self.assertEqual(game.player_balance('kirakis'),8840)
        game.mourtage('kirakis',3)
        self.assertEqual(game.player_balance('kirakis'),8840)
        game.unmourtage('kirakis',39)
        self.assertEqual(game.player_balance('kirakis'),8640)
        #build house + sell
        self.assertEqual(game.buy_building('kirakis',37),True)
        #self.assertEqual(game.player_items_names('kirakis'), ['Boardwalk'])
        self.assertEqual(game.has_line('Dark-Blue',game.player_items('kirakis')),True)
        self.assertEqual(game.has_line('Red',game.player_items('kirakis')),False)                    
        self.assertEqual(game.player_balance('kirakis'),8290)
        self.assertEqual(game.build_house('kirakis',39),True)
        self.assertEqual(game.build_house('kirakis',39),True)
        self.assertEqual(game.build_house('kirakis',39),True)
        self.assertEqual(game.build_house('kirakis',39),True)
        self.assertEqual(game.build_house('kirakis',39),True)
        self.assertEqual(game._deck.has_hotel(39),True)
        self.assertEqual(game._deck.house_count(39),0)
        self.assertEqual(game.check_acurate_trading_list(['Mediterranean Ave.']),True)
        self.assertEqual(game.player_balance('kirakis'),7290)
        self.assertEqual(game.check_acurate_trading_list(['Boardwalk']),False)
        self.assertEqual(game.sell_house('kirakis',39),True)
        self.assertEqual(game.sell_house('kirakis',39),True)
        self.assertEqual(game.sell_house('kirakis',39),True)
        self.assertEqual(game.sell_house('kirakis',39),True)
        self.assertEqual(game.sell_house('kirakis',39),True)
        self.assertEqual(game._deck.has_hotel(39),False)
        self.assertEqual(game._deck.house_count(39),0)
        self.assertEqual(game.check_acurate_trading_list(['Boardwalk']),True)
        self.assertEqual(game.player_balance('kirakis'),7790)
        self.assertEqual(game.player_items_names('kirakis'), ['Boardwalk', 'Mediterranean Ave.', 'Park Place'])
        self.assertEqual(game.player_items_names('goshko1'), [])
        self.assertEqual(game.check_acurate_trading_list(['Boardwalk','Mediterranean Ave.', 'Park Place']),True)
        game.remove_jail_card('kirakis')
        game.add_jail_card('kirakis')
        self.assertEqual(game.has_jail_card('kirakis'),True)
        self.assertEqual(game.has_jail_card('goshko1'),False)

        game.remove_jail_card('goshko1')
        #trade
        game.trade_cards('kirakis','goshko1')
        self.assertEqual(game.has_jail_card('kirakis'),False)
        self.assertEqual(game.has_jail_card('goshko1'),True)
        #nqma ogranichenie za prodajba na mqsto s kushta !
        game.trade_buildings('kirakis',['Boardwalk'],'goshko1',[])
        self.assertEqual(game.player_items_names('kirakis'), [ 'Mediterranean Ave.', 'Park Place'])
        self.assertEqual(game.player_items_names('goshko1'), ['Boardwalk'])
        self.assertEqual(len(game.player_items('goshko1')), 1)
        self.assertEqual(len(game.player_items('kirakis')), 2)
        game.trade_money('kirakis','goshko1',100,200)
        self.assertEqual(game.player_balance('kirakis'),7890)
        self.assertEqual(game.player_balance('goshko1'),1289)
        #bancrupt
        game.bancrupt('kirakis','goshko1')
        self.assertEqual(game.player_balance('kirakis'),9179)
        #ne trqbva da rabotqt!
        #self.assertEqual(game.player_balance('goshko1'),0)
        #game.trade_money('kirakis','goshko1',100,200)

        self.assertEqual(game.monent_status_balanced('kirakis'),True)
        self.assertEqual(game.monent_status_buildings('kirakis'),['Mediterranean Ave.', 'Park Place', 'Boardwalk'])
        self.assertEqual(game.can_build('Boardwalk','kirakis'),True)
        self.assertEqual(game.buy_building('kirakis',5),True)
        self.assertEqual(game.buy_building('kirakis',15),True)
        #auction
        self.assertEqual(game.get_auction_price(),0)
        self.assertEqual(game.get_auction_building(),'BANK')
        self.assertEqual(game.get_auction_players(),[])
        self.assertEqual(game.get_auction_winner(),'')
        game.init_auction('Boardwalk')
        
        
        
        
        
        
         

        
        

        

        
        

        
        

        
        










if __name__ == '__main__':
    unittest.main()
