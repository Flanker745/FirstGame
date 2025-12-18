import pygame 
from sys import exit  # exit from main lops or ports 

pygame.init()  # insilites the pygame

screen = pygame.display.set_mode((800,600)) #screen = pygame.display.set_mode((weidth,height))
pygame.display.set_caption("Bhaag bhai") # giving name or title to the game 
clock = pygame.time.Clock()  # this gives the clock obj to ctr fram rate

#test_surface = pygame.Surface((200,100)) # display upon the screen varibale
#est_surface.fill("red") # fil color in screen
 
sky_surface = pygame.image.load("graphics/sky_5.png").convert_alpha() # import image to display it
ground_surface = pygame.image.load("graphics/ground.png").convert_alpha()
# from chat gpt 
width = screen.get_width()
sky_surface = pygame.transform.scale(sky_surface, (width, 500))
ground_surface = pygame.transform.scale(ground_surface , (width,130))

# display text
text_font = pygame.font.Font( "font/Pixeltype.ttf", 50) # 2 argunments (font type , font size)
score_surf = text_font.render("Flanker" , False , (64,64,64)) # 3 argunments  (text , AA , color)
score_rect = score_surf.get_rect(center=(400,50))

# add snail

snail_surafce = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surafce.get_rect(midbottom = (0 , 470))

#add player
palyer_surf = pygame.image.load("graphics/Player/player_stand.png").convert_alpha()
player_rect = palyer_surf.get_rect(midbottom = (50,470))
player_gr = 0

 #mouse posiiton
mou_pos = (0,0)
while True:
    #update all element 
    #make all logic
    for event in pygame.event.get():  # record the keyboard inputs in event variable
        if event.type == pygame.QUIT: # if type is quit then do close the game 
            pygame.quit()
            exit() # exit to not get error because of pygame.display.update() by closing the while loop
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                #player_gr = -20 
                print("")
        if event.type == pygame.KEYUP:
            print("up")
        if event.type == pygame.MOUSEMOTION: # get mouse motion or not 
            mou_pos  = event.pos
            
    screen.blit(sky_surface , (0,0))  # blit help to block the screen variable and put new screen on that variable  it take 2 argunment new screena & location
    screen.blit(ground_surface , (0,470))
    pygame.draw.rect(screen,"#c0e8ec",score_rect)
    # pygame.draw.line(screen,"Black",(0,0),pygame.mouse.get_pos(),10)  # draw a line which follow the mouse 
    screen.blit(score_surf,score_rect)    
    
    #screen.blit(snail_surafce , (snail_x_pos,435))
    screen.blit(snail_surafce , snail_rect)
    if snail_rect.right == 0:
        snail_rect.left=800
    snail_rect.right -=4
    
    #PLayer
    player_gr +=1
    screen.blit(palyer_surf,player_rect)
    player_rect.right +=1
    player_rect.y = player_gr

    # keys  = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print("Jump")
    # if player_rect.colliderect(snail_rect):
    #     print("huaa huaa")
    # mouse_pos = pygame.mouse.get_pos() # to get the mouse position
    # if player_rect.collidepoint(mou_pos):
    #     print(pygame.mouse.get_pressed()) # to get the which mouse btn is pressed 

    pygame.display.update()  # update screen every time
    clock.tick(60) # this tells the while loop run 60 time per second 60 frame per sec 60fps