import random

from  building import *
from global_variables import LIST_OF_BUILDINGS
BANK = 'BANK'
CONST_HOUSE = 5
class playing_deck:
    def __init__(self, deck ):
        self._deck = list(LIST_OF_BUILDINGS)
    
    def __getitem__(self,i):
        return self._deck[i]   

    #def get_building(self, building_position):
    #    return self._deck[building_position]

    def buy_building(building_index,player,auction):
        self._deck[building_index].buy_building(player,auction)
        player.add_item(self._deck[building_index])
    
    def trade_buildings(offerer,offerer_buildings_index,offerer_money,receiver, receiver_buildings_index, receiver_money):
        offerer_buildings = [self._deck[i] for i in offerer_buildings_index]
        receiver_buildings = [self._deck[i] for i in receiver_buildings_index]
        if not set(offerer_buildings).issubset(offerer.get_items()) or not  set(receiver_buildings).issubset(receiver.get_items()):
            return False # some of buildings are not owned  ...
        
        for building in  offerer_buildings:    
            receiver.get_items().append(building)
            self._deck[self._deck.index(building)].change_owner(receiver)    
            offerer.get_items().remove(building)

        for building in  receiver_buildings:  
            offerer.get_items().append(building ) 
            self._deck[self._deck.index(building)].change_owner(offerer) #tell building about new owner
            receiver.get_items().remove(building)   
        
        if offerer.budget() >= offerer_money and receiver.budget() >= receiver_money:
            offerer.add_money(receiver_money)
            offerer.pay_money(offerer_money)
            receiver.add_money(offerer_money)
            receiver.pay_money(receiver_money)
    
     
    def move_player_by_roll(self,player,steps): #nqma proverka za jal zashtoto se vika ot chest i chance
        positions = player.move_from_to(steps)[0]
        self._deck[positions[0]].remove(player)#ne go polzvam !
        self._deck[positions[1]].append(player)#ne go polzvam !
            return positions
    
    def move_player_to_position(self,player,position): #chance and chest
        positions = player.move_from_to(steps)[0]
        if positions == position: 
            return True:
        self._deck[positions].remove(player)#ne go polzvam !
        self._deck[position].append(player)

        if positions < position:
            self.move_player_by_roll(player,position - positions)            
            return position - positions # kolko stypki da mine gui
        elif positins > position:
            counter = 0
            while positons != position:
                positions = (positions + 1)%len(self._deck)
                count = count + 1
            self.move_player_by_roll(player,count)
            return count


        
    

    




#>>> a = [1,2,3,4,5,4]
#>>> b = [1,2,3,1,2]
#>>> set(b).issubset(a) true









    def set_player_on_pos(self,position,player_name):
        self._deck[position].add_player(player_name)
        
    def get_player(self,position):
        return self._deck[position].all_players() 

    def set_player_on_pos(self,position,player_name):
        self._deck[position].add_player(player_name)   
    
    def move_player(self,old_position, new_position,player_name):
        self._deck[old_position].delete_player(player_name)
        self._deck[new_position].add_player(player_name)

    def buy_place(self, position , player_name): # ako ima kushti ne moje da se prodade
        if self._deck[position].can_buy:
            self._deck[position].buy_building(player_name)
            return self._deck[position].get_price()
        else :
            self._deck[position].buy_building(player_name)

    def get_rent(self, position, player_name): 
        if self.get_owner(position) in [BANK, player_name]:
            return 0
        else:
            return self._deck[position].take_fee()

    def price_for_house(self, position):
        return self._deck[position].house_cost()
    
    def get_player(self,position):
        return self._deck[position].all_players()

    def house_count(self,position):
        return self._deck[position].count_houses()

    def has_hotel(self,position):
        return self._deck[position].has_hotel()
        
    def build_house(self,position,player_name):        
        if self._deck[position].can_build(player_name)  :
            if self._deck[position].build_house() :
                return self.price_for_house(position)
            else:
                return 0
            return 0

    def destroy_house(self,position,player_name ):
        if self._deck[position].destroy_house() :
            return self.price_for_house(position) * 0.5
        return 0

    def mourtage(self, position):
        if not self._deck[position].is_mourtage():
            self._deck[position].change_mourtage(True)
            return self._deck[position].mourtage_price()
        return 0  

    def unmourtage(self, position):
        if self._deck[position].is_mourtage():
            self._deck[position].change_mourtage(False)
            return self._deck[position].mourtage_price()
        return 0
    
    
    def is_owned(self, position,player_name):
        return self._deck[position].get_owner() == player_name
    
    def get_owner(self, position):
        return self._deck[position].get_owner()
    