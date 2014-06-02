
#GUI FUNCTIONS

from  game  import *
from tkinter import *
main_game = Game()

def find_position_x_y(position):
    picx = go_player_picturex
    picy = go_player_picturey
    for a in range(position):
        if picx > end_trip and picy >start_trip:
            
            picx = picx - step_trip
            picy = picy 
            
            
        elif picx <end_trip and picy >end_trip:
              
            picx = picx 
            picy = picy - step_trip
            
        elif picx < start_trip - magic_trip and picy <end_trip:
            picx = picx + step_trip
            picy = picy
        else :
            picx = picx 
            picy = picy + step_trip
    return (picx,picy)


def move_icon(old_poss, new_pos,catImg1):   
    picx,picy = find_position_x_y(old_poss)
    mousex = 0
    mousey= 0
    fpsClock = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((760, 555), 0, 32)
    for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
    for a in range(new_pos):
        if picx > end_trip and picy >start_trip:
            
            picx = picx - step_trip
            picy = picy 
            
            
        elif picx <end_trip and picy >end_trip:
              
            picx = picx 
            picy = picy - step_trip
            
        elif picx < start_trip - magic_trip and picy <end_trip:
            picx = picx + step_trip
            picy = picy
        else :
            picx = picx 
            picy = picy + step_trip
            
        DISPLAYSURF.blit(catImg1,(0, 0))
        DISPLAYSURF.blit(catImg, (picx,picy))
        fpsClock.tick(FPS)
        pygame.display.update()
        #pygame.save(get_surface(),'C:/Python33/pictures/resized.bmp')
        fpsClock.tick(FPS)






"""    
def saver():
    pygame.image.save(DISPLAYSURF,'C:/Python33/pictures/resized.bmp')        








 za saver
for a in range(100):
            if picx > end_trip and picy >start_trip:
                
                picx = picx - step_trip
                picy = picy 
                
                
            elif picx <end_trip and picy >end_trip:
                  
                picx = picx 
                picy = picy - step_trip
                
            elif picx < start_trip - magic_trip and picy <end_trip:
                picx = picx + step_trip
                picy = picy
            else :
                picx = picx 
                picy = picy + step_trip
               
            DISPLAYSURF.blit(catImg1,(0, 0))
            DISPLAYSURF.blit(catImg, (picx,picy))
            
            
            fpsClock.tick(FPS)
            pygame.display.update()
            
            fpsClock.tick(FPS)

"""





















