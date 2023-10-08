import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800 , 400)) #display
pygame.display.set_caption("Name of the game") #title
clock = pygame.time.Clock() # create a clock object

surface_1 = pygame.Surface((100 , 200)) # makes a graohic object
surface_1.fill('Red')

#IMAGES

surface_2 = pygame.image.load("D:\\Wallpapers\\OIP.jfif").convert()

#TEXT

test_font = pygame.font.Font(None , 50)
text_surface = test_font.render("text" ,True , "Green")

#ANIMATIONS
test_animation = pygame.image.load("D:\\Wallpapers\\Web capture_20-5-2023_202937_th.bing.com.jpeg").convert_alpha()
animation_x = 600

#RECTANGLES

player_surface = pygame.image.load("D:\\Wallpapers\\OIP (2).jfif").convert_alpha()
player_rectangle = player_surface.get_rect(topleft = (80, 200))




while True: # draw all elememts here and update stuff
    for event in pygame.event.get(): # all the inputs the player gives
        if event.type == pygame.QUIT:
            pygame.quit() # opposite to init 
            exit()# can use break as well
    
    screen.blit(surface_1 , (200 , 100)) #puts the surface on the main surface
     #       ^surface to be put ^position where to be put
    

    screen.blit(surface_2 , (0,0))
    screen.blit(text_surface , ( 50 , 50))

    
    animation_x -= 4
    animation_x %= 800
    screen.blit(test_animation, (animation_x , 250))# put the image on another surface othterwise overlaped images will be there

    screen.blit(player_surface , player_rectangle)

    pygame.display.update() #updates the display we created
    clock.tick(60) # causes while loop to run 60 times per sec 
    
    
    
