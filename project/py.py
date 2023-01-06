import pygame
import os

WIDTH,HEIGHT=900, 500
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("space game")

VEL=5
COLOR=(150,10,32)
BLACK=(0,0,0)
FPS=60
SIZE=(55,40)
BULLET=7
BORDER=pygame.Rect((WIDTH/2)-5,0,5,HEIGHT)
YELLOW_SPACESHIP_IMAGE=pygame.image.load(os.path.join('project/Assets','spaceship_yellow.png'))
YELLOW_SPACESHIP_IMAGE=pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,SIZE),90)

RED_SPACESHIP_IMAGE=pygame.image.load(os.path.join('project/Assets','spaceship_red.png'))
RED_SPACESHIP_IMAGE=pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,SIZE),-90)
def yellow_handle_movement(keys_pressed,yellow):
    if keys_pressed[pygame.K_a] and yellow.x-VEL>0:#left
        yellow.x-=VEL
    if keys_pressed[pygame.K_d] and yellow.x+VEL+yellow.width <BORDER.x:#right
        yellow.x+=VEL
    if keys_pressed[pygame.K_w ]and yellow.y-VEL>0:#up
        yellow.y-=VEL
    if keys_pressed[pygame.K_s] and yellow.y+VEL+yellow.height<HEIGHT:#down
        yellow.y+=VEL
def red_handle_movement(keys_pressed,red):
    if keys_pressed[pygame.K_LEFT] and red.x-VEL>BORDER.x+BORDER.width :#left
        red.x-=VEL
    if keys_pressed[pygame.K_RIGHT] and red.x+VEL+red.width <WIDTH:#right
        red.x+=VEL
    if keys_pressed[pygame.K_UP]and red.y-VEL>0:#up
        red.y-=VEL
    if keys_pressed[pygame.K_DOWN]and red.y+VEL+red.height<HEIGHT:#down
        red.y+=VEL
def draw_window(red,yellow):
    WIN.fill(COLOR)
    pygame.draw.rect(WIN,BLACK,BORDER)
    WIN.blit(YELLOW_SPACESHIP_IMAGE,(yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP_IMAGE,(red.x,red.y))
    pygame.display.update()
def main():
    red=pygame.Rect(700,300,SIZE[0],SIZE[1])
    yellow=pygame.Rect(100,300,SIZE[0],SIZE[1])
    bullets=[]
    clock=pygame.time.Clock()
    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        
        keys_pressed= pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed,yellow)
        red_handle_movement(keys_pressed,red)
        


        draw_window(red,yellow)
    pygame.quit()
if __name__=="__main__":
    main()