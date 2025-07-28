import pygame

pygame.init()

WIDTH=int(800)
HEIGHT=int(600)
line_x=300
line_y=300
line_size=20


screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Initial")

gameloop=True
line_position=(line_x,line_y,line_size,line_size)
pygame.draw.rect(screen, "green", line_position)

for i in range(200):
    line_position=(line_x,line_y,line_size,line_size)
    pygame.draw.rect(screen, "green", line_position)
    line_y-=1
    pygame.display.flip()
    
for i in range(200):
    line_position=(line_x,line_y,line_size,line_size)
    pygame.draw.rect(screen, "green", line_position)
    line_y+=1
    line_x+=1
    pygame.display.flip()

for i in range(200):
    line_position=(line_x,line_y,line_size,line_size)
    pygame.draw.rect(screen, "green", line_position)
    line_y-=1
    pygame.display.flip()

while gameloop:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameloop=False
    

pygame.quit()