import random

from  building import deck_building
from global_variables import LIST_OF_BUILDINGS
BANK = 'BANK'
CONST_HOUSE = 5
class playing_deck:
    def __init__(self, deck ):
        self._deck = list(LIST_OF_BUILDINGS)
    
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
    

    

