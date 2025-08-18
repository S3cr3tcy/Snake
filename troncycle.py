import pygame
import random

pygame.init()

WIDTH=int(800)
HEIGHT=int(600)
head_x=WIDTH//2
head_y=HEIGHT//2
snake_size=20
snake_dx=4
snake_dy=0
SNAKE_SPEED=4
FPS=60
clock=pygame.time.Clock()
body_coords=[]

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tron Cycle")

gameloop=True
snake_position=(head_x,head_y,snake_size,snake_size)
pygame.draw.rect(screen, "blue", snake_position)

font2=pygame.font.SysFont('Arial', 100)

while gameloop:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameloop=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                snake_dy=-1*SNAKE_SPEED
                snake_dx=0
            elif event.key==pygame.K_DOWN:
                snake_dy=1*SNAKE_SPEED
                snake_dx=0
            elif event.key==pygame.K_RIGHT:
                snake_dx=1*SNAKE_SPEED
                snake_dy=0
            elif event.key==pygame.K_LEFT:
                snake_dx=-1*SNAKE_SPEED
                snake_dy=0
    screen.fill("black")
    snake_position=(head_x,head_y,snake_size,snake_size)
    snake=pygame.draw.rect(screen, "blue", snake_position)
    head_x+=snake_dx
    head_y+=snake_dy
    
    for i in body_coords:
        pygame.draw.rect(screen, "blue", i)
    
    if snake.right>WIDTH or snake.left<0 or snake.top<0 or snake.bottom>HEIGHT or snake_position in body_coords:
        gameover=font2.render("GAME OVER", True, "yellow")
        text2_surface=gameover.get_rect()
        text2_surface.center=(WIDTH/2,HEIGHT/2)
        screen.blit(gameover,text2_surface)
        pygame.display.flip()
        pygame.time.delay(2000)
        gameloop=False

    body_coords.insert(0,snake_position)

    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()