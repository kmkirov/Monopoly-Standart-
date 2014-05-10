class Player:

    def __init__(self, player_name, picture=None):
        self.player_name = player_name
        self.budget = 1500
        self.houses = 0
        self.list_of_items = []
        self.picture = picture
        self.in_jail = False
        self.list_cards = []
        self.position = 0
        self.is_bancrupt = False

    def print_player_all(self):
        print(
            'Player name: ', self.player_name, '\n budget: ',  self.budget, ' bancrupt? ', self.is_bancrupt, 'houses: ', self.houses, '\n', self.list_of_items, '\n',
            'in jail', self.in_jail, ' cards: ', self.list_cards, '\n',
            'position is', self.position)

    def player_name():
        return self.player_name
        
    def __str__(self):
        return self.player_name

    
    def get_items():
        return self.list_of_items

        
    def can_pay(self,price):
        return price <= self.budget



    def get_position(sefl):
        return self.position

    def new_position(self,prosition):
        self.position=position   


    def name(self):
        return self.player_name

    def is_playing(self):
        return self.is_bancrupt == False

    def has_item(self, building_name):
        return building_name in list_of_items

    def count_type(self, color):
        import re
        counter = 0
        for i in list_of_items:
            if re.search(color, i):
                counter = counter + 1
        return counter  




