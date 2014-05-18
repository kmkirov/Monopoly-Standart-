class deck_building:
    def get_color(self):
        return self.color_street
    
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

        self.players_on_building = list (players_on_building)
        self.is_mourtaged = is_mourtaged
        self.owner = str(owner)

        self.picture = picture  # optional
        self.house_count = 0  # (4<= houses ,  5==hotel)!!!!!!!!
        self.with_house_fee = [self.buildig_fee_globa,
                               self.fee_with_one_house,
                               self.fee_with_two_house,
                               self.fee_with_three_house,
                               self.fee_with_four_house,
                               self.fee_with_five_house]
    def house_cost(self): 
        return self.perhouse_price
    
    def get_price(self):
        return self.building_price

    def mourtage_price(self):
        return self.building_price / 2
    
    def add_player(self,player_name):
        if player_name not in self.players_on_building:
            self.players_on_building.append(player_name)
    
    def delete_player(self,player_name):
        if player_name  in self.players_on_building:
            self.players_on_building.remove(player_name)
    
    def all_players(self):
        return self.players_on_building
    
    def buy_building(self, player_name):
        self.owner = player_name
        
    def count_houses(self):
        if self.house_count == 5:
            return 0
        else:
            return self.house_count

    def has_hotel(self):
        return self.house_count == 5

    def get_name(self):
        return self.building_name

    def get_owner(self):
        return self.owner

    def take_fee(self):
        if not self.is_mourtage() and self.owner != 'BANK':
            return self.with_house_fee[self.house_count]
        else:
            return 0
        
    def buy_building(self, player_name):
        self.owner = player_name
        
    def can_buy(self):
        return self.owner == 'BANK'
    
    def build_house(self):
        if not self.is_mourtage() :
            if self.house_count < 5:
                self.house_count = self.house_count + 1
                return True
        return False
    
    def destroy_house(self):
        if not self.is_mourtage() :
            if self.house_count > 0:
                self.house_count = self.house_count - 1
                return True
        return False

    def is_mourtage(self):
        return self.is_mourtaged != False

    def change_mourtage(self,option):
        self.is_mourtaged = option

    def can_build(self, player_name):
        return (self.owner == player_name and self.is_mourtage() == False)

    def __str__(self):
        print(
            'Name of building: ', self.building_name, ', price is: ', self.building_price,
            ', color is:', self.color_street, '.\n', ' Mourtaged value is: ', self.is_mourtaged,
            ', owner is ', self.owner, ', house count is ', self.house_count, '.')
        return str(self.owner)

    def show_building_info(self):
        print('Name: ', self.building_name, '\n',
              'price: ', self.building_price, '\n',
              'mourtage: ', self.mourtage_price, '\n',
              'One house price: ', self.perhouse_price, '\n',
              'Rent: \n'
              'None one two tree four hotel ', self.with_house_fee, '\n')
