import re


from map import * 
from player import Player
from building import building
from global_variables import *
JAIL_FEE = 50
FREE_FROM_JAIL = False
MUST_PAY_JAIL = 2
GO_MONEY = 200
JAIL = 10
class Game():
    def __init__(self):
        self.players = list()
        self.mapa = mapa()
        self._COMMUNITY_CHEST = list(COMMUNITY_CHEST)
        self._comunity_chest_index = 0
        self._CHANCE = list(CHANCE)
        self._chance_index = 0
        self.current_player = 0
        self.chift = False
        self.rolls_counter = 0
    #def __getitem__(self,index_building):
    #    return [self.mapa[index_building].building_names(),
    #    str(self.players[self.current_player])]
    def bug_fix(self,building_index):
        for index in range(0,len(self.players)):
            if index != self.current_player:
                if self.mapa[building_index] in self.players[index].get_items():
                    return index
        return -1

    def current_position(self):
        return self.players[self.current_player].move_from_to(0)[0]
    def player_Free(self):
        return not self.players[self.current_player].jail()
    def current_player_index(self):
        return self.current_player
    def icon(self):
        return self.players[self.current_player].get_picture()[0]
    def render_name_and_budget(self):
        return [self.players[self.current_player].playername(),
                self.players[self.current_player].player_budget() ]
    
    def at(self, index_building):
        return self.mapa[index_building].building_names()
    #def who(self):
    #    return self.players[self.current_player].playername()

    def roll_dice(self):
        #
        END_TURN = False
        ASK_PLAYER = "ASK"
        JAIL_PLACE= 10
        IN_COURT = 30
        a = random.randrange(1,7)
        b = random.randrange(1,7)
        #dali imame chift
        currnet_possition = self.players[self.current_player].move_from_to(0)[0]
        
        """check 1) in jail -> rolled a pair or not (2 options)
                 2) 3dr pair in a roll got ot jail .. 
                 3) pos + rolled = jail place ->go to jail 
                 4) check if can move 
                 5) move player by rolled """
        if (self.rolls_counter > 0 and not self.chift ) or self.rolls_counter == 3 :
            self.end_turn()
            print('endturn case 1 '+  str(self.current_player_index()))
            return

        if  self.rolls_counter == 2 and a == b: #2
            self.rolls_counter = self.rolls_counter + 1
            steps = self.move_on_position(JAIL)
            #self.rolls_counter = 3
            print('endturn case 2',[steps,END_TURN, self.current_player_index()])
            return [steps,END_TURN]#'END_TURN'
                
        elif not  self.player_Free() : #1
            if a==b:
                #izliza ot zatvora i pravi 1 hod s hwyrlenoto ot nego
                position = self.move_player_by_rolled(a + b) 
                print('endturn case 4'[a + a,position[0],END_TURN], self.current_player_index())  
                self.rolls_counter = 3              
                return [a + a,position[0],END_TURN,] 
            else :
                if self.players[self.current_player].jail() == MUST_PAY_JAIL:
                    self.players[self.current_player].pay_money(JAIL_FEE)
                    self.players[self.current_player].change_jail(FREE_FROM_JAIL)
                    self.move_player(a + b)
                    print('endturn case 5',[a+b,END_TURN], self.current_player_index())
                    self.rolls_counter= 3
                    return [a+b,END_TURN]
                    
                #return [a + b]ne znam zashto e tuk ...
        elif  currnet_possition + a + b == IN_COURT:
            steps = self.move_on_position(a+b)
            #auto jail added :D
            print('endturn case 6'[steps,END_TURN], self.current_player_index())
            self.rolls_counter= 3
            return [steps,END_TURN]        
        else:
            if a==b:
                self.chift = a==b
                self.rolls_counter = self.rolls_counter + 1
            else :
                self.chift = False
                self.rolls_counter =3
            position = self.move_player_by_rolled(a + b) #old new - pos
            if position[1]<position[0]:
                self.players[self.current_player_index()].add_money(200)#minava go
            print('endturn case 7:',self.rolls_counter, a==b, self.current_player_index())
            return [a + b, a==b,position[1]]


    def end_turn(self):
        print("player end_turn fn "+ str(self.current_player))
        self.current_player = (self.current_player + 1)% len(self.players)
        self.chift = False
        self.rolls_counter = 0
        print("player start_turn fn "+ str(self.current_player))




    

    def register_player(self,name):
        if self._valid_name(name):
            self.players.append(Player(name,len(self.players)))
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



    def buy_building(self, building_index,auction):
        return self.mapa.buy_building(building_index, self.players[self.current_player],auction)

    
    def move_on_position(self,position):
        #return steps
        return self.mapa.move_player_to_position(self.players[self.current_player],position)
 
    def move_player_by_rolled(self, steps ):
        
        if not self.players[self.current_player].jail():             
            return self.players[self.current_player].move_from_to(steps) #return the positon
        else:
            return JAIL

    def take_fee(self):
        building_index = self.current_player_index()
        print(self.mapa[building_index].get_color())
        #if self.mapa[building_index] not in self.players[self.current_player].get_items():
            #plashta taksa
            #if self.bug_fix(building_index)!=-1:
            #    self.mapa[building_index].take_fee(self.players[self.current_player],1)
                
            #    return 'pay_player'#da go napisha
            

        building_index1 = self.move_player_by_rolled(0)[0]#bezpolezno za sega
        renting_result = self.mapa[building_index].take_fee(self.players[self.current_player])
        
        if renting_result =='CC':
            return self.community_chest(self.players[self.current_player])
        if renting_result =='C':
            return self.Chance(self.players[self.current_player])
        return renting_result
        #else :
        #    return 'own'
        
    #za sega nqma da go polzvam! no e za sluchq koga igrach e v zatvora i na 
    #3ti put trqbva da izleze 
    #avgradena v roll
    def stay_in_jail(self):
        self.players[self.current_player].change_jail(self.players[self.current_player].jail() + 1)
    def free_from_jail(self,staps):
        money = 50
        self.players[self.current_player].pay_money(money)
        self.players[self.current_player].change_jail(FREE_FROM_JAIL)
        self.move_player(steps)
        return 

    def jail_decision(self,money,steps=0):
        if money == JAIL_FEE: #pay for freedom
            self.playes[self.current_player].pay_money(money)
            self.playes[self.current_player].change_jail(FREE_FROM_JAIL)
            self.move_player(steps)
        elif money == 0 and self.playes[self.current_player].jail() == MUST_PAY_JAIL: #must pay ont 3rd roll
            self.playes[self.current_player].pay_money(JAIL_FEE)
            self.playes[self.current_player].change_jail(FREE_FROM_JAIL)
            self.move_player(steps)
        else:
            self.playes[self.current_player].change_jail(self.playes[self.current_player].jail() + 1)#+1 for being there

    def bancrupt(self):
        index = self.move_by_rolled(0)
        self.mapa[index].bancrupt(self.playes[self.current_player])
        self.players.pop(self.current_player)
        #self.endturn()

    def shuffler(self): #ne raboti !!!
        for i in range(random.randint(5,10)):
            random.shuffle(self._CHANCE)
        for i in range(random.randint(5,10)):
            random.shuffle(self._COMMUNITY_CHEST)

    def trade_buildings(self,offerer,offerer_buildings_index,offerer_money,receiver_name, receiver_buildings_index, receiver_money):
        names = [player.playername() for player in self.players ]
        index = names.index(receiver_name)
        return self.mapa.trade_buildings(self.players[self.current_player],offerer_buildings_index,offerer_money,self.players[index], receiver_buildings_index, receiver_money)
    
    def mourtage(self, building_index):
        return self.mapa[building_index].mourtage(self.players[self.current_player])

    def unmourtage(self, building_index):
        return self.mapa[building_index].unmourtage(self.players[self.current_player])

    def build_house(self,building_index):
        return self.mapa[building_index].build_house(self.players[self.current_player])

    def sell_house(self, building_index):
        return self.mapa[building_index].sell_house(self.players[self.current_player])
    
    
    
    
    def __nearest_pos_from_list( self, player_pos ,listed_places): #checked in game_test_only
        for i in listed_places:
            if i > player_pos :
                return i
        return listed_places[0]



    def community_chest(self,player):  
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
            self.mapa.move_player_to_position(player,command[1])#map
            player.add_money(command[0])

        elif second_len == 0 and free_jail:# ne se poddyrja
            #self.players [self.current_player].add_jail_card()
            pass
        elif second_len == 2 and pay_hotel:
            money = player.house_and_hotels_counter()
            player.pay_money(command[0] * money[0] + command[1] * money[1])
                                         
        elif everybody and  many :
            player.add_money(command[0]*(len(self.players)-1))
            for i in self.players :
                if i != player:
                    i.pay_money(command[0])
                
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
            self.mapa.move_player_to_position(player,nearest)
            if self.mapa[nearest].have_owner() == '':
                return 'buy'
            self.mapa[nearest].take_fee(player)
            

        elif travel and nearest and second_len > 3: #vlakovete
            nearest = self.__nearest_pos_from_list(  player_pos ,card_chest[1])
            self.mapa.move_player_to_position(player,nearest)            
            if player_pos >= card_chest[1][-1]:
                player.add_money( GO_MONEY)#minava go
            if self.mapa[nearest].have_owner() == '':              
                return 'buy'#ako ne e kupeno
            self.mapa[nearest].take_fee(player) 

        elif travel and get_money and second_len == 2 : #advance to + 200 if
            if player_pos >= card_chest[1][-1]:
                player.add_money( GO_MONEY)
            self.mapa.move_player_to_position(player,command[1]) 
            self.mapa[nearest].take_fee(player)
        elif travel  and second_len == 2 : #advance to + 200 if
            if player_pos >= card_chest[1][-1]:
                player.add_money( GO_MONEY)
            self.mapa.move_player_to_position(player,command[1]) 
            self.mapa[nearest].take_fee(player)
            

        elif spaces and second_len == 1: # 3 spaces back
            self.mapa.move_player_to_position(player,command[0]) 
            if self.mapa[player_pos - 3].have_owner() == '':              
                return 'buy'
            self.mapa[nearest].take_fee(player)
        
        elif second_len == 0 and free_jail: # jail card 
            pass
            #self.self.players[self.current_player].add_jail_card()
            
        elif second_len == 2 and pay_hotel: #pay for repairs
            money = player.house_and_hotels_counter()
            player.pay_money(command[0] * money[0] + command[1] * money[1])

        elif just_pay :
            player.pay_money(command[0])
        
        elif get_money :
            player.add_money(command[0])
        
        else :
           print('errr chance '+ mesg)
        self._chance_index = self._chance_index + 1
        return mesg
    
    """
#old version
    def roll_dice11(self):
        a = random.randrange(1,7)
        b = random.randrange(1,7)
        #logging
               
        if self.rolls_counter == 2 and a==b:  # otiva v zatvora zashtoto mu e 3tiq chift
            steps = self.move_on_position(JAIL)
            self._draw_counter = 3
            return [steps,'JAIL']
        elif self._draw_counter > 0 and not self._draw_dice or self._draw_counter == 3: #==endturn
            #self.end_turn()
            return [0,'END_TURN']
        #skoro dobaveno
        elif  self.move_on_position(0) == 10 : # v zatvora e 
            if a == b:
                return [a+b,'END_TURN']

            return ['jail_decision']
        else:
            self._draw_dice = a == b
            self._draw_counter = self._draw_counter + 1
            position = self.move_player_by_rolled(a + b) 
            return [a + b, a==b,position[0]] #!!!!!  


    def move_by_rolled(self,steps):
        if   self.players[self.current_player].jail != False:
            return JAIL   #can return jail
        return  self.mapa.move_player( steps ,self.players[self.current_player])"""