import pygame, sys
from pygame.locals import *
import threading
from multiprocessing import Process, Value
import time
import pygame, pygame.font, pygame.event, pygame.draw, string

from game import Game
from gui_functions import *

def f():
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
#processes = Process(target=f, )
"""
"""
players_move_icons = {}
players_buy_icons = {}
players_mortage_icons = {} 


players_buy_icons[1]= pygame.image.load( 'players_icons/car - own.gif')
players_mortage_icons[1]= pygame.image.load('players_icons/car - mortage.gif')
players_move_icons[1]= pygame.image.load('players_icons/car.gif')

players_buy_icons[2]=pygame.image.load('players_icons/dog - own.gif')
players_mortage_icons[2]=pygame.image.load('players_icons/dog - mortage.gif')
players_move_icons[2]=pygame.image.load('players_icons/dog.gif')

players_buy_icons[3]=pygame.image.load('players_icons/ship - own.gif')
players_mortage_icons[3]=pygame.image.load('players_icons/ship - mortage.gif')
players_move_icons[3]=pygame.image.load('players_icons/ship.gif')

players_buy_icons[4]=pygame.image.load('players_icons/hat - own.gif')
players_mortage_icons[4]=pygame.image.load('players_icons/hat - mortage.gif')
players_move_icons[4]=pygame.image.load('players_icons/hat.gif')

from buttons import *

FPS = 15 # frames per second setting
go_player_picturex = 497
go_player_picturey = 501

WHITE = (255, 255, 255)
start_trip = 500
end_trip = 50
step_trip = 46
magic_trip = 20 #bez popravkata ne e krasivo :)

from multiprocessing import Process, Value







# monopoly picture with players
def main():
    game = Game()
    game.register_player('goshko')
    game.register_player('kirakis')
    FPS = 15
    picx = go_player_picturex
    picy = go_player_picturey
    global DISPLAYSURF, fpsClock
    pygame.init()
    fpsClock = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((760, 580), 0, 32)
    #windowSurface = pygame.display.set_mode((500, 400),0,32)
    pygame.display.set_caption('Hello ddddddddd world!')
    background = pygame.image.load('pictures/resized.bmp')
    moving_dog = pygame.image.load('pictures/dog.gif')
    #end of main pictures
    DISPLAYSURF.blit(background,(0, 0))
    #DISPLAYSURF.blit(catImg, (picx,picy))
    
       
    #end of buttons
    #move_icon(0, 10,players_buy_icons[1],DISPLAYSURF)
    #move_icon(0, 10,players_buy_icons[2],DISPLAYSURF)
    #buy_or_mortage_property(players_buy_icons[1], 3,DISPLAYSURF)
    #build_or_sell_house(players_buy_icons[1],3 ,DISPLAYSURF)
    pygame.display.update()
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
    #move_icon(0, 30,0,DISPLAYSURF)
    #move_icon(0,5,0,DISPLAYSURF)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos

                if roll_button.pressed([mousex,mousey]):
                    print('rolled pressed')    
                    if not game.player_Free() :
                        a = jail()
                        if a == 'free':
                            game.jail_decision(50)
                        else: 
                            break
                    

                    #svoboden
                    roll = roll_dices(game,DISPLAYSURF) #hvyrlq zarove
                    if len(roll)<2: 
                        display_centre(DISPLAYSURF)
                        break
                    move_icon(roll[0], roll[1],game.current_player_index(),DISPLAYSURF)#mesti igracha
                    fee_result = game.take_fee()
                    display_centre(DISPLAYSURF)
                    if fee_result == 'buy':
                        result = Buyer(game,roll[1],DISPLAYSURF)
                        display_centre(DISPLAYSURF)
                        if result =='buy':
                            picx,picy = move_icon(roll[0], roll[1],game.current_player_index(),DISPLAYSURF)
                            buy_or_mortage_property(game.current_player_index(), roll[1],DISPLAYSURF,picx,picy)
                    else: 
                        auctioner()
                        display_centre(DISPLAYSURF)
                        
                    print('render')
                    players_render(DISPLAYSURF,game)
                    f()
                
                if end_turn.pressed([mousex,mousey]):
                    game.end_turn()
                    players_render(DISPLAYSURF,game)
                    print('end_turn pressed')
                
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
                    
                    display_centre(DISPLAYSURF)
                    
                if register.pressed([mousex,mousey]):#works but buggy
                    print('register pressed',register.stat)
                    register_player(game,DISPLAYSURF)
                    pygame.display.update()    
                    display_centre(DISPLAYSURF)                                            
                    print(game.all_player())

                    #da dobavq centralna kartinka 
                    
                if bancrupt.pressed([mousex,mousey]):#works but buggy
                    print('bancrupt pressed',register.stat)
                    #self.other(DISPLAYSURF,game)
                    #display_centre(DISPLAYSURF)
                    #register_player()
                    #register.status(False)
                pygame.display.update()    
                mouseClicked = True
    
        

        pygame.display.update()
        
        
       
        
        
main()










        #pionkax = 30
        #pionkay = 20
        #player_name = 'goshko'
        #player_budget = 400
         # player name coord (20,558) and budget(400,558)
        #display_current_player(DISPLAYSURF,'goshko',500,(20,558),(400,558))
        #blank_names(DISPLAYSURF, 1,(0,558))
        #display_current_player(DISPLAYSURF,'gosaddsashko',5200,(20,558),(400,558))








#--------- ne znam za kakvo si

