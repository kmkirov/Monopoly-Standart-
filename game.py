import random
import re

from global_variables import CHANCE, COMMUNITY_CHEST, LIST_OF_BUILDINGS



class Game:
    
    
    def __init__(self):
        self._bancrupt_players = []
        self.player_list = []
        self.PLAYER_NAMEORDER = []
        self.BUILDING_NAMEORDER = [building.get_building_name() for building in list_of_buildings]
        #self.playerNAMES 
        
        self._COMMUNITY_CHEST = COMMUNITY_CHEST #globalno
        self._comunity_chest_index = 0
         

        self._CHANCE = CHANCE
        self._chance_index = 0
         
        
    def shuffler(self):
        for i in range(random.randint(2,10)):
            random.shuffle(self._COMMUNITY_CHEST)
        for i in range(random.randint(2,10)):
            random.shuffle(self._CHANCE)

    def register_player(self):
        """ add new players at the beginning of the game (work with typing Yes,No to continue)"""
        register='Yes'
        while register == 'Yes':
            register='No'
            print('Enter Player name: ')
            name=input()
            if self._valid_name(name):
            #if not macht \w* again
                player = Player(name)
                player_list.append(player)
                print('Success ', player,'added')
            else:
                print( player,'can\'t be added')
            print('do you want to add player?\n (Yes, No)')
            register = input() #true false


    def _valid_name(self,name):
       
        
        name_regex = r'(?P<username>^[a-zA-Z]\w{5,10}$)'
        if bool(re.match(name_regex, name)):
            names = [ i.player_name for i in self.player_list ]
            if name not in names :
                return True
        return False   

    def roll_dice(self): #pochti bezpolezna
        
        a = random.randrange(1,7)
        
        b = random.randrange(1,7)
        
        #logging
        return a + b

    def auction(self, building_name):
        #players_acuction=[ player for player in player_list if player.is_playing()]
        # samo za igraeshtite
        auction_players = [
            player for player in player_list if player.is_playing()]
        auction_price = 1
        player_index = 0
        while len(auction_players) > 1:
            on_turn_player = auction_players[player_index %
                                             len(auction_players)]
            print(on_turn_player.name(), ' the auction price for', building_name,
                  ' is ', auction_price, 'bid or fold')
            answer = input('fold, bid or auction_price + your number ')

            if answer == 'fold':
                print(player_index %
                      len(auction_players), 'folded the auction')
                auction_players.pop(player_index % len(auction_players))
            elif answer == 'bid':
                auction_price = auction_price + 1
                player_index = player_index + 1
            else:
                answer = int(answer)
                if on_turn_player.can_pay(answer + auction_price):
                    auction_price = auction_price + answer
                    print(on_turn_player, 'bided to ', auction_price)
                    player_index = player_index + 1
                else:
                    print(on_turn_player, 'you can\'t afford :', answer + auction_price, 'mourtage,sell,\
                     trade or fold ..(m,s,t,f) ' )
                    ask = input()
                    if ask == 'm':
                        print('mourtage player')
                    elif ask == 's':
                        print('selling')
                    elif ask == 't':
                        print('trade')
                    elif ask == 'f':
                        print(player_index %
                              len(auction_players), 'folded the auction')
                        auction_players.pop(player_index %
                                            len(auction_players))

        print('The winner is ', auction_players[0], 'bought ',
              building_name, 'for', auction_price)
        pl_index = player_list.index(auction_players[0])
        player_list[pl_index].budget =  player_list[pl_index].budget - \
            auction_price
        player_list[pl_index].self.list_of_items.append(building_name)
##slagam imeto na sgradata :)

#we know that the player has money!
    def buy_house(self, player,building_name, building_price):
        pl_index =player_list.index(player)
        player_list[pl_index].budget = player_list[pl_index].budget - building_price
        player_list[pl_index].self.list_of_items.append(building_name)##slagam imeto na sgradata :)
    

    
    def can_build(self, players_items_, wanted_to_build):

        color_buildig = [ group for group in groups if wanted_to_build in group ]    
        for part in color_buildig:
            if part not in players_items_:
              return False
        return True

    


    def check_position(self, index, player_name):
        if list_of buildings[index].owner = player_name:
            return 'O'
        elif list_of buildings[index].color_street == 'FREE':
            return 'F'
        elif list_of buildings[index].color_street == 'TAX':
            return 'T'
        elif list_of buildings[index].color_street == 'utility':
            return 'U'
        elif list_of buildings[index].color_street == 'STATION':
            return 'S'
        elif list_of buildings[index].color_street == 'CC':
            return 'CC'
        elif list_of buildings[index].color_street == 'C':
            return 'C'
        elif list_of buildings[index].color_street == 'JAIL':
            return 'J'
        else:
            return 'B'

    def player_action_after_step(self, command, player_index, building_index):
        building_name = list_of buildings[building_index].get_building_name()
        if command == 'F' or command == 'O':
            return
        elif command == 'T':
            player_list[player_index].add_money(-list_of buildings[building_index].buildig_fee_globa)
        elif command == 'U':
            a = random.randrange(1,7)
            b = random.randrange(1,7)
            if  index_of_owner('Electronic Company') == index_of_owner('Water Work'):
                player_list[player_index].add_money(-((a+b)*10))
            else :
                player_list[player_index].add_money(-((a+b)*4))
        elif command == 'S':
            STATION_FEE =[25,50,100,200]
            happy_player_index = index_of_owner(self,building_name)
            owned_types = player_type_of_buildings( happy_player_index)
            player_list[happy_player_index].add_money(STATION_FEE[owned_types.count('STATION')-1])
            player_list[player_index].add_money(-STATION_FEE[owned_types.count('STATION')-1])

        elif command == 'CC':
            Community(self, player_index, self.comunity_chest_index)
        elif command == 'C':
            Chance(self, player_index, self.chance_index)

        elif command == 'J':
            move_pos_pos(building_index, 10 ,player_list[player_index].name())
        else: 
            if   list_of buildings[building_index].can_buy():
                print ('auction or buy')
                answer = input()
            else:
                player_list[player_index].add_money(-list_of buildings[building_index].take_fee())
                happy_player_index = index_of_owner(self,building_name)
                owned_types = player_type_of_buildings( happy_player_index)
                player_list[happy_player_index].add_money(list_of buildings[building_index].take_fee())






    def can_buy(self, buildin_index):


    def player_type_of_buildings(self, player_index):
        owned_buildings = player_list[player_index].get_items()
        owned_types = []
        for item in owned_buildings:
            index = BUILDING_NAMEORDER.index(item)
            owned_types.append(list_of_buildings[index].color_street)
        return owned_types

#DICT_OF_COLORS = {'Purple':2, 'Light-Green':3, 'Violet':3, 'Orange':3, 'Red':3 , 'Yellow':3, 'Dark-Green':3, 'Dark-Blue':2}
    def can_build_house(self, selected_house_name):
        index = BUILDING_NAMEORDER.index(selected_house_name)
        selected_color = list_of_buildings[index].color_street
        owner = index_of_owner(selected_house_name):
        owner_buildings = player_type_of_buildings( owner)
        if selected_color in ['Dark-Blue','Purple']:
            return owner_buildings.count(selected_color) == 2
        else:
            return owner_buildings.count(selected_color) == 3


    def index_of_owner(self,building_name):
        building_index = BUILDING_NAMEORDER.index(building_name)
        return PLAYER_NAMEORDER.index(list_of_buildings[building_index].owner)


    def main_loop(self):
        import random
        pindex = 0
        while len(player_list)>1:
            a = random.randrange(1,7)
            b = random.randrange(1,7)
            new_pos = move_player_from_to(player_list[pindex].get_position(),a+b ,player_list[pindex].name())
            player_list[pindex].new_position(new_pos)
            if list_of_buildings[new_pos].owner != player_list[pindex].name():
                command = check_position(new_pos)
                player_action_after_step( command, pindex, new_pos)
            #veche e premesten i polugloben
                while True:
                print('do you want to mourtage,unmourtage,sell,build?  or No')
                answer = input()
                if answer == No:
                    break
    def bancrupt(self, winer,loser):
        w = player_list[ player_list.index(winner)]
        l = player_list[ player_list.index(winner)]
        a = deck_buldings_ordered
        for building in l.list_of_items:
            if a[a.index(building)].house_count>0:
                destroy_house(self,a.index(building),l.name,a[a.index(building)].house_count )
        w.budget = w.buget + l.budget
        w.list_of_items.append(l.list_of_items)
# ne znam zashto e tuk tova
    def add_money(self,player_name,money):
        players_ = [player.name() for player in player_list]
        index_player = players_.index(player_name)
        player_list.budget = player_list.budget + money

lucky_regex = {'Get_money':r'collect',
               'Pay_money':r'Collect',
               'Jail_free':r'Get out of jail free',
               'Jail_in ':r'Go to jail',
               'Pay': r'Pay',
               'Hotel_pay':r'hotel', 
               'Go_option':'Advance',
               'Each':r'each',
               'utility' : r'utility',
               'pay_each' :r'pay each player',
               'Spaces' : r'back 3 spaces'
              }


        def trade(self,buyer,seller,money_for_b, money_for_s,b_buildig,s_buliding):
        buy_person =  player_list[ player_list.index(buyer)]
        sell_person =  player_list[ player_list.index(seller)]
        
        buy_person.budget = buy_person.budget + money_for_b
        sell_person.budget = sell_person.budget + money_for_s
        
        buy_person.list_of_items.append(b_buildig) 
        sell_person.remove(s_buliding)
        player_list[ player_list.index(buyer)] = buy_person
        player_list[ player_list.index(seller)] = sell_person 