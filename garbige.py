class building:

    def __init__(self, building_name,
                 color_street='a',
                 building_price=0,                 
                 buildig_fee_globa=0,             
                
                 is_mourtaged=False,
                 owner=str(),
                 
                 ):
        
    
        self.players_on_building=list()
        self.building_name = building_name
        self.__color_street = color_street  # neighborhood po dobre vunshen
        self.building_price = building_price     
        self.buildig_fee_globa = buildig_fee_globa            
        self.is_mourtaged = False
        self.owner = ' '     
        self.house_count = 0  # (4<= houses ,  5==hotel)!!!!!!!!

    def take_fee(self, player,tax=0):
        """
         elif self.owner == ' ': # za krasota da pitam zashto ne raboti
            return 'buy'

         elif self.owner == player: #totalno ne raboti
            return 'own'
        """
        print(self.owner,  self.__color_street)
        if self.owner == ' ': # za krasota da pitam zashto ne raboti
            return 'buy'

        elif self.owner == player: #totalno ne raboti
            return 'own'
        elif self.__color_street not in ['CC','C','TAX','JAIL','FREE']:
            print(1)
            return self.__color_street
       
        
        elif not self.is_mourtaged and tax:  # take fee from player
            player.pay_money(self.with_house_fee[self.house_count])
            self.owner.add_money(self.with_house_fee[self.house_count])
            # take money and return
            print(11)
            return 'fee'
        
        elif self.__color_street == 'TAX':
             player.pay_money(self.with_house_fee[self.house_count]) 
             print(111)
             return 'TAX'

        elif self.__color_street in ['STATION','utility']:
            if self.color_street == 'STATION':
                money = [25,50,100,200]
                player.pay_money(money[self.owner.has_line('STATION')[1]])
                self.owner.add_money(money[count_stations])
                print(12)
                return 'STATION'
            else : 
                a = random.randint(1,7)
                b = random.randint(1,7)
                money = [4,10]
                player.pay_money(( a+ b)*money[self.owner.has_line('utility')[1]])
                self.owner.add_money(( a+ b)*money[count_stations])
                print(112)
                return 'utility'
        print(133)
        return self.__color_street

    def have_owner(self):
        return self.owner
        
    def build_house(self, player):
        if not self.is_mourtaged and self.owner == player:
            if player.has_line(self.color_street)[0] and self.house_count < 5:
                self.house_count = self.house_count + 1
                player.pay_money(self.perhouse_price)
                return True
        return False
    def buy_building(self, player, auctcion_buy=False):
        #print(player)
        if  self.owner == ' ' and player.budget >= self.building_price:
            self.owner = player  # change ownar
            if auctcion_buy == False:
                # if he buyies it he is on it
                self.players_on_building.append(player)
                player.pay_money(self.building_price)  # player pays for the building
                return True
            else :
                player.pay_money(auctcion_buy)
                return True
        return False
    
class Player:   
    
    def __init__(self, player_name, picture=None):
        self.player_name = player_name
        self.budget = 1500
        self.list_of_items = list() # buildigns        
        self.picture = picture
        self.in_jail = False
        self.list_cards = 0# miss :)
        self.position = 0        
        self.jail_cards = 0
    #da si napisha funkciqza jail_card in jail
    def player_budget(self):
        return self.budget

    def get_picture(self):
        return [self.picture,self.position]

    def playername(self):
        return self.player_name        

    def add_money(self, money):
        self.budget = self.budget + money

    def pay_money(self, money):
        self.budget = self.budget - money    

    def get_items(self):
        return self.list_of_items

    def jail(self):
        return self.in_jail

    def change_jail(self,status):
        self.in_jail = status

    def move_from_to(self, steps):

        old_position = self.position
        self.position = (self.position + steps)  % FIELD
        if self.position == JAIL:
            self.in_jail = 0
        return [old_position,self.position % FIELD]      

    
    def has_line(self, color):        
        counter = 0
        for i in self.list_of_items:
            if re.search(color, i.get_color()):
                counter = counter + 1
        return [counter  == DICT_OF_COLORS[color], counter]

    def house_and_hotels_counter(self):
        house = 0
        hotel = 0
        for building in self.list_of_items:
            house,hotel = house + building.house_and_hotels_list()[0], hotel +  building.house_and_hotels_list()[1]
        return [house,hotel]

    #def __str__(self):
    #    return self.player_name

    def add_items(self, items): #test only
        if items == 'bancrupt':
            self.list_of_items = list()
        else :
            self.list_of_items.append(items)
goshkoto = Player('goshkoto')
kirakis = Player('kirakis')
a = building('GO', 'FREE', 0, 0, 0),   
b =building('Mediterranean Ave.',  'Purple', 60,
                  50, 2)
