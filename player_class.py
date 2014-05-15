import re
class Player:
    
    def pay_money(self, money):
        if self.can_pay(money):
            self.budget = self.budget - money
            return True
        return False
    
    def __init__(self, player_name, picture=None):
        self.player_name = player_name
        self.budget = 1500
        self.houses = 0
        self.list_of_items = list() # buildigns
        self.list_of_items_names = list() #just name of building
        self.picture = picture
        self.in_jail = False
        self.list_cards = list()
        self.position = 0
        self.is_bancrupt = False
        self.jail_cards = 0
    def add_0_remove1_item_name(self,item_name,flag):
        if flag:
            self.list_of_items_names.remove(item_name)
        else :
            self.list_of_items_names.append(item_name)
            
    def add_jail_card(self):
        self.jail_cards = self.jail_cards + 1
        
    def have_jail_card():        
        return 0 == self.jail_cards
    def remove_jail_card():
        self.jail_cards = self.jail_cards - 1
        
        
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

    def add_money(self, money):
        self.budget = self.budget + money
    def get_money(self):
        return self.budget
        
    def get_items(self):
        return self.list_of_items
    #tova sa strukturi
    def add_item(self,item):
        if item_name not in  self.list_of_items:
            self.list_of_items.append(item)
            
    def remove_item(self,item):
        if item_name  in  self.list_of_items:
            self.list_of_items.remove(item)
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




