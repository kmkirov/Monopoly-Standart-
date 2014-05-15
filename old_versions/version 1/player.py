import re
class Player:

    def __init__(self, player_name, picture=None):
        self.player_name = player_name
        self.budget = 1500
        self.houses = 0
        self.list_of_items = list()
        self.picture = picture
        self.in_jail = False
        self.list_cards = list()
        self.position = 0
        self.is_bancrupt = False

    def print_player_all(self):
        print(
            'Player name: ', self.player_name, '\n budget: ',  self.budget, ' bancrupt? ', self.is_bancrupt, 'houses: ', self.houses, '\n', self.list_of_items, '\n',
            'in jail', self.in_jail, ' cards: ', self.list_cards, '\n',
            'position is', self.position)

    def playername(self):
        return self.player_name
    
    def name(self):
        return self.player_name
        
    def __str__(self):
        return self.player_name

    
    def get_items(self):
        return self.list_of_items
    
    def add_item(self,item_name):
        if item_name not in  self.list_of_items:
            self.list_of_items.append(item_name)
            
    def remove_item(self,item_name):
        if item_name  in  self.list_of_items:
            self.list_of_items.remove(item_name)
            return True
        return False
        
    def can_pay(self,price):
        return price <= self.budget 

    def get_position(self):
        return self.position

    def new_position(self,position):
        self.position=position       

    def is_playing(self):
        return self.is_bancrupt == False
    
    def new_status(self, status):
        self.is_bancrupt=status

    def has_item(self, building_name):
        return building_name in  self.list_of_items
# ne mislq che mu e tuk mqstoto
    def count_type(self, color):
        
        counter = 0
        for i in list_of_items:
            if re.search(color, i):
                counter = counter + 1
        return counter  




