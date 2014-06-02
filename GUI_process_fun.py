from game import Game
from multiprocessing import Process, Value
import time,sys
from buttons import *
from global_variables import  *

#ot internet!!!
import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *

def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass

def display_box(screen, message):
  "Print a message in a box in the middle of the screen"
  fontobject = pygame.font.Font(None,18)
  pygame.draw.rect(screen, (0,0,0),
                   ((screen.get_width() / 2) - 100,
                    (screen.get_height() / 2) - 10,
                    200,20), 0)
  pygame.draw.rect(screen, (255,255,255),
                   ((screen.get_width() / 2) - 102,
                    (screen.get_height() / 2) - 12,
                    204,24), 1)
  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, (255,255,255)),
                ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
  pygame.display.flip()

def ask(screen, question):
  "ask(screen, question) -> answer"
  pygame.font.init()
  current_string = []
  display_box(screen, question + ": " + ''.join(current_string))
  while 1:
    inkey = get_key()
    if inkey == K_BACKSPACE:
      current_string = current_string[0:-1]
    elif inkey == K_RETURN:
      break
    elif inkey == K_MINUS:
      current_string.append("_")
    elif inkey <= 127:
      current_string.append(chr(inkey))
      a = []
      a =str(question) + ": " + ''.join(current_string)
    display_box(screen,a )
  return ''.join(current_string)

"""
def main():
  screen = pygame.display.set_mode((320,240))
  #game register
  az = ask(screen, "Name")
  print(az)
  print( " was entered")
  pygame.quit()
if __name__ == '__main__': main()

"""




def roll_dices(game,display): #testvan!!!!
    
    
    rolled = game.roll_dice()
    font = pygame.font.Font(None, 30)
    textImg = font.render( "rolled "+ str(rolled[0]), 1, (255,0,0))
    display.blit( textImg, (200,150) )# za da e nai otgore
    
    pygame.display.update()
    
    #game processing ...
    
    print('current rolled' +  str(rolled[0]) + ' was diece '+str(rolled[1]))
  














 # frames per second setting
go_player_picturex = 497
go_player_picturey = 501

WHITE = (255, 255, 255)
start_trip = 500
end_trip = 50
step_trip = 46
magic_trip = 20 #bez popravkata ne e krasivo :)
"""
pygame.font.init()
    font = pygame.font.Font( pygame.font.get_default_font(), 12 )
    text = font.render( string, False, color )
    text.blit( text, picture, ( x, y ) )
    pygame.font.quit()
"""
#------------- register player just view process version----------
def register_player1(game): #ne raboti s
    pygame.init()
    window = pygame.display.set_mode((400, 200), 0, 32)
    
    pygame.display.set_caption('Registration')
    background = pygame.image.load('pictures/bG.jpg')
    window.blit(background,(0, 0))

    font = pygame.font.Font(None, 30)
    textImg = font.render( "   Register player (type and pres enter)", 1, (255,0,0))
    window.blit( textImg, (0,0) )# za da e nai otgore

    pygame.display.update()
    pygame.font.quit()
    #game processing ...
    player_name = ask(window,'name')#vyvejdaneto
    print(player_name + ' was entered.')
    successful = game.register_player(player_name)
    print(player_name + ' was entererd ' + str(successful))
    pygame.quit()


#------------- register player just view rectangular version----------
def register_player(game,display): #testvan!!!!
    
    

    font = pygame.font.Font(None, 22)
    textImg = font.render( "   Register player (type and pres enter)", 1, (255,0,0))
    display.blit( textImg, (200,150) )# za da e nai otgore
    
    pygame.display.update()
    
    #game processing ...
    player_name =ask(display,'name')#vyvejdaneto
    print(player_name + ' was entered.')
    successful = game.register_player(player_name)
    print(player_name + ' was entererd ' + str(successful))
    
    
      

#register_player(game)
#----------------=== end register player =======-----------

# --------==== mourtage house =======----------

def trade(game,player_name): #ne raboti za procesi ..!!!
    pygame.init()
    window = pygame.display.set_mode((400, 200), 0, 32)
    
    pygame.display.set_caption('Trading')
    background = pygame.image.load('pictures/bG.jpg')
    window.blit(background,(0, 0))

    font = pygame.font.Font(None, 30)
    textImg = font.render( "   Trading between two people ", 1, (255,0,0))
    window.blit( textImg, (0,0) )# za da e nai otgore

    pygame.display.update()
    pygame.font.quit()
    #smenqt se posledovatelno :)
    other_player = ask(window,'other player name')
    #if other_player not a player: return

    current_offer_buildings = ask(window,'current player buildings')#vyvejdaneto
    current_offer_money = int(ask(window,'current player money offer'))#vyvejdaneto
    other_offer_buildings = ask(window,'other player buildings')#vyvejdaneto
    other_offer_money = int(ask(window,'other player money'))#vyvejdaneto
    current_offer_buildings = [int(i) for  i in current_offer_buildings.split()]
    other_offer_buildings = [int(i) for  i in other_offer_buildings.split()]


    #print(other_player)
    #print(current_offer_buildings,current_offer_money)
    #print(other_offer_buildings,other_offer_money)
    

    
    game.trade_buildings(player_name,current_offer_buildings,other_player,other_offer_buildings)
    game.trade_money(player_name, other_player, current_offer_money, other_offer_money)
    pygame.quit()

#trade(1,1)
#---------------=== end trade ===-------------
def trader(game,player_name,window): #raboti
    #pygame.init()
    #window = pygame.display.set_mode((400, 200), 0, 32)
    
    #pygame.display.set_caption('Trading')
    #background = pygame.image.load('pictures/bG.jpg')
    #window.blit(background,(200, 200))

    font = pygame.font.Font(None, 30)
    textImg = font.render( "   Trading between two people ", 1, (255,0,0))
    window.blit( textImg, (0,0) )# za da e nai otgore

    pygame.display.update()
    
    #smenqt se posledovatelno :)
    other_player = ask(window,'other player name')
    #if other_player not a player: return

    current_offer_buildings = ask(window,'current player buildings')#vyvejdaneto
    current_offer_money = int(ask(window,'current player money offer'))#vyvejdaneto
    other_offer_buildings = ask(window,'other player buildings')#vyvejdaneto
    other_offer_money = int(ask(window,'other player money'))#vyvejdaneto
    current_offer_buildings = [int(i) for  i in current_offer_buildings.split()]
    other_offer_buildings = [int(i) for  i in other_offer_buildings.split()]


    #print(other_player)
    #print(current_offer_buildings,current_offer_money)
    #print(other_offer_buildings,other_offer_money)
    

    
    game.trade_buildings(player_name,current_offer_buildings,other_player,other_offer_buildings)
    game.trade_money(player_name, other_player, current_offer_money, other_offer_money)
    #pygame.quit()

#trade(game)



    
#------------- ==== mourtage ==== ----------
def mourtage(game, player_name): #testvana ne raboti za procesi
    pygame.init()
    window = pygame.display.set_mode((400, 200), 0, 32)
    print(game.PLAYER_NAMEORDER)
    pygame.display.set_caption('Mourtage')
    background = pygame.image.load('pictures/bG.jpg')
    window.blit(background,(0, 0))

    font = pygame.font.Font(None, 30)
    textImg = font.render( "  Mourtage write just one building", 1, (255,0,0))
    window.blit( textImg, (0,0) )# za da e nai otgore   
    pygame.display.update()
    pygame.font.quit()
    building_number = ask(window,'Number of a building')#vyvejdaneto    
    print(game.mourtage(player_name,int(building_number)))
    #mourtage animation
    pygame.quit()

#mourtage(game,'goshkoto')

#----------------=== end register player =======-----------
#------------- ==== mourtage ==== ----------
def mourtager(game, player_name, window,icon): #testvana da sloja animaciq za poziciq
    
    
    print(game.PLAYER_NAMEORDER)
    
    background = pygame.image.load('pictures/bG.jpg')
    window.blit(background,(120, 120))

    font = pygame.font.Font(None, 30)
    textImg = font.render( "  Mourtage write just one building", 1, (255,0,0))
    window.blit( textImg, (0,0) )# za da e nai otgore   
    pygame.display.update()
    
    building_number = ask(window,'Number of a building')#vyvejdaneto    
    print(game.mourtage(player_name,int(building_number)))
    #mourtage animation
    

#mourtage(game,'goshkoto')






#------------- ==== unmourtage ==== ----------
def unmourtage(game, player_name):  #testvana ne raboti za procesi
    pygame.init()
    window = pygame.display.set_mode((400, 200), 0, 32)
    
    pygame.display.set_caption('Unmourtage')
    background = pygame.image.load('pictures/bG.jpg')
    window.blit(background,(0, 0))

    font = pygame.font.Font(None, 30)
    textImg = font.render( "  unmourtage write just one building", 1, (255,0,0))
    window.blit( textImg, (0,0) )# za da e nai otgore

    pygame.display.update()
    pygame.font.quit()

    building_number = ask(window,'Number of a building')#vyvejdaneto
    print(game.unmourtage(player_name,int(building_number)))
    #unmortage animation
    pygame.quit()

#unmourtage(game)
#----------------=== end unmourtage =======-----------

#------------- ==== unmourtage ==== ----------
def unmourtager(game, player_name,window,icon):  #testvana da sloja animaciq za poziciq
   
    background = pygame.image.load('pictures/bG.jpg')
    window.blit(background,(120, 120))

    font = pygame.font.Font(None, 30)
    textImg = font.render( "  unmourtage write just one building", 1, (255,0,0))
    window.blit( textImg, (0,0) )# za da e nai otgore

    pygame.display.update()
    

    building_number = ask(window,'Number of a building')#vyvejdaneto
    print(game.unmourtage(player_name,int(building_number)))
    #unmortage animation
    

#unmourtage(game)
#----------------=== end unmourtage =======-----------

    
#------------- ==== build_house ==== ----------
def build_house(game,player_name):   #testvana ne raboti za procesi
    pygame.init()
    window = pygame.display.set_mode((400, 200), 0, 32)
    
    pygame.display.set_caption('Build')
    background = pygame.image.load('pictures/bG.jpg')
    window.blit(background,(0, 0))

    font = pygame.font.Font(None, 30)
    textImg = font.render( " Build one house", 1, (255,0,0))
    window.blit( textImg, (0,0) )# za da e nai otgore

    pygame.display.update()
    pygame.font.quit()

    building_number = ask(window,'Number of a building')#vyvejdaneto
    game.build_house(player_name,int(building_number))
    print(1)
    pygame.quit()

#build_house(game)
#----------------=== end build_house =======-----------


#------------- ==== build_house ==== ----------
def build_houser(game,player_name,window,icon):   #testvana da dobavq animaciq
   
    background = pygame.image.load('pictures/bG.jpg')
    window.blit(background,(0, 0))

    font = pygame.font.Font(None, 30)
    textImg = font.render( " Build one house", 1, (255,0,0))
    window.blit( textImg, (0,0) )# za da e nai otgore

    pygame.display.update()
    

    building_number = ask(window,'Number of a building')#vyvejdaneto
    game.build_house(player_name,int(building_number))
    print(1)
    

#build_house(game)
#----------------=== end build_house =======-----------









#------------- ==== sell_house ==== ----------
def sell_house(game,player_name):   #testvana ne raboti za procesi
    pygame.init()
    window = pygame.display.set_mode((400, 200), 0, 32)
    
    pygame.display.set_caption('Sell')
    background = pygame.image.load('pictures/bG.jpg')
    window.blit(background,(0, 0))

    font = pygame.font.Font(None, 30)
    textImg = font.render( " Sell one house", 1, (255,0,0))
    window.blit( textImg, (0,0) )# za da e nai otgore

    pygame.display.update()
    pygame.font.quit()

    building_number = ask(window,'Number of a building')#vyvejdaneto
    game.sell_house(player_name,int(building_number))
    print(building_number)
    pygame.quit()

#sell_house(game)
#----------------=== endsell_house =======-----------

#------------- ==== sell_house ==== ----------
def sell_houser(game,player_name,window,icon):   #testvana uj
    
    background = pygame.image.load('pictures/bG.jpg')
    window.blit(background,(0, 0))

    font = pygame.font.Font(None, 30)
    textImg = font.render( " Sell one house", 1, (255,0,0))
    window.blit( textImg, (200,200) )# za da e nai otgore

    pygame.display.update()

    building_number = ask(window,'Number of a building')#vyvejdaneto
    game.sell_house(player_name,int(building_number))
    print(building_number)
     

#sell_house(game)
#----------------=== endsell_house =======-----------






    

#----- buy --- ==

def Buy(game, building_number, player_name):
    pygame.init()    
    catImg1 = pygame.image.load('pictures/bG.jpg')   
    #FPS = 15
    #picx = go_player_picturex
    #picy = go_player_picturey    
    pp = pygame.display.set_mode((400, 200), 0, 32)
    
    font = pygame.font.Font(None, 30)
    a = 'gosho' + str(building_number)
    textImg = font.render( "   Buy building ", 1, (255,0,0))
    textImg1 = font.render( "   building name is " + a, 1, (255,0,0))
    
    
    pygame.display.set_caption('Buy')
    catImg1 = pygame.image.load('pictures/bG.jpg')
    
    
    pp.blit(catImg1,(0, 0))
    
 
    
    # buttons on the screen
    bg_color = (255, 255, 255)
    text_color = (255,   0,   0)    
    x_position = 0
    y_position = 0
    text_lenght = 150
    x_text_border = 30
    y_text_border =40
    
    bg_color = (255, 255, 255)
    text_color = (255,   0,   0)
    
    x_position = 40
    y_position = 100
    text_lenght = 150
    x_text_border = 30
    y_text_border =40   
    
    
    Buy = Button()
    Buy.create_button(pp,bg_color, x_position ,120,
                        text_lenght,x_text_border,y_text_border,'Buy',text_color)
    Auction= Button()
    Auction.create_button(pp,bg_color, x_position +200,120,
                           text_lenght,x_text_border,y_text_border,'Auction',text_color)
    pp.blit( textImg, (0,0) )# za da e nai otgore
    pp.blit( textImg1, (10,50) )# za da e nai otgore
    pygame.display.update()
    
    pygame.font.quit()
    mousex = 0
    mousey= 0
    
    time.sleep(2)
    for event in pygame.event.get(): # event handling loop
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            if Buy.pressed([mousex,mousey]):
                print('d')
                game.buy_building(self,player_name,building_index) 
            
            if Auction.pressed([mousex,mousey]):
                print('d4')
                Auction(game, building_number)
    pygame.quit()


#Buy(game,2)
#======--------------- end buy ------------=============
    
#======--------------- auction ------------=============


def auction(game, building_number):
    pygame.init()
    
    catImg1 = pygame.image.load('pictures/bG.jpg')
    
    
    FPS = 15
    picx = go_player_picturex
    picy = go_player_picturey    
    pp = pygame.display.set_mode((400, 200), 0, 32)
    
    font = pygame.font.Font(None, 30)
    a = 'gosho'
    textImg = font.render( "   auction building ", 1, (255,0,0))
    textImg1 = font.render( "   building name is " + a+ 'price is '+a, 1, (255,0,0))
    
    
    pygame.display.set_caption('Buy')
    catImg1 = pygame.image.load('pictures/bG.jpg')
    
    
    pp.blit(catImg1,(0, 0))
    
 
    
    # buttons on the screen 

    bg_color = (255, 255, 255)
    text_color = (255,   0,   0)
    #windowBgColor = WHITE
    x_position = 0
    y_position = 0
    text_lenght = 150
    x_text_border = 30
    y_text_border =40
    
    bg_color = (255, 255, 255)
    text_color = (255,   0,   0)
    #windowBgColor = WHITE
    x_position = 40
    y_position = 100
    text_lenght = 150
    x_text_border = 30
    y_text_border =40   
    #y_position =(i for i in range(1,500) if i % 40 == 0)
    
    rules = Button()
    rules.create_button(pp,bg_color, x_position ,120,
                        text_lenght,x_text_border,y_text_border,'bid 1',text_color)
    register= Button()
    register.create_button(pp,bg_color, x_position +170,120,
                           text_lenght,x_text_border,y_text_border,'bid 50',text_color)
    register= Button()
    register.create_button(pp,bg_color, x_position +100,160,
                           text_lenght,x_text_border,y_text_border,'fold',text_color)
    pp.blit( textImg, (0,0) )# za da e nai otgore
    pp.blit( textImg1, (10,50) )# za da e nai otgore
    pygame.display.update()
    
    pygame.font.quit()
    mousex = 0
    mousey= 0
    #kom = ask(pp,'name')
    time.sleep(2)
    for event in pygame.event.get(): # event handling loop
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            if rules.pressed([mousex,mousey]):
                print('d')
            
            if register.pressed([mousex,mousey]):
                print('d4')
    pygame.quit()


#auction(game,2)

#======--------------- end auction ------------=============

#----- buy --- ==

def Buyer(game, building_number, player_name,pp, icon_player):
   
      
    
    
    font = pygame.font.Font(None, 30)
    a = 'gosho' + str(building_number)
    textImg = font.render( "   Buy building ", 1, (255,0,0))
    textImg1 = font.render( "   building name is " + a, 1, (255,0,0))
    
    
    pygame.display.set_caption('Buy')
    catImg1 = pygame.image.load('pictures/bG.jpg')
    
    
    pp.blit(catImg1,(0, 0))
    
 
    
    # buttons on the screen
    bg_color = (255, 255, 255)
    text_color = (255,   0,   0)    
    x_position = 0
    y_position = 0
    text_lenght = 150
    x_text_border = 30
    y_text_border =40
    
    bg_color = (255, 255, 255)
    text_color = (255,   0,   0)
    
    x_position = 40
    y_position = 100
    text_lenght = 150
    x_text_border = 30
    y_text_border =40   
    
    
    Buy = Button()
    Buy.create_button(pp,bg_color, x_position ,120,
                        text_lenght,x_text_border,y_text_border,'Buy',text_color)
    Auction= Button()
    Auction.create_button(pp,bg_color, x_position +200,120,
                           text_lenght,x_text_border,y_text_border,'Auction',text_color)
    pp.blit( textImg, (0,0) )# za da e nai otgore
    pp.blit( textImg1, (10,50) )# za da e nai otgore
    pygame.display.update()
    
    pygame.font.quit()
    mousex = 0
    mousey= 0
    
    time.sleep(2)
    for event in pygame.event.get(): # event handling loop
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            if Buy.pressed([mousex,mousey]):
                print('d')
                game.buy_building(player_name,building_index) 
            
            if Auction.pressed([mousex,mousey]):
                print('d4')
                Auction(game, building_number)
    


#Buy(game,2)
#======--------------- end buy ------------=============
    # def auctioner(game, building_number,pp,icon): da go prepravq na go to jail !!!
#======--------------- auction ------------=============


def auctioner(game, building_number,pp,icon):
    
    
    font = pygame.font.Font(None, 30)
    a = 'gosho'
    textImg = font.render( "   auction building ", 1, (255,0,0))
    textImg1 = font.render( "   building name is " + a+ 'price is '+a, 1, (255,0,0))
    
    
    pygame.display.set_caption('Buy')
    catImg1 = pygame.image.load('pictures/bG.jpg')
    
    
    pp.blit(catImg1,(0, 0))
    
 
    
    # buttons on the screen 

    bg_color = (255, 255, 255)
    text_color = (255,   0,   0)
    #windowBgColor = WHITE
    x_position = 0
    y_position = 0
    text_lenght = 150
    x_text_border = 30
    y_text_border =40
    
    bg_color = (255, 255, 255)
    text_color = (255,   0,   0)
    #windowBgColor = WHITE
    x_position = 40
    y_position = 100
    text_lenght = 150
    x_text_border = 30
    y_text_border =40   
    #y_position =(i for i in range(1,500) if i % 40 == 0)
    
    rules = Button()
    rules.create_button(pp,bg_color, x_position ,120,
                        text_lenght,x_text_border,y_text_border,'bid 1',text_color)
    register= Button()
    register.create_button(pp,bg_color, x_position +170,120,
                           text_lenght,x_text_border,y_text_border,'bid 50',text_color)
    register= Button()
    register.create_button(pp,bg_color, x_position +100,160,
                           text_lenght,x_text_border,y_text_border,'fold',text_color)
    pp.blit( textImg, (0,0) )# za da e nai otgore
    pp.blit( textImg1, (10,50) )# za da e nai otgore
    pygame.display.update()
    
    pygame.font.quit()
    mousex = 0
    mousey= 0
    #kom = ask(pp,'name')
    time.sleep(2)
    for event in pygame.event.get(): # event handling loop
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            if rules.pressed([mousex,mousey]):
                print('d')
            
            if register.pressed([mousex,mousey]):
                print('d4')
    pygame.quit()


#auction(game,2)

#======--------------- end auction ------------=============






"""
def d(a):
    pygame.init()
    a.append(1)
    

    #text
    
    catImg1 = pygame.image.load('pictures/bG.jpg')
    
    print(5)
    FPS = 15
    picx = go_player_picturex
    picy = go_player_picturey
       
    
    #pygame.init()
    
    pp = pygame.display.set_mode((400, 200), 0, 32)
    
    font = pygame.font.Font(None, 30)
    textImg = font.render( "   Register player (type and pres enter)", 1, (255,0,0))
    
    #windowSurface = pygame.display.set_mode((500, 400),0,32)
    pygame.display.set_caption('ACTION')
    catImg1 = pygame.image.load('pictures/bG.jpg')
    #catImg = pygame.image.load('pictures/dog.gif')
    #end of main pictures
    pp.blit(catImg1,(0, 0))
    #pp.blit(catImg, (picx,picy))
    
    # buttons on the screen 

    bg_color = (255, 255, 255)
    text_color = (255,   0,   0)
    #windowBgColor = WHITE
    x_position = 0
    y_position = 0
    text_lenght = 150
    x_text_border = 30
    y_text_border =40
    
    bg_color = (255, 255, 255)
    text_color = (255,   0,   0)
    #windowBgColor = WHITE
    x_position = 40
    y_position = 100
    text_lenght = 150
    x_text_border = 30
    y_text_border =40   
    y_position =(i for i in range(1,500) if i % 40 == 0)
    
    rules = Button()
    rules.create_button(pp,bg_color, x_position ,next(y_position),text_lenght,x_text_border,y_text_border,'Buy',text_color)
    register= Button()
    register.create_button(pp,bg_color, x_position ,next(y_position),text_lenght,x_text_border,y_text_border,'Auction',text_color)
    pp.blit( textImg, (0,0) )# za da e nai otgore
    pygame.display.update()
    time.sleep(2)
    pygame.font.quit()
    mousex = 0
    mousey= 0
    kom = ask(pp,'name')
    for event in pygame.event.get(): # event handling loop
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            if rules.pressed([mousex,mousey]):
                print('d')
            
            if register.pressed([mousex,mousey]):
                print('d4')
    pygame.quit()

#--------- original
def d(a):
    pygame.init()
    a.append(1)
    

    #text
    
    catImg1 = pygame.image.load('pictures/bG.jpg')
    
    print(5)
    FPS = 15
    picx = go_player_picturex
    picy = go_player_picturey
       
    
    #pygame.init()
    
    pp = pygame.display.set_mode((400, 200), 0, 32)
    
    font = pygame.font.Font(None, 30)
    textImg = font.render( "   Register player (type and pres enter)", 1, (255,0,0))
    
    #windowSurface = pygame.display.set_mode((500, 400),0,32)
    pygame.display.set_caption('ACTION')
    catImg1 = pygame.image.load('pictures/bG.jpg')
    #catImg = pygame.image.load('pictures/dog.gif')
    #end of main pictures
    pp.blit(catImg1,(0, 0))
    #pp.blit(catImg, (picx,picy))
    
    # buttons on the screen 

    bg_color = (255, 255, 255)
    text_color = (255,   0,   0)
    #windowBgColor = WHITE
    x_position = 0
    y_position = 0
    text_lenght = 150
    x_text_border = 30
    y_text_border =40
    
    bg_color = (255, 255, 255)
    text_color = (255,   0,   0)
    #windowBgColor = WHITE
    x_position = 40
    y_position = 100
    text_lenght = 150
    x_text_border = 30
    y_text_border =40   
    y_position =(i for i in range(1,500) if i % 40 == 0)
    
    rules = Button()
    rules.create_button(pp,bg_color, x_position ,next(y_position),text_lenght,x_text_border,y_text_border,'Buy',text_color)
    register= Button()
    register.create_button(pp,bg_color, x_position ,next(y_position),text_lenght,x_text_border,y_text_border,'Auction',text_color)
    pp.blit( textImg, (0,0) )# za da e nai otgore
    pygame.display.update()
    time.sleep(2)
    pygame.font.quit()
    mousex = 0
    mousey= 0
    kom = ask(pp,'name')
    for event in pygame.event.get(): # event handling loop
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            if rules.pressed([mousex,mousey]):
                print('d')
            
            if register.pressed([mousex,mousey]):
                print('d4')
    pygame.quit()

"""



























#text oprosten
"""

pygame.init()
window = pygame.display.set_mode( (424,440) )#suzdava prozorec
pygame.display.set_caption( 'Example Game' )#zaglavie
font = pygame.font.Font(None, 30)
textImg = font.render( "Press SPACE BAR to start", 1, (255,0,0))
window.blit( textImg, (0,0) )

pygame.display.update()

"""


"""
pygame.init()
window = pygame.display.set_mode( (424,440) )
pygame.display.set_caption( 'Example Game' )
background = pygame.Surface( window.get_size() )
background.fill( (0,0,0) )
font = pygame.font.Font(None, 30)
textImg = font.render( "Press SPACE BAR to start", 1, (255,0,0))
background.blit( textImg, (0,0) )
window.blit( background, (0,0) )
pygame.display.flip()
backSprites = pygame.sprite.RenderUpdates()
frontSprites = pygame.sprite.RenderUpdates()
time.sleep(2)  
pygame.quit()"""
