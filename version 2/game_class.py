import random
import re

from playing_deck import playing_deck
from global_variables import COMMUNITY_CHEST, CHANCE,lucky_regex,LIST_OF_BUILDINGS
from player import Player


GO = 0
Jail = 10
class Game:
    
    
    def __init__(self):
        self._deck = playing_deck(list(LIST_OF_BUILDINGS)) #igralnoto pole
        self._bancrupt_players = set()
        self.player_list = list()
        self.PLAYER_NAMEORDER = list()
        self._COMMUNITY_CHEST = COMMUNITY_CHEST #globalno
        self._comunity_chest_index = 0
        self._CHANCE = CHANCE
        self._chance_index = 0
        self._turn_index=0
        self._auction_index=0
        self._auction_building='BANK'
        self._auction_price = 0
        self._auction_players_names=list()
        
    
         

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
    
    def roll_dice(self): #pochti bezpolezna
        a = random.randrange(1,7)
        b = random.randrange(1,7)
        #logging
        return a + b
    
        
    def new_position(self, player_name, position):
        return self.player_list[self.player_index(player_name)].new_position(position)

    def move_player_by_rolled(self,rolled,player_name):
        old_position = self.player_position(player_name)
        self.new_position(player_name, rolled + old_position)    
    
    def player_position(self, player_name):
        return self.player_list[self.player_index(player_name)].get_position()
        
        
    def on_starting(self):#da ne se polzva
        random.shuffle(self.PLAYER_NAMEORDER)
        for index in range(len(self.player_list) + 1):
            self.PLAYER_NAMEORDER.append(self.player_list[index].name())
        
                                                
    def player_index(self,player_name): #priemam che e korektno
        return self.PLAYER_NAMEORDER.index(player_name)

    def player_items_names(self,player_name):
        index = self.player_index(player_name)
        return self.player_list[index].get_items()
        
    def player_balance(self,player_name):
        return self.player_list[self.player_index(player_name)].get_money()
   
    def house_count(self,player_name):
        index = self.player_index(player_name)
        counter = 0
        for building in self.player_list[index].self.list_of_items():
            counter = counter + building.count_houses()
        return counter

    def hotel_count(self,player_name):
        index = self.player_index(player_name)
        counter = 0
        for building in self.player_list[index].self.list_of_items():
            if building.has_hotel():
                counter = counter + 1
        return counter
            
    def add_money(self,player_name, money):
        self.player_list[self.player_index(player_name)].add_money(money)
        
    def pay_money(self,player_name,money):
        self.player_list[self.player_index(player_name)].pay_money(money)
        
    def player_pay_player(self, payer, receiver, money):
        self.pay_money(payer,money)
        self.add_money(receiver,money)
        
        
    def can_pay(self,player_name,money):
        return self.player_list[self.player_index(player_name)].can_pay(money)
 
    def __nearest_pos_from_list( self, player_pos ,listed_places):
        for i in listed_places:
            if i > pos :
                return i
        return listed_places[0]
                

    def is_owned(self, building_index, player_name):
        if player_name == self._deck[building_index].get_owner():
            return True
        return False

    def building_owner(self, building_index):
        return self._deck[building_index].get_owner()
            

    def buy_building(self,player_name,house_name):
        house_index = BUILDING_NAMEORDER.index(house_name)
        if self.can_pay(player_name,self._deck[building_index].get_price() and is_owned(self,house_index,BANK)):
            self._deck[building_index].buy_building(player_name)
            self.player_list[self.player_index(player_name)].add_item(self._deck[building_index])
            self.player_list[self.player_index(player_name)].add_0_remove1_item_name(house_name,0)
            return True            
        else:
            return False
                        
         
    #def sell_building(self,seller,buyer,house_name):
        
             
    def mourtage(self,player_name,house_name):
        house_index = BUILDING_NAMEORDER.index(house_name)
        if self.is_owned(house_index,player_name) and not self._deck[building_index].is_mourtage:
            self._deck[building_index].change_mourtage(True)
            self.add_money(player_name,self._deck[building_index].mourtage_price())
        
    def unmourtage(self, player_name, house_name):
        house_index = BUILDING_NAMEORDER.index(house_name)
        if self.is_owned(house_index,player_name) and  self._deck[building_index].is_mourtage:
            self._deck[building_index].change_mourtage(False)
            self.pay_money(player_name,self._deck[building_index].mourtage_price())
        
    def build_house(self,player_name,house_name):
        house_index = BUILDING_NAMEORDER.index(house_name)
        if self.is_owned( house_index, player_name) and have_liniq:
            if self._deck[building_index].build_house() and self.can_pay(player_name,self._deck[building_index].house_cost()):
                self.pay_money(player_name,self._deck[building_index].house_cost())
                return True
        return False
                        
    def sell_house(self,player_name,house_name):
        house_index = BUILDING_NAMEORDER.index(house_name)
        if self.is_owned( house_index, player_name) :
            if self._deck[building_index].destroy_house():
                self.add_money(player_name,self._deck[building_index].house_cost()/2)
        return False

    #podavat se list ot 1 argumenti i list ot drugi i 2 playera i se razmenqt :)  bez jail card
    def trade_buildings(self,ofer_maker,ofer_maker_items, buyer,buyer_items ):
        ofered_items_indexes = [BUILDING_NAMEORDER.index(i)  for i in ofer_maker_items]
        buyer_items_indexes = [BUILDING_NAMEORDER.index(i)  for i in buyer_items]
        for i in ofered_items_indexes:
            self._deck[i].buy_building(buyer)
        for i in buyer_items_indexes:
            self._deck[i].buy_building(ofer_maker)
        for i in ofer_maker_items:
            self.player_list[self.player_index(ofer_maker)].add_0_remove1_item_name(i,0)
            deleted = self.player_list[self.player_index(ofer_maker)].get_items().index(i)
            item_is = self.player_list[self.player_index(ofer_maker)].get_items()[deleted]
            self.player_list[self.player_index(ofer_maker)].remove_item(item_is)
        for i in buyer_items:
            self.player_list[self.player_index(buyer)].add_0_remove1_item_name(i,0)
            deleted = self.player_list[self.player_index(buyer)].get_items().index(i)
            item_is = self.player_list[self.player_index(buyer)].get_items()[deleted]
            self.player_list[self.player_index(buyer)].remove_item(item_is)
            #index ++ !!!!!

    def trade_cards(self,offer_maker, receiver):
        if self.player_list[self.player_index(offer_maker)].have_jail_card():
             self.player_list[self.player_index(offer_maker)].remove_jail_card()
             self.player_list[self.player_index(receiver)].add_jail_card()
             return True
        return False
                
                        
#narochno ne proverqvam dali moje da plati koito i da e
    def trade_money(self, ofer_maker, receiver, ofer_maker_give_money, receiver_give_money):
        self.player_pay_player( ofer_maker, receiver, ofer_maker_give_money)
        self.player_pay_player( receiver, ofer_maker, receiver_give_money)
                        
    def have_line(self,player,building_name):
        
    def bancrupt(self, winner,looser):
        while self.trade_cards(winner,looser)
        self.trade_buildings(winner,list(),looser,self.player_items_names(looser))
        self.player_pay_player(looser,winner,self.player_balance(looser))
        
    def monent_status_balanced(self,player_name):
        if self.player_balance(player_name) >=0 :
            return True
        return False
        
    def monent_status_buildings(self,player_name):
        return  self.player_items_names(player_name)
    
    def has_line(self, building_color, player_buildings):
        indexes = [BUILDING_NAMEORDER.index(building) for building in player_buildings ]
        colors = [self._deck[index].get_color()for index in indexes]
        counter = colors.count(building_color)
        if counter == DICT_OF_COLORS[ building_color]:
            return True
        return False
        
    #DICT_OF_COLORS = {'Purple':2, 'Light-Green':3, 'Violet':3, 'Orange':3, 'Red':3 , 'Yellow':3, 'Dark-Green':3, 'Dark-Blue':2}   
    def can_build(self, house_name,player_name):
        if self.building_owner(house_name) == player_name: #owner :)
            index = BUILDING_NAMEORDER.index(house_name)
            building_color = self._deck[index].get_color()
            if self.has_line(building_color,self.monent_status_buildings(player_name)):
                return True
        return False
            
        
    def get_auction_price(self):
        return self._auction_price
    def get_auction_building(self):
        return self._auction_building
     def get_auction_players(self):
        return self._auction_players_names
        
    def init_auction(self,building_name):
        player_names_auction=list()
        for i in range(len(self.player_list))
            player_names_auction.append(self.player_list[i].name())
        self._auction_players_names = player_names_auction
    def auction_player(self):
        
    def auction(self):
        player_index = 
    def rail_counter(self, player_name)
         list_buildings = self.monent_status_buildings(player_name)
         indexes = [BUILDING_NAMEORDER.index(building) for building in player_buildings ]
         colors = [self._deck[index].get_color()for index in indexes]
         return colors.count('RAIL')
         
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
    def position_type()
    def positio_work()
    
    def start turn
    def end turn



     













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
            
            
            
            
                
            
            
                



  
        
            
            
            
        
    
