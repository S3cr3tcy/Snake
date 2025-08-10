import pygame

pygame.init()

WIDTH=int(800)
HEIGHT=int(600)
midas_x=WIDTH//2
midas_y=HEIGHT//2
midas_size=20
OBJ_SIZE=20
midas_dx=4
midas_dy=0
obj1_x=700
obj1_y=500
obj2_x=100
obj2_y=500
obj3_x=700
obj3_y=100
obj4_x=100
obj4_y=100
MIDAS_SPEED=4
FPS=60
clock=pygame.time.Clock()

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Midas")

gameloop=True
midas_position=(midas_x,midas_y,midas_size,midas_size)
pygame.draw.rect(screen, "gold", midas_position)

obj1_position=(obj1_x,obj1_y,OBJ_SIZE,OBJ_SIZE)
obj2_position=(obj2_x,obj2_y,OBJ_SIZE,OBJ_SIZE)
obj3_position=(obj3_x,obj3_y,OBJ_SIZE,OBJ_SIZE)
obj4_position=(obj4_x,obj4_y,OBJ_SIZE,OBJ_SIZE)

colour1="green"
colour2="blue"
colour3="red"
colour4="yellow"

while gameloop:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameloop=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                midas_dy=-1*MIDAS_SPEED
                midas_dx=0
            elif event.key==pygame.K_DOWN:
                midas_dy=1*MIDAS_SPEED
                midas_dx=0
            elif event.key==pygame.K_RIGHT:
                midas_dx=1*MIDAS_SPEED
                midas_dy=0
            elif event.key==pygame.K_LEFT:
                midas_dx=-1*MIDAS_SPEED
                midas_dy=0
    screen.fill("black")
    midas_position=(midas_x,midas_y,midas_size,midas_size)
    midas=pygame.draw.rect(screen, "gold", midas_position)
    midas_x+=midas_dx
    midas_y+=midas_dy

    obj1=pygame.draw.rect(screen, colour1, obj1_position)
    obj2=pygame.draw.rect(screen, colour2, obj2_position)
    obj3=pygame.draw.rect(screen, colour3, obj3_position)
    obj4=pygame.draw.rect(screen, colour4, obj4_position)

    if midas.colliderect(obj1) == True:
        colour1="gold"
    elif midas.colliderect(obj2) == True:
        colour2="gold"
    elif midas.colliderect(obj3) == True:
        colour3="gold"
    elif midas.colliderect(obj4) == True:
        colour4="gold"
    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()