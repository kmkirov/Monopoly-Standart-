import player


class building:

    def __init__(self, building_name,
                 color_street='FREE',
                 building_price=0,
                 perhouse_price=0,
                 buildig_fee_globa=0,
                 fee_with_one_house=0,
                 fee_with_two_house=0,
                 fee_with_three_house=0,
                 fee_with_four_house=0,
                 fee_with_five_house=0,
                 players_on_building=[],
                 is_mourtaged=False,
                 owner='BANK',
                 picture=None
                 ):

      self.building_name = building_name
      self.color_street = color_street  # neighborhood po dobre vunshen
      self.building_price = building_price
      self.perhouse_price = perhouse_price
      self.buildig_fee_globa = buildig_fee_globa

      self.fee_with_one_house = fee_with_one_house
      self.fee_with_two_house = fee_with_two_house
      self.fee_with_three_house = fee_with_three_house
      self.fee_with_four_house = fee_with_four_house
      self.fee_with_five_house = fee_with_five_house

      self.players_on_building = list()
      self.is_mourtaged = False
      self.owner = str()

      self.picture = picture  # optional
      self.house_count = 0  # (4<= houses ,  5==hotel)!!!!!!!!
      self.with_house_fee = [self.buildig_fee_globa,
                             self.fee_with_one_house,
                             self.fee_with_two_house,
                             self.fee_with_three_house,
                             self.fee_with_four_house,
                             self.fee_with_five_house]

    def mourtage(self, player):
        if self.owner == player and not self.is_mourtaged:
            player.add_money(self.building_price * 0.4)
            return True
        else:
            return False

    def unmourtage(self, player):
        if self.owner == player and not self.is_mourtaged:
            player.pay_money(self.building_price / 2)
            return True
        else:
            return False

    def get_color(self):
        return self.color_street

    def delete_player(self, player):
        if player in self.players_on_building:
            self.players_on_building.remove(player)

    def all_players(self):
        return self.players_on_building

    def buy_building(self, player, auctcion_buy=False):
        if self.owner == '' and player.budget >= self.building_price:
            self.owner = player  # change ownar
            if auctcion_buy == False:
                # if he buyies it he is on it
                self.players_on_building.append(player)
                player.pay_money(self.building_price)  # player pays for the building
                #test
                #player.add_items(self) ne
                return True
            else :
                player.pay_money(auctcion_buy)
                return True
        return False

    def house_and_hotels_list(self):
        if self.house_count == 5:
            houses = 0
            hotel = 1
        else:
            houses = self.house_count
            hotel = 0
        return [houses, hotel]

    def bancrupt(self, player):#bancrupt a player and add to owner
        #print(self.owner.get_items())
        if player == self.owner:
            return 
        for item in player.get_items():
            self.owner.get_items().append(item)
            item.change_owner(self.owner)  

        self.owner.add_money(player.player_budget())#take money
        player.add_items('bancrupt')
        #print(self.owner.get_items())


    def change_owner(self, player):  # on trade only
        if self.owner != '' and self.house_and_hotels_list() ==[0,0]:
            self.owner = player
            return True
        return False

    def take_fee(self, player):
        # add player to list of players
        if player not in self.players_on_building:
            self.players_on_building.append(player)

        if not self.is_mourtaged and self.owner != '':  # take fee from player
            player.pay_money(self.with_house_fee[self.house_count])
            self.owner.add_money(self.with_house_fee[self.house_count])
            # take money and return
            return 'fee'
        elif self.owner == player:
            return 'own'
        elif self.color_street == 'TAX':
             player.pay_money(self.self.with_house_fee[self.house_count]) 
             return 'TAX'
        elif self.color_street in ['STATION','utility']:
            if color_street == 'STATION':
                count_stations = self.owner.has_line('STATION')[1]
                money = [25,50,100,200]
                player.pay_money(money[count_stations])
                self.owner.add_money(money[count_stations])
                return 'STATION'
            else : 
                count_stations = self.owner.has_line('utility')[1]
                a = random.randint(1,7)
                b = random.randint(1,7)
                money = [4,10]
                player.pay_money(( a+ b)*money[count_stations])
                self.owner.add_money(( a+ b)*money[count_stations])
                return 'utility'
        return self.color_street

    def have_owner(self):
        return self.owner
        
    def build_house(self, player):
        if not self.is_mourtaged and self.owner == player:
            if player.has_line(self.color_street)[0] and self.house_count < 5:
                self.house_count = self.house_count + 1
                player.pay_money(self.perhouse_price)
                return True
        return False

    def sell_house(self,player):
        if not self.is_mourtaged and self.owner == player:
            if self.house_count > 0:
                self.house_count = self.house_count - 1
                player.add_money(self.perhouse_price * 0.40)
                return True
        return False

    def __str__(self):
        return self.building_name
  