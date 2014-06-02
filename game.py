import random
import re

from playing_deck import playing_deck
from global_variables import  *
from player import Player


GO = 0
Jail = 10
class Game:
    
    
    def __init__(self):
        self.current_player_index = 0
        self._deck = playing_deck(list(LIST_OF_BUILDINGS)) #igralnoto pole
        self._bancrupt_players = list()
        self.player_list = list()
        self.PLAYER_NAMEORDER = list()
        self._COMMUNITY_CHEST = COMMUNITY_CHEST #globalno
        self._comunity_chest_index = 0
        self._CHANCE = CHANCE
        self._chance_index = 0
        self._turn_index=0
        self._auction_index=0
        self._auction_building=str('BANK')
        self._auction_price = 0
        self._auction_players_names=list()
        self._auction_winner=str('')

    #def current_player_index(self):
        #return self._turn_index
    def has_house_on_building(self, building_index,player_name):       
        if player_name == self._deck[building_index].get_owner():
            if self._deck[building_index].has_hotel() or self._deck[building_index].count_houses:
                return False
        return True
    
    def get_all_players(self):
        return self.PLAYER_NAMEORDER
    
    def get_playername_by_index(self, index):
        return self.PLAYER_NAMEORDER[index]
    
    def get_current_playing_index(self): #index of current player
        return self.current_player_index
    
    def next_player_turn(self): 
        self.current_player_index = self.current_player_index + 1
        
    def shuffler(self):
        for i in range(random.randint(5,10)):
            random.shuffle(self._CHANCE)
        for i in range(random.randint(5,10)):
            random.shuffle(self._COMMUNITY_CHEST)


    def register_player(self,name):
        if self._valid_name(name):            
            player = Player(name)
            self.player_list.append(player)
            self.PLAYER_NAMEORDER.append(name)
            return True
        else:
            return False
            
        
                
    def _valid_name(self,name):
        name_regex = r'(?P<username>^[a-zA-Z]\w{5,10}$)'
        if bool(re.match(name_regex, name)):
            names = [ i.playername() for i in self.player_list ]
            if name not in names :
                return True
        return False
    
    def roll_dice(self): #checked in game_test_only
        a = random.randrange(1,7)
        b = random.randrange(1,7)
        #logging
        return [a + b, a==b] #!!!!!
    
        
    def new_position(self, player_name, position):  #checked in game_test_only
        return self.player_list[self.player_index(player_name)].new_position(position)

    def move_player_by_rolled(self,rolled,player_name):  #checked in game_test_only
        old_position = self.player_position(player_name)
        self.new_position(player_name, rolled + old_position)    
    
    def player_position(self, player_name):  #checked in game_test_only
        return self.player_list[self.player_index(player_name)].get_position()
        
        
    def on_starting(self):#da ne se polzva
        random.shuffle(self.PLAYER_NAMEORDER)
        for index in range(len(self.player_list) + 1):
            self.PLAYER_NAMEORDER.append(self.player_list[index].name())
        
                                                
    def player_index(self,player_name):  #checked in game_test_only
        return self.PLAYER_NAMEORDER.index(player_name)

    def player_items_names(self,player_name):  #checked in game_test_only
        index = self.player_index(player_name)
        return self.player_list[index].get_items_names()

    def player_items(self,player_name):  #checked in game_test_only
        index = self.player_index(player_name)
        return self.player_list[index].get_items()
        
    def player_balance(self,player_name):  #checked in game_test_only
        return self.player_list[self.player_index(player_name)].get_money()
   
    def house_count(self,player_name): #checked in game_test_only
        index = self.player_index(player_name)
        counter = 0
        for building in self.player_list[index].get_items():
            counter = counter + building.count_houses()
        return counter

    def hotel_count(self,player_name): #checked in game_test_only
        index = self.player_index(player_name)
        counter = 0
        for building in self.player_list[index].get_items():
            if building.has_hotel():
                counter = counter + 1
        return counter
            
    def add_money(self,player_name, money): #checked in game_test_only
        self.player_list[self.player_index(player_name)].add_money(money)
        
    def pay_money(self,player_name,money): #checked in game_test_only
        self.player_list[self.player_index(player_name)].pay_money(money)
        
    def player_pay_player(self, payer, receiver, money): #checked in game_test_only
        self.pay_money(payer,money)
        self.add_money(receiver,money)
        
        
    def can_pay(self,player_name,money): #checked in game_test_only
        #return True or False
        return self.player_list[self.player_index(player_name)].can_pay(money)
 
    def __nearest_pos_from_list( self, player_pos ,listed_places): #checked in game_test_only
        for i in listed_places:
            if i > player_pos :
                return i
        return listed_places[0]
                
    
    
    def is_owned(self, building_index, player_name): #checked in game_test_only
        if player_name == self._deck[building_index].get_owner():
            return True
        return False

    def building_owner(self, building_index): #checked in game_test_only
        return self._deck[building_index].get_owner()
            
    
    def buy_building(self,player_name,building_index):#checked in game_test_only
        house_name = BUILDING_NAMEORDER[building_index]
        if self.can_pay(player_name,self._deck[building_index].get_price() and self.is_owned(building_index,'BANK')) and building_index not in FORBIDDEN:
            self._deck[building_index].buy_building(player_name)
            self._add_building_to_player(player_name,house_name)
            #self.player_list[self.player_index(player_name)].add_item(self._deck[building_index])
            #self.player_list[self.player_index(player_name)].add_0_remove1_item_name(house_name,0)
            self.player_list[self.player_index(player_name)].pay_money(self._deck[building_index].get_price())
            return True            
        else:
            return False
                        
         
    #def sell_building(self,seller,buyer,house_name): not implemented
        
    def can_mourtage_0_unmourtage_1(self,player_name,building_index,flag): #checked in game_test_only
        if self.is_owned(building_index,player_name):
            if  flag == 0 and  not  self._deck[building_index].is_mourtage() \
               and self._deck.house_count(building_index) == 0 and self._deck.has_hotel(building_index) == 0:
                return True
            elif flag == 1 and self._deck[building_index].is_mourtage():
                return True
        else:
            return False
        
    def mourtage(self,player_name,building_index): #checked in game_test_only
        building_name = BUILDING_NAMEORDER[building_index]
        if self.can_mourtage_0_unmourtage_1(player_name,building_index,0):
            self._deck[building_index].change_mourtage(True)
            self.add_money(player_name,self._deck[building_index].mourtage_price())
            return True
        else :
            return False

        
    def unmourtage(self, player_name, building_index): #checked in game_test_only
        building_name = BUILDING_NAMEORDER[building_index]
        if self.can_mourtage_0_unmourtage_1(player_name,building_index,1):
            self._deck[building_index].change_mourtage(False)
            self.pay_money(player_name,self._deck[building_index].mourtage_price())
            return True
        else:
            return False




    def has_line(self, building_color, player_buildings): #checked in game_test_only
        indexes = [building.get_color() for building in player_buildings ]
        #colors = [self._deck[index].get_color()for index in indexes]
        counter = indexes.count(building_color)
        if counter == DICT_OF_COLORS[ building_color]:
            return True
        return False

        
    def build_house(self,player_name, building_index): #checked in game_test_only
        building_name = BUILDING_NAMEORDER[building_index]
        color = self._deck[building_index].get_color()
        buildings = self.player_items(player_name)
        # da proverq dali e mortaged
        if self.is_owned( building_index, player_name) and self.has_line(color, buildings):
            if self._deck[building_index].build_house() and self.can_pay(player_name,self._deck[building_index].house_cost()):
                self.pay_money(player_name,self._deck[building_index].house_cost())
                return True
        return False
                        
    def sell_house(self,player_name,building_index): #checked in game_test_only
        building_name = BUILDING_NAMEORDER[building_index]
        if self.is_owned( building_index, player_name) :
            if self._deck[building_index].destroy_house():
                self.add_money(player_name,self._deck[building_index].house_cost()/2)
                return True
        return False

    #podavat se list ot 1 argumenti i list ot drugi i 2 playera i se razmenqt :)  bez jail card

    def remove_jail_card(self, player_name): #checked in game_test_only
        return self.player_list[self.player_index(player_name)].remove_jail_card()

    def add_jail_card(self, player_name): #checked in game_test_only
        return self.player_list[self.player_index(player_name)].add_jail_card()

    def has_jail_card(self,player_name): #checked in game_test_only
        return self.player_list[self.player_index(player_name)].has_jail_card()
     

    
    def _remove_building_from_player(self,player_name,building_name):
        player_index = self.player_index(player_name)
        return self.player_list[player_index].remove_item(building_name) #true False
        

    def _add_building_to_player(self,player_name,building_name): #checked in game_test_only
        building_index = BUILDING_NAMEORDER.index(building_name)
        player_index = self.player_index(player_name)
        self.player_list[player_index].add_item(building_name,self._deck[building_index])
        
    def trade_buildings(self,ofer_maker,ofer_maker_items_index, buyer,buyer_items_index ):#prima list ot chisla 
        ofered_items_names = [BUILDING_NAMEORDER[i]  for i in ofer_maker_items_index]
        buyer_items_names = [BUILDING_NAMEORDER[i]  for i in buyer_items_index ]
        #ne sym proveril za tova dali ima kushti vurhu sgradite.. tova se proverqva v igrata
        for building in  buyer_items_index:
            if self.has_house_on_building(building,buyer):
               return False
        for building in  ofer_maker_items_index:
            if self.has_house_on_building(building,ofer_maker):
               return False
        for i in ofer_maker_items_index:
            self._deck[i].buy_building(buyer)
        for i in buyer_items_index:
            self._deck[i].buy_building(ofer_maker)
        for i in ofered_items_names:
            self._add_building_to_player(buyer,i)
            self._remove_building_from_player(ofer_maker,i)
        for i in buyer_items_names:
            self._add_building_to_player(ofer_maker,i)
            self._remove_building_from_player(buyer,i)
        return True
            
            #index ++ !!!!!




    def check_acurate_trading_list(self,buildings_name):#checked in game_test_only
        if len(buildings_name)>1:
            for building_name in buildings_name:
                index = BUILDING_NAMEORDER.index(building_name)
                if self._deck.has_hotel(index) or self._deck.house_count(index) > 0:
                    return False
        else:
            index = BUILDING_NAMEORDER.index(buildings_name[0])
            if self._deck.has_hotel(index) or self._deck.house_count(index) > 0:
                    return False
        return True
        
    def trade_cards(self,offer_maker, receiver): #checked in game_test_only
        if self.has_jail_card(offer_maker):
             self.remove_jail_card(offer_maker)
             self.add_jail_card(receiver)
             return True
        return False
                
                        
#narochno ne proverqvam dali moje da plati koito i da e
    def trade_money(self, ofer_maker, receiver, ofer_maker_give_money, receiver_give_money):#checked in game_test_only
        self.player_pay_player( ofer_maker, receiver, ofer_maker_give_money)
        self.player_pay_player( receiver, ofer_maker, receiver_give_money)
                        
        
    def bancrupt(self, winner, looser): #checked in game_test_only
        self.trade_cards(winner,looser)
        self.trade_buildings(winner,list(),looser,self.player_items_names(looser))
        self.player_pay_player(looser,winner,self.player_balance(looser))
        index_looser = self.player_index(looser)
        self.player_list.pop(index_looser)
        self._bancrupt_players.append(looser)
        self.PLAYER_NAMEORDER.pop(index_looser)
    #help functions for has_line    
    def monent_status_balanced(self,player_name): #checked in game_test_only
        if self.player_balance(player_name) >=0 :
            return True
        return False
        
    def monent_status_buildings(self,player_name): #checked in game_test_only
        return  self.player_items_names(player_name)

    def monent_status_buildings2(self,player_name): #checked in game_test_only objects 
        return  self.player_items(player_name)
    
    
        
    #DICT_OF_COLORS = {'Purple':2, 'Light-Green':3, 'Violet':3, 'Orange':3, 'Red':3 , 'Yellow':3, 'Dark-Green':3, 'Dark-Blue':2}   

    def can_build(self, building_name,player_name): #checked in game_test_only objects 
        index_building =  BUILDING_NAMEORDER.index(building_name)
        if self.building_owner(index_building) == player_name: #owner :)
            building_color = self._deck[index_building].get_color()
            if self.has_line(building_color,self.monent_status_buildings2(player_name)):
                return True
        return False
            
    def rail_counter(self, player_name): #checked in game_test_only objects
         list_buildings = self.monent_status_buildings(player_name)
         indexes = [BUILDING_NAMEORDER.index(building) for building in list_buildings ]
         colors = [self._deck[index].get_color()for index in indexes]
         return colors.count('STATION')
        
    def get_auction_price(self):
        return self._auction_price
    
    def get_auction_building(self):
        return self._auction_building
    
    def get_auction_players(self):
        return self._auction_players_names
    
    def get_auction_winner(self):
        return self._auction_winner
        
    def init_auction(self,building_name):#first
        player_names_auction=list()
        for i in range(len(self.player_list)):
            player_names_auction.append(self.player_list[i].name())
        self._auction_players_names = player_names_auction

    def auction_start_turn(self):#1.2
        if len(self._auction_players_names) == 1:
            return self._auction_players_names[0]
        player_name=self._auction_players_names[self._auction_index% len(self._auction_players_names)]
        return [player_name,self._auction_price] #tejushtiq igrach i cena
    
    def auction(self,player_name,money,action): # action = [bid,fold]
        if action == 'bid' and money > self._auction_price:
            self._auction_winner = money
            self._auction_winner =player_name
        elif action == 'fold':
            self._auction_players_names.remove(player_name)
        else : raise
        self._auction_index = self._auction_index + 1
        
        
    
         
    def rules(self):
        return ['условия  ']
    
    def play():
        pass
        ##roll
    #check postio
    #position action
    #adition comman
    #++next
    #return next index
    def position_type():pass
    def positio_work():pass

    
    """def has_line(self, building_color, player_buildings):
        indexes = [BUILDING_NAMEORDER.index(building) for building in player_buildings ]
        colors = [self._deck[index].get_color()for index in indexes]
        counter = colors.count(building_color)
        if counter == DICT_OF_COLORS[ building_color]:
            return True
        return False"""
    """def start turn():pass
    def end turn
        self._auction_index=0
        self._auction_building=str('BANK')
        self._auction_price = 0
        self._auction_players_names=list()
        self._auction_winner=str('')

    
    def check_position(self, index, player_name):
        if self.list_of buildings[index].owner = player_name:
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
    def act_position(self,command, player_name,building_index):pass
    def start_turn(self):
        return

    def trade_buildings(self,ofer_maker,ofer_maker_items_names, buyer,buyer_items_names ):
        ofered_items_indexes = [BUILDING_NAMEORDER.index(i)  for i in ofer_maker_items_names]
        buyer_items_indexes = [BUILDING_NAMEORDER.index(i)  for i in buyer_items_names ]
        for i in ofered_items_indexes:
            self._deck[i].buy_building(buyer)
        for i in buyer_items_indexes:
            self._deck[i].buy_building(ofer_maker)
        for i in ofer_maker_items_names:
            self._add_building_to_player(buyer,i)
            self._remove_building_from_player(ofer_maker,i)
            #self.player_list[self.player_index(ofer_maker)].add_0_remove1_item_name(i,0)
            #deleted = self.player_list[self.player_index(ofer_maker)].get_items().index(i)
            #item_is = self.player_list[self.player_index(ofer_maker)].get_items()[deleted]
            #self.player_list[self.player_index(ofer_maker)].remove_item(item_is)
        for i in buyer_items_names:
            self._add_building_to_player(buyer,i)
            self._remove_building_from_player(ofer_maker,i)
            #self.player_list[self.player_index(buyer)].add_0_remove1_item_name(i,0)
            #deleted = self.player_list[self.player_index(buyer)].get_items().index(i)
            #item_is = self.player_list[self.player_index(buyer)].get_items()[deleted]
            #self.player_list[self.player_index(buyer)].remove_item(item_is)
            #index ++ !!!!!
    """
     




    def community_chest(self, player_name):  
        card_chest = self._COMMUNITY_CHEST[self._comunity_chest_index] #izbiram karta

        mesg = card_chest[0]#suobshtenieto koeto shte vurnem
        command = card_chest[1]
        many = bool(re.search(lucky_regex['Collect'], mesg)) 
        travel =     bool(re.search(lucky_regex['Go_option'], mesg))
        get_money =  bool(re.search(lucky_regex['Get_money'],  mesg))
        free_jail =  bool(re.search(lucky_regex['Jail_free'],  mesg))
        pay_hotel =  bool(re.search(lucky_regex['Hotel_pay'],  mesg))
        everybody =  bool(re.search(lucky_regex['Each'],mesg))
                                          
        just_pay =   bool(re.search(lucky_regex['Pay'], mesg))                                   

        second_len = len(card_chest[1])#bezpolezen ..:)                                   
        if travel and get_money and second_len == 2 : #advance to go only
             self._deck.move_player(self.player_position(player_name),command[1],player_name)
             self.add_money(player_name, command[0])
             self.new_position( player_name,command[1])
             
        elif second_len == 0 and free_jail:
            self.player_list[self.player_index(player_name)].add_jail_card()

        elif second_len == 2 and pay_hotel:
            money = command[0]*self.house_count() + command[1]*self.hotel_count()                                
            self.player_list[self.player_index(player_name)].pay_money(money)
            return ['pay']
                                         
        elif everybody and  many :
            self.player_list[self.player_index(player_name)].add_money(command[0]*(len(self.player_list)-1))
            for i in range(len(self.player_list )) :
                if self.player_list[i].name() != player_name:
                    self.player_list[i].pay_money(command[0])
                
        elif just_pay:
            self.player_list[self.player_index(player_name)].pay_money(command[0])

        elif get_money:
            self.player_list[self.player_index(player_name)].add_money(command[0])
        else :
          raise Exception('test again !! fun Community chest '+ mesg)
        self._comunity_chest_index = self._comunity_chest_index + 1
        return mesg

    
    def Chance(self, player_name):#ne e testvan
        card_chest = self._CHANCE[self._chance_index] #izbiram karta

        mesg = card_chest[0]#suobshtenieto koeto shte vurnem
        command = card_chest[1]
        ifa =     bool(re.search(lucky_regex['If'], mesg))
        many = bool(re.search(lucky_regex['Collect'], mesg)) 
        travel =     bool(re.search(lucky_regex['Go_option'], mesg))
        get_money =  bool(re.search(lucky_regex['Get_money'],  mesg))
        free_jail =  bool(re.search(lucky_regex['Jail_free'],  mesg))
        pay_hotel =  bool(re.search(lucky_regex['Hotel_pay'],  mesg))
        #everybody =  bool(re.search(lucky_regex['Each'],mesg))
        nearest =  bool(re.search(lucky_regex['nearest'],mesg))                                          
        just_pay =   bool(re.search(lucky_regex['Pay'], mesg))
        spaces =   bool(re.search(lucky_regex['Spaces'], mesg))                                   

        second_len = len(card_chest[1])#bezpolezen ..:)
        player_pos = self.player_position(player_name)
        if travel and nearest and second_len == 3: #roll utility 
            if player_pos > card_chest[1][-1]:
                self.add_money( player_name,200)#minava go
                
            nearest = self.__nearest_pos_from_list( self, player_pos ,card_chest[1])
            self._deck.move_player(self.player_position(player_name),nearest,player_name)
            self.new_position( player_name,nearest)
            if self.is_owned(self, nearest, BANK):               
                return ['buy'] #ako ne e kupeno
            if not self.is_owned(self, nearest, player_name):
                roll = self.roll_dice()
                money = card_chest[1][2]*roll
                self.player_pay_player(player_name,building_owner,money )#ako plashta globa                
            else :
                return 1 #ako e na player_name

        elif travel and nearest and second_len > 3: #vlakovete
            nearest = self.__nearest_pos_from_list( self, player_pos ,card_chest[1])
            self._deck.move_player(self.player_position(player_name),nearest,player_name)
            self.new_position( player_name,nearest)
            
            if player_pos > card_chest[1][-1]:
                self.add_money( player_name,GO_MONEY)#minava go
            if self.is_owned(self, nearest, BANK):               
                return ['buy'] #ako ne e kupeno
            if not self.is_owned(self, nearest, player_name):                
                self.player_pay_player(player_name,building_owner,self.rail_counter()*card_chest[1][0] )#ako plashta globa                
            else :
                return 1 #ako e na player_name 
        elif travel and get_money and second_len == 2 : #advance to + 200 if
             self._deck.move_player(self.player_position(player_name),command[1],player_name)
             self.add_money(player_name, command[0])
             self.new_position( player_name,command[1])

        elif spaces and second_len == 1: # 3 spaces back
            self._deck.move_player(self.player_position(player_name),command[0],player_name)
            self.new_position( player_name,self.player_position(player_name) - command[0])
            return ['buy']
        elif second_len == 0 and free_jail: # jail card 
            self.player_list[self.player_index(player_name)].add_jail_card()
            
        elif second_len == 2 and pay_hotel: #pay for repairs
            money = command[0]*self.house_count() + command[1]*self.hotel_count()                                
            self.player_list[self.player_index(player_name)].pay_money(money)
            return ['pay']
        elif just_pay :
            self.pay_money(payer_name,money)
        
        elif get_money :
            self.add_money(payer_name,money)
        
        else :
            raise('errr chance '+ mesg)
        self._chance_index = self._chance_index + 1
        return mesg
            
            
            
    def comments(self):       
      """
      #using index is better !
      def buy_building(self,player_name,house_name):
        house_index = BUILDING_NAMEORDER.index(house_name)
        if self.can_pay(player_name,self._deck[building_index].get_price() and is_owned(self,house_index,BANK)) and house_index not in FORBIDDEN:
            self._deck[building_index].buy_building(player_name)
            self.player_list[self.player_index(player_name)].add_item(self._deck[building_index])
            self.player_list[self.player_index(player_name)].add_0_remove1_item_name(house_name,0)
            return True            
        else:
            return False

       """
            
"""          
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

        """   



  
        
            
            
            
        
    
