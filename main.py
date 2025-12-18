import pygame 
from sys import exit  # exit from main lops or ports 
from random import randint
def display_score ():
    current_score = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = text_font.render(f"{current_score}" , False , (64,64,64)) # 3 argunments  (text , AA , color)
    score_rect = score_surf.get_rect(center=(400,50))
    # pygame.draw.line(screen,"Black",(0,0),pygame.mouse.get_pos(),10)  # draw a line which follow the mouse 
    screen.blit(score_surf,score_rect) 
    return current_score
def obstacles_movement(obstacles_list):
    if obstacles_list:
        for obstacles_rect in obstacles_list:
            obstacles_rect.x -=5
            if obstacles_rect.bottom == 470:
                screen.blit(snail_surafce,obstacles_rect)
            else:
                screen.blit(fly_surf,obstacles_rect)
        obstacles_list = [obstacles for obstacles in obstacles_list if obstacles.x > -100]
        return obstacles_list
    else:
        return []
def collision(player , obstacles):
    if obstacles:
        for obstacles_rect in obstacles:
            if player.colliderect(obstacles_rect): return False
    return True


pygame.init()  # insilites the pygame
screen = pygame.display.set_mode((800,600)) #screen = pygame.display.set_mode((weidth,height))
pygame.display.set_caption("Kuud bhai") # giving name or title to the game 
clock = pygame.time.Clock()  # this gives the clock obj to ctr fram rate
game_active = False
start_time = 0
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


#obstacles
snail_surafce = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
# snail_rect = snail_surafce.get_rect(midbottom = (0 , 470))

fly_surf = pygame.image.load("graphics/Fly/Fly1.png").convert_alpha()
#add player
palyer_surf = pygame.image.load("graphics/Player/player_stand.png").convert_alpha()
player_play_rect = palyer_surf.get_rect(midbottom = (100,470))
palyer_surf_2x = pygame.transform.rotozoom(palyer_surf,0,3)
player_stand_rect = palyer_surf_2x.get_rect(center=(400 , 250))
player_gr = 0

#restsrt screen
game_title = text_font.render("Kuud bhai" ,False,"#599D87" )
game_title_rect = game_title.get_rect(center=(400,50))

restart_text = text_font.render("Press space to run" ,False,"#599D87" )
restart_text_rect = restart_text.get_rect(center=(400,450))

final_score = 0

# Timer
obstacles_timer = pygame.USEREVENT +1
pygame.time.set_timer(obstacles_timer,1300)

obstacles_rect_list = []

while True:
    #update all element 
    #make all logic
    for event in pygame.event.get():  # record the keyboard inputs in event variable
        if event.type == pygame.QUIT: # if type is quit then do close the game 
            pygame.quit()
            exit() # exit to not get error because of pygame.display.update() by closing the while loop
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE and player_play_rect.bottom == 470:
                    player_gr = -25 
            # if event.type == pygame.KEYUP:
            #     print("up")
            # if event.type == pygame.MOUSEMOTION: # get mouse motion or not 
            #     mou_pos  = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN and player_play_rect.bottom == 470:
                player_gr = -25
            
            if event.type == obstacles_timer:
                if randint(0,2):
                    obstacles_rect_list.append(snail_surafce.get_rect(midbottom = (randint(900,1100) , 470)))
                else:
                    obstacles_rect_list.append(fly_surf.get_rect(midbottom = (randint(900,1100), 370)))
                    
        else:
            if event.type == pygame.KEYDOWN and event.key==pygame.K_SPACE :
                game_active = True
            
    if game_active:
        screen.blit(sky_surface , (0,0))  # blit help to block the screen variable and put new screen on that variable  it take 2 argunment new screena & location
        screen.blit(ground_surface , (0,470))
        final_score = display_score()  
        
        #screen.blit(snail_surafce , (snail_x_pos,435))
       
        # if snail_rect.right == 0:
        #     snail_rect.left=800
        # snail_rect.right -=4
        # screen.blit(snail_surafce , snail_rect)
        
        #PLayer
        player_gr +=1
        screen.blit(palyer_surf,player_play_rect)
        #player_play_rect.right +=1
        player_play_rect.y += player_gr
        if player_play_rect.bottom >=470 :
            player_play_rect.bottom = 470
        
        # keys  = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     print("Jump")
        # if player_play_rect.colliderect(snail_rect):
        #     print("huaa huaa")
        # mouse_pos = pygame.mouse.get_pos() # to get the mouse position
        # if player_play_rect.collidepoint(mou_pos):
        #     print(pygame.mouse.get_pressed()) # to get the which mouse btn is pressed 
        obstacles_rect_list = obstacles_movement(obstacles_rect_list)
        game_active = collision(player_play_rect , obstacles_rect_list)
        # if snail_rect.colliderect(player_play_rect):
        #     game_active= False
    else:
       
        screen.fill("#4A6782")
        start_time = int(pygame.time.get_ticks() / 1000)
        obstacles_rect_list.clear()
        player_play_rect.midbottom = (100,470)
        player_gr = 0
        screen.blit(game_title , game_title_rect)
        screen.blit(palyer_surf_2x,player_stand_rect)
        screen.blit(restart_text,restart_text_rect)
        final_score_text = text_font.render(f"{final_score}",False ,"#599D87")
        final_score_text_rect = final_score_text.get_rect(center=(400,500 ))
        screen.blit(final_score_text,final_score_text_rect)
    pygame.display.update()  # update screen every time
    clock.tick(60) # this tells the while loop run 60 time per second 60 frame per sec 60fps