class deck_building:

    """ all deck_buildig have :
    public elements:
            buildig_name,
            building_price,
            color_street, 
            is_mourtaged, 
            buildig_fee_globa, 
            players_on_building = []
            owner='Bank', 
            picture=None
    functions:
        __str__(self)
        mourtage_price(self)
        hotel(self) """

    def __init__(self, buildig_name,
                 building_price,
                 color_street,
                 is_mourtaged,
                 buildig_fee_globa,
                 players_on_building=[],
                 perhouse_price,
                 owner='Bank',
                 picture=None
                 ):

        self.buildig_name = buildig_name
        self.building_price = building_price
        self.color_street = color_street  # neighborhood po dobre vunshen
        self.is_mourtaged = is_mourtaged
        self.buildig_fee_globa = buildig_fee_globa
        self.players_on_building = players_on_building
        self.perhouse_price = perhouse_price
        self.owner = owner
        self.house_count = 0  # (4<= houses ,  5==hotel)!!!!!!!!
        self.picture = picture  # optional
        #kompromis za tochnost ne moga da namerq formulata ... 
        self.with_house_fee = [self.buildig_fee_globa,
                               5 * self.buildig_fee_globa, 
                               15 * self.buildig_fee_globa,
                               45 * self.buildig_fee_globa,
                               62 * self.buildig_fee_globa,
                               80 * self.buildig_fee_globa]

        
    def show_building_info(self):
        print('Name: ',self.buildig_name,'\n',
            'price: ',self.building_price,'\n',
            'mourtage: ',self.mourtage_price,'\n',
            'One house price: ',self.perhouse_price,'\n',
            'Rent: \n'
            'None one two tree four hotel ',self.with_house_fee,'\n')
        #return None 

    def mourtage_price(self):
        return self.building_price / 2

    def kak_da_namerq_liniq_ot_ulici(self):
        pass
    

    def get_building_name(self):
        return self.buildig_name


    def take_fee(self):
        return self.with_house_fee[self.house_count]


    def __str__(self):
        print(
            'Name of building: ', self.buildig_name, ', price is: ', self.building_price,
            ', color is:', self.color_street, '.\n', ' Mourtaged value is: ', self.is_mourtaged,
            ', owner is ', self.owner, ', house count is ', self.house_count, '.')
        return str(self.owner)

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

\#globalen////\\\\
deck_buldings_ordered=[  deck_building('start',0,'BLACK',0 ),
        deck_building('Old Kent Road',60,'brown',False, 2 ),
        deck_building('Whitechapel Road',60,'brown',False, 4 ),
        deck_building( 'Take Card',0,'BLACK',False, 0),
        deck_building('Station',200,'BLACK',False, 25 ),
        deck_building('cheshma',150,'BLACK',False, 0 ),
        deck_building( 'Old Kent Road',200,'red',False, 10),
        deck_building('Old Kent Road',600,'red',False, 200 ),
        deck_building( 'Old Kent Road',300,'red',False, 20),
]
        
///////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
class Player:
    def __init__(self, player_name,picture=None):
        self.player_name = player_name
        self.budget = 1500
        self.houses = 0
        self.list_of_items = []
        self.picture = picture
        self.in_jail = False
        self.list_cards = []
        self.position = 0
////////////////////////////////////////////////\\\\\\
import random
class playing_deck:
    """ 
    def roll_dice(self, player_name):
        return result from 2 rolled dices and print smth




        """


    def __init__(self,player_list,deck):
        player_list = [] #moje da e dict
        deck_buldings_ordered ....
    

    def roll_dice(self, player_name):
        a = random.randrange(1,7)
        print(player_name,' get ',a)
        b = random.randrange(1,7)
        print('and ',b)
        #logging
        return a + b

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
    
    def bancrupt(self, winer,loser):
        w = player_list[ player_list.index(winner)]
        l = player_list[ player_list.index(winner)]
        a = deck_buldings_ordered
        for building in l.list_of_items:
            if a[a.index(building)].house_count>0:
                destroy_house(self,a.index(building),l.name,a[a.index(building)].house_count )
        w.budget = w.buget + l.budget
        w.list_of_items.append(l.list_of_items)
    
    def end_turn(self):
        pass
    def special_card(self):
        pass


//////////\\\\\\\\\\\\\\\\
chance_index_arr = [('vzemam 30',30),('str',value) ] #da gi razmesvam predi igra
comunity_chest
class Game:
    chance_index = 0
    comunity_chest_index = 0
    def __init__(self, deck,players):
        self.deck
        pass
    def register_player(self):
        register=True
        while register:
            register=False
            name=input()
            #if not macht \w* again
            player = Player(name)
            player_list.add(player)
            print('do you want to add player?\n')
            register = input() #true false


            
    def main_loop(self):
        index = 0
        while len(player_list)>1:
            player= player_list[index]
            roll_dice(self, player_name)
            move_player_from_to(self,player.position,player_name)...


