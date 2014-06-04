import re

import player, building , map
JAIL_FEE = 50
FREE_FROM_JAIL = False
MUST_PAY_JAIL = 2
class Game():
    def __init__(self,mapa):
        self.players = list()
        self.mapa = list(mapa)
        self.current_player = 0

    def roll_dice(self): #checked in game_test_only
        a = random.randrange(1,7)
        b = random.randrange(1,7)
        #logging
        return [a + b, a==b] #!!!!!  

    def register_player(self,name):
        if self._valid_name(name):
            self.players.append(Player(name))
            return True
        return False
                        
    def _valid_name(self,name):
        name_regex = r'(?P<username>^[a-zA-Z]\w{5,10}$)'
        if bool(re.match(name_regex, name)):
            names = [ i.playername() for i in self.players ]
            if name not in names :
                return True
        return False

    def all_player(self): #za gui
        return [player.get_picture() for player in self.players]

    def end_turn(self):
        self.current_player = (self.current_player + 1)% len(self.players)

    def buy_building(self, building_index):
        mapa.buy_building(building_index, self.players[self.current_player])

    def trade_buildings(offerer,offerer_buildings_index,offerer_money,receiver_name, receiver_buildings_index, receiver_money):
        index = [player.playername() for player in self.players].index(receiver_name)
        map.trade_buildings(self.players[self.current_player],offerer_buildings_index,offerer_money,self.players[index], receiver_buildings_index, receiver_money)
    
    def mourtage(self, building_index):
        self.mapa[building_index].mourtage(self.players[self.current_player])

    def unmourtage(self, building_index):
        self.mapa[building_index].unmourtage(self.players[self.current_player])

    def build_house(self,building_index):
        self.mapa[building_index].build_house(self.players[self.current_player])

    def sell_house(self, building_index):
        self.mapa[building_index].sell_house(self.players[self.current_player])
    
    def take_fee(self,building_index):
        result = self.mapa[building_index].take_fee(self.players.[self.current_player]))
        if renting_result in ['comuniti chest', 'chance']:
        if chance() == 'buy'
 
    def move_player(self, steps ,player):
        if not self.playes[self.current_player].jail():             
            return self.map.move_player_by_roll(self.players[self.current_player],steps) #return the positon
        else:
            return JAIL

    def jail_decision(self,money,steps):
        if money = JAIL_FEE:#pay for freedom
            self.playes[self.current_player].pay_money(money)
            self.playes[self.current_player].change_jail(FREE_FROM_JAIL)
            self.move_player(steps)
        elif money = 0 and self.playes[self.current_player].jail() == MUST_PAY_JAIL: #must pay ont 3rd roll
            self.playes[self.current_player].pay_money(JAIL_FEE)
            self.playes[self.current_player].change_jail(FREE_FROM_JAIL)
            self.move_player(steps)
        else:
            self.playes[self.current_player].change_jail(self.playes[self.current_player].jail() + 1)#+1 for being there
    
    
    def move_on_position(self,position):
        return self.mapa.move_player_to_position(self.players[self.current_player],position)

    def bancrupt(self):
        index = self.move_by_rolled(0)
        self.mapa[index].bancrupt(self.playes[self.current_player])
        self.players.pop(self.current_player)
        #self.endturn()


    """def move_by_rolled(self,steps):
        if   self.players[self.current_player].jail != False:
            return JAIL   #can return jail
        return  self.mapa.move_player( steps ,self.players[self.current_player])"""
        def shuffler(self):
        for i in range(random.randint(5,10)):
            random.shuffle(self._CHANCE)
        for i in range(random.randint(5,10)):
            random.shuffle(self._COMMUNITY_CHEST)


    
    
    
    
    def __nearest_pos_from_list( self, player_pos ,listed_places): #checked in game_test_only
        for i in listed_places:
            if i > player_pos :
                return i
        return listed_places[0]



    def community_chest(self, player):  
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
            self.self.mapa.move_player_to_position(self.players[self.current_player],command[1])#map
            player.add_money(command[0])

        elif second_len == 0 and free_jail: ne se poddyrja
            self.player_list[self.player_index(player_name)].add_jail_card()

        elif second_len == 2 and pay_hotel:
            money = player.house_and_hotels_counter()
            player.pay_money(command[0] * money[0] + command[1] * money[1])
                                         
        elif everybody and  many :
            player.add_money(command[0]*(len(self.player_list)-1))
            for i in self.players :
                if self.players[i] != player:
                    self.players[i].pay_money(command[0])
                
        elif just_pay:
            player.pay_money(command[0])

        elif get_money:
            player.add_money(command[0])
        else :
          raise Exception('test again !! fun Community chest '+ mesg)
        #ne znam dali vaji oshte
        self._comunity_chest_index = self._comunity_chest_index + 1
        return mesg

    
    def Chance(self, player):#ne e testvan
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
        player_pos = player.move_from_to(0)[0]#self.player_position(player_name)
        if travel and nearest and second_len == 3: #roll utility 
            if player_pos > card_chest[1][-1]:
                player.add_money( 200)#minava go
                
            nearest = self.__nearest_pos_from_list(  player_pos ,card_chest[1])
            self.self.mapa.move_player_to_position(self.players[self.current_player],nearest)
            if self.mapa[nearest].have_owner() == '':
                return 'buy'
            self.mapa[nearest].get_rent(player)
            

        elif travel and nearest and second_len > 3: #vlakovete
            nearest = self.__nearest_pos_from_list(  player_pos ,card_chest[1])
            self.self.mapa.move_player_to_position(self.players[self.current_player],nearest)            
            if player_pos > card_chest[1][-1]:
                player.add_money( GO_MONEY)#minava go
            if self.mapa[nearest].have_owner() == '':              
                return 'buy'#ako ne e kupeno
            self.mapa[nearest].get_rent(player) 

        elif travel and get_money and second_len == 2 : #advance to + 200 if
            if player_pos > card_chest[1][-1]:
                player.add_money( GO_MONEY)
            self.self.mapa.move_player_to_position(self.players[self.current_player],command[1]) 
            self.mapa[nearest].get_rent(player)
            

        elif spaces and second_len == 1: # 3 spaces back
            self.self.mapa.move_player_to_position(self.players[self.current_player],command[1]) 
            if self.mapa[player_pos - 3].have_owner() == '':              
                return 'buy'
            self.mapa[nearest].get_rent(player)
        
        elif second_len == 0 and free_jail: # jail card 
            self.player_list[self.player_index(player_name)].add_jail_card()
            
        elif second_len == 2 and pay_hotel: #pay for repairs
            money = player.house_and_hotels_counter()
            player.pay_money(command[0] * money[0] + command[1] * money[1])

        elif just_pay :
            player.pay_money(command[0])
        
        elif get_money :
            player.add_money(money)
        
        else :
            raise('errr chance '+ mesg)
        self._chance_index = self._chance_index + 1
        return mesg
            