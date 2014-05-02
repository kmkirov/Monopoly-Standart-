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

Community Chest list:

{'Advance to Go (Collect $200)':200,
'Bank error in your favor – collect $75':75,
'Doctor\'s fees – Pay $50':50,
'Get out of jail free – this card may be kept until needed, or sold':card_collection+1
'Go to jail – go directly to jail – Do not pass Go, do not collect $200':200
'It is your birthday Collect $10 from each player':10,
'Grand Opera Night – collect $50 from every player for opening night seats':50
'Income Tax refund – collect $20':20
'Life Insurance Matures – collect $100':100,
'Pay Hospital Fees of $100':100,
'Pay School Fees of $50':,
'Receive $25 Consultancy Fee':25,
'You are assessed for street repairs – $40 per house, $115 per hotel':perhotel,
'You have won second prize in a beauty contest– collect $10':10,
'You inherit $100':100,
'From sale of stock you get $50':50,
'Holiday Fund matures - Receive $100':100}

Chance list:

{'Advance to Go (Collect $200)' :200,
'Advance to Illinois Ave.':index[ave],
'Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned,\
  throw dice and pay owner a total ten times the amount thrown.':2x,
'Advance token to the nearest Railroad and pay owner twice the rental to which he/she is otherwise entitled.\
 If Railroad is unowned, you may buy it from the Bank. (There are two of these.)':2x,
'Advance to St. Charles Place – if you pass Go, collect $200':200,
'Bank pays you dividend of $50':50,
'Get out of Jail free – this card may be kept until needed, or traded/sold':jail,
'Go back 3 spaces',cur[index -3],
'Go directly to Jail – do not pass Go, do not collect $200':200,
'Make general repairs on all your property – for each house pay $25 – for each hotel $100':perhotel,
'Pay poor tax of $15':15,
'Take a trip to Reading Railroad – if you pass Go collect $200':200 + indexdetect,
'Take a walk on the Boardwalk – advance token to Boardwalk':index,
'You have been elected chairman of the board – pay each player $50':50 each
'Your building loan matures – collect $150':150,
'You have won a crossword competition - collect $100 ':100 }