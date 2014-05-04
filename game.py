class Game:
    bancrupt_players = []
    chance_index = 0
    comunity_chest_index = 0
    def __init__(self, deck,players):
        self.deck
        pass
    def register_player(self):
        """ add new players at the beginning of the game (work with typing Yes,No to continue)"""
        register='Yes'
        while register == 'Yes':
            register='No'
            print('Enter Player name: ')
            name=input()
            if self.__valid_name(name):
            #if not macht \w* again
                player = Player(name)
                player_list.append(player)
                print('Success ', player,'added')
            else:
                print( player,'can\'t be added')
            print('do you want to add player?\n (Yes, No)')
            register = input() #true false


    def __valid_name(self,name):
        """ Check the size and content of username"""
        import re
        name_regex = r'(?P<username>^[a-zA-Z]\w{5,10}$)'
        if bool(re.match(name_regex, name)):
            names = [ i.player_name for i in player_list ]
            if name not in names :
                return True
        return False   



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

    def roll_dice(self, player_name): #pochti bezpolezna
        
        a = random.randrange(1,7)
        print(player_name,' get ',a)
        b = random.randrange(1,7)
        print('and ',b)
        #logging
        return a + b


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

    def player_game(self, command, player):
        if command

    def main_loop(self):
        import random
        pindex = 0
        while len(player_list)>1:
            a = random.randrange(1,7)
            b = random.randrange(1,7)
            new_pos = move_player_from_to(player_list[pindex].get_position(),a+b ,player_list[pindex].name())
            player_list[pindex].new_position(new_pos)
            command = check_position(new_pos)



