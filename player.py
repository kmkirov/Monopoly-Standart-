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
        self.is_bancrupt = False

    def can_pay(price):
        return price <= self.budget


    def name(self):
        return self.player_name


    def is_playing(self):
        return self.is_bancrupt == False

    def has_item(self,building_name):
        return building_name in list_of_items

    def count_type(self, color):
        import re
        counter = 0
        for i in list_of_items:
            if re.search(color, i):
                counter = counter + 1
        return counter




