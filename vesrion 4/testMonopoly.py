import unittest
import random
#from game import Game
from global_variables import CHANCE,COMMUNITY_CHEST,LIST_OF_BUILDINGS
from building import deck_building
from playing_deck import playing_deck
from game import Game
from player import Player

class TestMonopolyGameFunctions(unittest.TestCase):
    

        

    def testShuffleChance(self):
        mygame = Game()
        self.assertEqual(mygame._CHANCE, CHANCE)
 
        
    def testSuffleCommunityChest(self):
        mygame = Game()
        mygame.shuffler()
        
        self.assertNotEqual(mygame._COMMUNITY_CHEST, COMMUNITY_CHEST)
        self.assertNotEqual(mygame._CHANCE, CHANCE)
        
#____________---rerigster player --- _____________start

        
    def testINVALIDRegisterPlayer(self):
        mygame = Game()
        mygame.register_player('az')
        self.assertNotEqual(mygame.PLAYER_NAMEORDER,'[\'az\']')
        self.assertEqual(mygame.player_list,[])

    def testVALIDRegisterPlayer(self):
        mygame = Game()
        mygame.register_player('kirov124')
        self.assertEqual(mygame.PLAYER_NAMEORDER,['kirov124'])
        self.assertEqual(mygame.player_list[0].player_name,'kirov124')

    def testVALIDRegisterPlayer(self):
        mygame = Game()
        mygame.register_player('kirov124')
        mygame.register_player('kir24')
        mygame.register_player('peshko134')
        self.assertEqual(mygame.PLAYER_NAMEORDER,['kirov124','peshko134'])
        self.assertEqual(mygame.player_list[0].player_name,'kirov124')
        self.assertEqual(mygame.player_list[1].player_name,'peshko134')
#_______ ---registration of player--- _____________end

#_____________________roll   dice
    def testRoll_Dice(self):
        mygame = Game()
        self.assertIn(mygame.roll_dice(),range(2,13))
        self.assertIn(mygame.roll_dice(),range(2,13))
        self.assertIn(mygame.roll_dice(),range(2,13))
        self.assertIn(mygame.roll_dice(),range(2,13))
        

        
#__________________ ---single building---   =start= _____________
    def testBuildingAtributes(self):
        building = deck_building('test building','green',230,40,400,10,20,30,40,50,['gosho'],True)
        self.assertEqual(building.get_price(),230)
        self.assertEqual(building.mourtage_price(),115)
        self.assertEqual(building.all_players(),['gosho'])
        building.add_player('kikosan')
        building.delete_player('goshkosan')
        building.delete_player('gosho')
        self.assertEqual(building.all_players(),['kikosan'])
        self.assertEqual(building.get_owner(),'BANK')
        building.buy_building('mark')
        self.assertNotEqual(building.get_owner(),'BANK')
        self.assertEqual(building.get_owner(),'mark')
        self.assertEqual(building.is_mourtage(),True)
        

    #def testBuildingOwners(self):        
        building = deck_building('test building','green',230,40,400,10,20,30,40,50,['gosho'],True)
        building.buy_building('mark')
        self.assertEqual(building.can_build('az'),False)
        self.assertEqual(building.can_build('mark'),False)
        building.change_mourtage(False)
        self.assertEqual(building.can_build('mark'),True)
        building.change_mourtage(True)
        self.assertEqual(building.can_build('mark'),False)
        self.assertEqual(building.has_hotel(),False)
        self.assertEqual(building.count_houses(),0)
        self.assertEqual(building.get_name(),'test building')
        self.assertEqual(building.get_owner(),'mark')
        self.assertNotEqual(building.get_owner(),'BANK')
        self.assertEqual(building.take_fee(),0)
        building.change_mourtage(False)
        self.assertEqual(building.take_fee(),400)
        self.assertEqual(building.can_buy(),False)
        building.buy_building('kirakis')
        self.assertEqual(building.get_owner(),'kirakis')
        self.assertEqual(building.can_build('kirakis'),True)

    #def testBuildingRentsa(self):#da pitam za imeto
        building2 = deck_building('test building','green',230,40,400,10,20,30,40,50,['gosho'],False)
        building = deck_building('test building','green',230,40,400,10,20,30,40,50,['gosho'],False)
        buildingTEST = deck_building('test building','green')
        buildingTEST1 = deck_building('test building','green')
        
        
        self.assertEqual(buildingTEST1.house_cost(),0)
        buildingTEST1.perhouse_price = 444
        
        self.assertEqual(buildingTEST1.house_cost(),444)
        self.assertNotEqual(buildingTEST.house_cost(),444)#!!!!!!!!!!!!
        building2.perhouse_price = 444 #!!!!!!!!!!!!!!
        self.assertNotEqual(building2.house_cost(),40)
        self.assertEqual(building2.house_cost(),444)
        self.assertEqual(building.house_cost(),40)
        self.assertEqual(building2.take_fee(),0)
        building.buy_building('mark')
        self.assertEqual(building.take_fee(),400)
        building.build_house()
        self.assertEqual(building.take_fee(),10)
        building.build_house()
        self.assertEqual(building.take_fee(),20)
        self.assertEqual(building.is_mourtage(), False)
        self.assertEqual(building.count_houses(),2)
        self.assertEqual(building.has_hotel(),False)
        self.assertEqual(building.get_name(),'test building')
        self.assertEqual(building.is_mourtage(),False)
        self.assertNotEqual(str(building),'')
        self.assertNotEqual(building.show_building_info(),'')
        self.assertEqual(building.build_house(),True)
        self.assertEqual(building.take_fee(),30)
        building.build_house()
        self.assertEqual(building.get_price(),230)        
        self.assertEqual(building.count_houses(),4)
        self.assertEqual(building.take_fee(),40)
        building.build_house()
        self.assertEqual(building.take_fee(),50)
        self.assertEqual(building.build_house(),False)
        self.assertEqual(building.count_houses(),0)
        self.assertEqual(building.has_hotel(),True)
        building.destroy_house()
        building.destroy_house()
        self.assertEqual(building.count_houses(),3)
        self.assertEqual(building.has_hotel(),False)
        building.build_house()
        building.build_house()
        self.assertEqual(building.has_hotel(),True)
        
    #def testBuildingRemovePlayers(self):
        building = deck_building('test building','green',230,40,400,10,20,30,40,50,['gosho'],False)
        self.assertEqual(building.all_players(),['gosho'])
        building.add_player('kirakis')
        self.assertEqual(building.all_players(),['gosho','kirakis'])
        building.add_player('kirakis1')
        building.delete_player('kirakis')
        self.assertEqual(building.all_players(),['gosho','kirakis1'])
        building.delete_player('kirakis1')
        self.assertEqual(building.all_players(),['gosho'])
        building1 = deck_building('test building','green',230,40,400,10,20,30,40,50,[],False)
        building2 = deck_building('test building','green',230,40,400,10,20,30,40,50,[],False)
        building1.add_player('kirakis')
        self.assertEqual(building2.all_players(),[])
        self.assertEqual(building1.all_players(),['kirakis'])
        building1.add_player('kirakis23')
        #self.assertEqual(building2.all_players(),['kirakis'])
        ll = [deck_building('test building1','green',230,40,400,10,20,30,40,50,[],False),
              deck_building('test building2','green',230,40,400,10,20,30,40,50,[],False)]
        ll[1].add_player('kirakis23')
        self.assertEqual(ll[0].all_players(),[])
        self.assertEqual(ll[1].all_players(),['kirakis23'])
    
        

#________________________---single building test ---end ____________________
        

#___________ ---playing deck test ==start== _________________        
        

    def testPlayingDeckMOVE(self):
        deck = playing_deck(LIST_OF_BUILDINGS)
        self.assertEqual(deck._deck,LIST_OF_BUILDINGS)
        self.assertEqual(deck.get_player(2),[])
        self.assertEqual(deck.get_player(0),[])
        deck.move_player(0,2,'kirakis')
        self.assertEqual(deck.get_player(0),[])
        self.assertEqual(deck.get_player(2),['kirakis'])
        deck.move_player(2,3,'kirakis')
        self.assertEqual(deck.get_player(2),[])
        self.assertEqual(deck.get_player(3),['kirakis'])

    def testPlayingDeckBuyOptions(self):
        deck = playing_deck(LIST_OF_BUILDINGS)
        self.assertEqual(deck.is_owned(3,'BANK'),True)
        deck.buy_place(3,'goshko')
        self.assertEqual(deck.is_owned(3,'BANK'),False)
        self.assertEqual(deck.get_owner(3),'goshko')
        self.assertEqual(deck.is_owned(3,'goshko'),True)
        self.assertEqual(deck.is_owned(4,'BANK'),True)
        self.assertEqual(deck.get_rent(3,'goshko1'),4)
        self.assertEqual(deck.get_rent(3,'goshko'),0)
#da pitam zashto ne rabotqt !!!! 
    def testPlayingDeckBuild(self):
        deck = playing_deck(LIST_OF_BUILDINGS)
        self.assertEqual(deck.get_owner(3),'BANK')
        self.assertEqual(deck.is_owned(3,'BANK'),True)
        
        self.assertEqual(deck.price_for_house(3),50)
        deck.buy_place(3,'goshko')
        self.assertEqual(deck.build_house(3,'goshko'),50)
        self.assertEqual(deck.is_owned(3,'goshko'),True)
        self.assertEqual(deck.house_count(3),1)
        self.assertEqual(deck.build_house(3,'goshko'),50)
        self.assertEqual(deck.house_count(3),2)
        self.assertEqual(deck.build_house(3,'goshko'),50)
        self.assertEqual(deck.house_count(3),3)
        self.assertEqual(deck.build_house(3,'goshko'),50)
        self.assertEqual(deck.house_count(3),4)
        self.assertEqual(deck.build_house(3,'goshko'),50)
        self.assertEqual(deck.house_count(3),0)
        self.assertEqual(deck.has_hotel(3),1)
        self.assertEqual(deck.destroy_house(3,'goshko'),25)
        self.assertEqual(deck.house_count(3),4)
        self.assertEqual(deck.has_hotel(3),0)
        self.assertEqual(deck.destroy_house(3,'goshko'),25)
        self.assertEqual(deck.destroy_house(3,'goshko'),25)
        self.assertEqual(deck.destroy_house(3,'goshko'),25)
        self.assertEqual(deck.house_count(3),1)
        self.assertEqual(deck.destroy_house(3,'goshko'),25)
        self.assertEqual(deck.destroy_house(3,'goshko'),0)
        self.assertEqual(deck.house_count(3),0)

    def testPlayingDeckBuildMourtageProbs(self):
        deck = playing_deck(LIST_OF_BUILDINGS)
        self.assertEqual(deck.get_owner(3),'BANK')
        deck.buy_place(3,'goshko')
        #self.assertEqual(deck.is_owned(4,'goshko'),False)
        self.assertEqual(deck.destroy_house(3,'goshko'),0)
        self.assertEqual(deck.get_owner(3),'goshko')
        self.assertEqual(deck.mourtage(3),30)
        self.assertEqual(deck.mourtage(3),0)
        
        self.assertEqual(deck.unmourtage(3),30)
        self.assertEqual(deck.unmourtage(3),0)

        self.assertEqual(deck.get_player(3),[])
        deck.move_player(2,3,'kirakis')
        self.assertEqual(deck.get_player(3),['kirakis'])
        deck.set_player_on_pos(13,'kirakis')
        self.assertEqual(deck.get_player(13),['kirakis'])
        
        



        
    def testPlayers(self):
        player = Player('goshko')
        player1 = Player('goshko')
        player2 = Player('kiki')
        self.assertIsNot(player1,player)
        self.assertIsNot(player1.list_of_items,player.list_of_items)
        self.assertEqual(player.get_items(),[])
        self.assertEqual(player1.get_items(),[])
        self.assertEqual(player2.get_items(),[])
        
        self.assertEqual(player.print_player_all(),None)
        self.assertEqual(str(player),'goshko')
        self.assertEqual(player.playername(),'goshko')
        self.assertEqual(player.name(),'goshko')

        self.assertEqual(player.can_pay(1501),False)
        self.assertEqual(player.can_pay(1500),True)
        self.assertEqual(player.can_pay(-15000),True)

        self.assertEqual(player.get_position(),0)
        player.new_position(5)
        self.assertEqual(player1.get_position(),0)
        self.assertEqual(player.get_position(),5)
        player.add_item('mall')
        self.assertEqual(player.get_items(),['mall'])
        self.assertEqual(player1.get_items(),[])
        
        self.assertEqual(player1.is_playing(),True)
        
        self.assertEqual(player.has_item('mall'),True)
        self.assertEqual(player1.has_item('mall'),False)
        self.assertEqual(player.remove_item('mall'),1)
        self.assertEqual(player.remove_item('mall'),0)
        self.assertEqual(player.get_items(),[])
        player.new_status(True)
        self.assertEqual(player.is_playing(),False)
        self.assertEqual(player1.is_playing(),True)


    
        
        
        

        
        
        
        


                         

          
if __name__ == '__main__':
    unittest.main()
