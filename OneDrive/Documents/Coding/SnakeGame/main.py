import pygame

pygame.init()

WIDTH=int(800)
HEIGHT=int(600)
head_x=WIDTH//2
head_y=HEIGHT//2
snake_size=20


screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Snake")

gameloop=True
snake_position=(head_x,head_y,snake_size,snake_size)
pygame.draw.rect(screen, "green", snake_position)

while gameloop:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameloop=False
    screen.fill("black")
    snake_position=(head_x,head_y,snake_size,snake_size)
    pygame.draw.rect(screen, "green", snake_position)
    head_x+=1
    
    
    
    pygame.display.flip()
pygame.quit()


