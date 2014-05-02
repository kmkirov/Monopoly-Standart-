class Game:
    bancrupt_players = []
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

    def auction(self, building_name):
        players_acuction=[ player for player in player_list if player.is_playing()]

        auction_players = player_list
        auction_price = 1
        player_index=0
        while len(auction_players) > 1:
            on_turn_player = players_acuction[player_index % len(players_acuction)]
            print(on_turn_player.name(),' the auction price for',building_name,
             ' is ',auction_price,'bid or fold')
            answer=input('fold, bid or auction_price + your number ')

            if answer == 'fold':
                print(player_index % len(players_acuction), 'folded the auction')
                auction_players.pop(player_index % len(players_acuction))
            elif answer == 'bid':
                auction_price = auction_price + 1 
                player_index = player_index + 1
            else :
                answer=int(answer)
                if on_turn_player.can_pay(answer):
                    auction_price = auction_price + answer
                    print(on_turn_player, 'bided to ',auction_price )
                    player_index = player_index + 1

        print('The winner is ',auction_players[0], 'bought ',
         building_name, 'for', auction_price)
        pl_index =player_list.index(auction_players[0])
        player_list[pl_index].budget =  player_list[pl_index].budget - auction_price
        player_list[pl_index].self.list_of_items.append(building_name)##slagam imeto na sgradata :)

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





    def main_loop(self):
        index = 0
        while len(player_list)>1:
            player= player_list[index]
            roll_dice(self, player_name)
            move_player_from_to(self,player.position,player_name)...
