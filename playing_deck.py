import random
class playing_deck:



    def __init__(self):
        pass
    




    def add_money(self,player_name,money):
        players_ = [player.name() for player in player_list]
        index_player = players_.index(player_name)
        player_list.budget = player_list.budget + money

    def move_pos_pos(old_position, new_position,player_name):
        deck_buldings_ordered[old_position].players_on_building.remove(player_name)
        deck_buldings_ordered[new_position].players_on_building.append(player_name)




    #remove from old pos and move to the new possition + return the index
    def move_player_from_to(self,from_pos,step,player_name):
        old_position = deck_buldings_ordered[from]
        old_position.players_on_building.remove(player_name)  #list.remove
        new_index = ( from_pos + step ) % len(deck_buldings_ordered)#da ne prevyrta
        new_position=deck_buldings_ordered[new_index]
        new.position.players_on_building.append(player_name)
        return new_index


    def rent(self, player_name, place_index): #samo ako moje da se vzeme
        position=deck_buldings_ordered[place_index]

        a = player_list[ player_list.index(player_name)].budget 
        if position.buildig_name not in a.list_of_items[]:
            player_list[ player_list.index(player_name)].budget = a - position.teke_fee()



    def build_house(self,index,player_name, house_count=1 ):
        a=deck_buldings_ordered[index].house_count
        #if a == 5: raise 
        deck_buldings_ordered[index].house_count=a + house_count
        player_list[ player_list.index(player_name)].budget = player_list[ player_list.index(player_name)].budget -
                house_count * deck_buldings_ordered[index].perhouse_price

    

     def destroy_house(self,index,player_name, house_count=1 ):
        a=deck_buldings_ordered[index].house_count
        deck_buldings_ordered[index].house_count=a - house_count
        player_list[ player_list.index(player_name)].budget = player_list[ player_list.index(player_name)].budget +
                0.5 * house_count * deck_buldings_ordered[index].perhouse_price


    def trade(self,buyer,seller,money_for_b, money_for_s,b_buildig,s_buliding):
        buy_person =  player_list[ player_list.index(buyer)]
        sell_person =  player_list[ player_list.index(seller)]
        
        buy_person.budget = buy_person.budget + money_for_b
        sell_person.budget = sell_person.budget + money_for_s
        
        buy_person.list_of_items.append(b_buildig) 
        sell_person.remove(s_buliding)
        player_list[ player_list.index(buyer)] = buy_person
        player_list[ player_list.index(seller)] = sell_person 

    def mourtage(self, building, player):
        a = deck_buldings_ordered
        a[a.index(building)].is_mourtaged = True
        money_get = a[a.index(building)].mourtage_price()
        player_list[ player_list.index(player)].budget =  player_list[ player_list.index(player)].budget+money_get
        deck_buldings_ordered = a
        return money_get


    def unmourtage(self, building, player):
        a = deck_buldings_ordered
        a[a.index(building)].is_mourtaged = False
        money_get = a[a.index(building)].mourtage_price()
        player_list[ player_list.index(player)].budget =  player_list[ player_list.index(player)].budget-money_get
        deck_buldings_ordered = a
        return money_get
    

    

    


    """ 
    def roll_dice(self, player_name):
        return result from 2 rolled dices and print smth




        """