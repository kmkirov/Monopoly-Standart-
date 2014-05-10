import unittest
import random
from game import Game
from global_variables import CHANCE,COMMUNITY_CHEST
from building import deck_building

class TestMonopolyGameFunctions(unittest.TestCase):
    

        

    def testShuffleChance(self):
        mygame = Game()
        self.assertEqual(mygame._CHANCE, CHANCE)
 
        
    def PROMBLEMtestSuffleCommunityChest(self):
        mygame = Game()
        mygame.shuffler()
        
        self.assertEqual(mygame._COMMUNITY_CHEST, COMMUNITY_CHEST)
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
        

        
#__________________ single building _____________
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
        

    def testBuildingOwners(self):        
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

    def testBuildingRents(self):
        building = deck_building('test building','green',230,40,400,10,20,30,40,50,['gosho'],False)
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

#________________________---single building test --- ____________________
        
        
        
        
        
        
        
        
        


                          

          
if __name__ == '__main__':
    unittest.main()
