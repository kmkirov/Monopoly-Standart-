import time, sys
import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *

from game import Game
from buttons import *
from global_variables import  *


def display_centre(window, up_x=110 , up_y=110):
    center = pygame.image.load('pictures/centre.gif') #central place blank
    window.blit(center,(up_x,up_y))
    pygame.display.update()
    
background = pygame.image.load('pictures/blank.gif')   #player bottom blank 
def blank_names(display, black_image,coords):    
    display.blit(background,coords)
    pygame.display.update()
#--- ne pomnq za kakvo sa ....

center = (120,150)
blue_bg = (120, 120)
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
                   ((screen.get_width() / 2) - 200,
                    (screen.get_height() / 2) - 10,
                    200,20), 0)
  pygame.draw.rect(screen, (255,255,255),
                   ((screen.get_width() / 2) - 202,
                    (screen.get_height() / 2) - 12,
                    204,24), 1)
  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, (255,255,255)),
                ((screen.get_width() / 2) - 200, (screen.get_height() / 2) - 10))
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

#---roll
def roll_dices(game,display): #testvan!!!!
    rolled = game.roll_dice()
    background = pygame.image.load('pictures/bG.jpg')
    display.blit(background,blue_bg)
    font = pygame.font.Font(None, 30)
    textImg = font.render( "rolled "+ str(rolled[0]), 1, (255,0,0))
    display.blit( textImg, (200,150) )# za da e nai otgore
    pygame.display.update()
    
    #game processing ...
    
    print('current rolled' +  str(rolled[0]) + ' was diece '+str(rolled[1]))
  

#------------=== menu buttons

 # buttons on the screen 


#------------- register player just view rectangular version----------
def register_player(game,display): #testvan!!!!
    font = pygame.font.Font(None, 22)
    background = pygame.image.load('pictures/bG.jpg')
    display.blit(background,blue_bg)
    textImg = font.render( "   Register player (type and pres enter)", 1, (255,0,0))
    display.blit( textImg,center )# za da e nai otgore
    pygame.display.update()
    
    #game processing ...
    player_name =ask(display,'name')#vyvejdaneto
    print(player_name + ' was entered.')
    successful = game.register_player(player_name)
    print(player_name + ' was entererd ' + str(successful))
    

#---------------===  trade ===-------------
def trader(game,player_name,window): #raboti
    font = pygame.font.Font(None, 30)
    background = pygame.image.load('pictures/bG.jpg')
    window.blit(background,blue_bg)
    textImg = font.render( "   Trading between two people ", 1, (255,0,0))
    window.blit( textImg,  center)# za da e nai otgore

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
def mourtager(game, player_name, window): #testvana da sloja animaciq za poziciq
    print(game.PLAYER_NAMEORDER)
    
    background = pygame.image.load('pictures/bG.jpg')
    window.blit(background,blue_bg)

    font = pygame.font.Font(None, 26)
    textImg = font.render( "  Mourtage write just one building", 1, (255,0,0))
    window.blit( textImg, center )# za da e nai otgore   
    pygame.display.update()
    
    building_number = ask(window,'Number of a building')#vyvejdaneto    
    print(game.mourtage(player_name,int(building_number)))
    #mourtage animation
    

#------------- ==== unmourtage ==== ----------
def unmourtager(game, player_name,window):  #testvana da sloja animaciq za poziciq
   
    background = pygame.image.load('pictures/bG.jpg')
    window.blit(background,blue_bg)

    font = pygame.font.Font(None, 26)
    textImg = font.render( "  unmourtage write just one building", 1, (255,0,0))
    window.blit( textImg, center )# za da e nai otgore

    pygame.display.update()
    

    building_number = ask(window,'Number of a building')#vyvejdaneto
    print(game.unmourtage(player_name,int(building_number)))
    #unmortage animation



#------------- ==== build_house ==== ----------
def build_houser(game,player_name,window):   #testvana da dobavq animaciq
   
    background = pygame.image.load('pictures/bG.jpg')
    window.blit(background,blue_bg)

    font = pygame.font.Font(None, 30)
    textImg = font.render( " Build one house", 1, (255,0,0))
    window.blit( textImg, center )# za da e nai otgore

    pygame.display.update()
    

    building_number = ask(window,'Number of a building')#vyvejdaneto
    game.build_house(player_name,int(building_number))
    




#------------- ==== sell_house ==== ----------
def sell_houser(game,player_name,window):   #testvana uj
    
    background = pygame.image.load('pictures/bG.jpg')
    window.blit(background,blue_bg)

    font = pygame.font.Font(None, 30)
    textImg = font.render( " Sell one house", 1, (255,0,0))
    window.blit( textImg, center )# za da e nai otgore

    pygame.display.update()

    building_number = ask(window,'Number of a building')#vyvejdaneto
    game.sell_house(player_name,int(building_number))
    print(building_number)
     

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

def printa(): print ('aaaa')
class menus:
    def other(self,DISPLAYSURF,game):
        bg_color = (255, 255, 255)
        text_color = (255,   0,   0)
        #windowBgColor = WHITE
        x_position = 600
        y_position = 0
        text_lenght = 150
        x_text_border = 30
        y_text_border =40   

        roll_button = Button()
        roll_button.create_button(DISPLAYSURF,bg_color, x_position ,y_position,text_lenght,x_text_border,y_text_border,'other',text_color)
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                if roll_button.pressed([mousex,mousey]):
                    print('rolled pressed',roll_button.stat)
                    roll_dices(game,DISPLAYSURF)
                    pygame.time.wait(2000)
                    display_centre(DISPLAYSURF)#, up_x=76 , up_y=74)

    def menu(self,DISPLAYSURF,game,event):
        bg_color = (255, 255, 255)
        text_color = (255,   0,   0)
        #windowBgColor = WHITE
        x_position = 600
        y_position = 0
        text_lenght = 150
        x_text_border = 30
        y_text_border =40   

        roll_button = Button()
        roll_button.create_button(DISPLAYSURF,bg_color, x_position ,y_position,text_lenght,x_text_border,y_text_border,'Roll',text_color)
        #                       range(start, end)   step
        y_position =(i for i in range(10,550) if i % 45 == 0)
        
        end_turn = Button()
        end_turn.create_button(DISPLAYSURF,bg_color, x_position ,next(y_position),text_lenght,x_text_border,y_text_border,'end_turn',text_color)
        mourtage = Button()
        mourtage.create_button(DISPLAYSURF,bg_color, x_position ,next(y_position),text_lenght,x_text_border,y_text_border,'mourtage',text_color)
        unmourtage = Button()
        unmourtage.create_button(DISPLAYSURF,bg_color, x_position ,next(y_position),text_lenght,x_text_border,y_text_border,'unmourtage',text_color)
        trade = Button()
        trade.create_button(DISPLAYSURF,bg_color, x_position ,next(y_position),text_lenght,x_text_border,y_text_border,'trade',text_color)
        sell = Button()
        sell.create_button(DISPLAYSURF,bg_color, x_position ,next(y_position),text_lenght,x_text_border,y_text_border,'sell',text_color)
        build = Button()
        build.create_button(DISPLAYSURF,bg_color, x_position ,next(y_position),text_lenght,x_text_border,y_text_border,'build',text_color)
        rules = Button()
        rules.create_button(DISPLAYSURF,bg_color, x_position ,next(y_position),text_lenght,x_text_border,y_text_border,'rules',text_color)
        register= Button()
        register.create_button(DISPLAYSURF,bg_color, x_position ,next(y_position),text_lenght,x_text_border,y_text_border,'register',text_color)
        bancrupt= Button()
        bancrupt.create_button(DISPLAYSURF,bg_color, x_position ,next(y_position),text_lenght,x_text_border,y_text_border,'bancrupt',text_color)
        #pygame.image.save(pygame.display.get_surface(),'C:/Python33/pictures/resized.bmp')
        pygame.display.update()

        mousex = 0
        mousey= 0
        
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            if roll_button.pressed([mousex,mousey]):
                print('rolled pressed',roll_button.stat)
                roll_dices(game,DISPLAYSURF)
                pygame.time.wait(2000)
                display_centre(DISPLAYSURF)#, up_x=76 , up_y=74)
                
            if end_turn.pressed([mousex,mousey]):
                print('end_turn pressed',end_turn.stat)
            if mourtage.pressed([mousex,mousey]):
                print('mourtage pressed')
                mourtager(game, 'kirakis', DISPLAYSURF)
                display_centre(DISPLAYSURF)
            if unmourtage.pressed([mousex,mousey]):
                print('unmourtage pressed')
                unmourtager(game, 'az',DISPLAYSURF)
                display_centre(DISPLAYSURF)
            if trade.pressed([mousex,mousey]):
                print('trade pressed')
                trader(game,'kirakis',DISPLAYSURF)
                display_centre(DISPLAYSURF)
            if sell.pressed([mousex,mousey]):
                print('sell pressed')
                sell_houser(game,"player_name",DISPLAYSURF)
                display_centre(DISPLAYSURF)
            if build.pressed([mousex,mousey]):
                print('build pressed')
                build_houser(game,"player_name",DISPLAYSURF)
                display_centre(DISPLAYSURF)
                
            if rules.pressed([mousex,mousey]):
                print('rules pressed')
                Buyer(game, 2, 'a',DISPLAYSURF, 'f')
                display_centre(DISPLAYSURF)
                
            if register.pressed([mousex,mousey]):#works but buggy
                print('register pressed',register.stat)
                register_player(game,DISPLAYSURF)
                pygame.display.update()    
                display_centre(DISPLAYSURF)                                            
                print(game.get_all_players())
                #da dobavq centralna kartinka 
                
            if bancrupt.pressed([mousex,mousey]):#works but buggy
                print('bancrupt pressed',register.stat)
                self.other(DISPLAYSURF,game)
                #display_centre(DISPLAYSURF)
                #register_player()
                #register.status(False)
            pygame.display.update()    
            mouseClicked = True