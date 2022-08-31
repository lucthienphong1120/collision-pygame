import pygame
import collision

pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Test Collision')

def rectPlay():
    # rect = [x, y, width, height]
    rect1 = [0, 0, 80, 50] # Hình chữ nhật di chuyển
    rect2 = [150, 150, 80, 50] # Hình chữ nhật đứng yên

    rect1[0], rect1[1] = pygame.mouse.get_pos() # Lấy vị trí của chuột

    pygame.draw.rect(DISPLAYSURF, (255, 255, 0), rect2)
    if collision.rectCollision(rect1, rect2):
        pygame.draw.rect(DISPLAYSURF, (255, 0, 0), rect1)
    else:
        pygame.draw.rect(DISPLAYSURF, (0, 255, 0), rect1)

def circlePlay():
    # center = [x, y]
    # radius = r
    center1 = [0, 0] # Tâm hình tròn di chuyển
    radius1 = 30 # Bán kính hình tròn di chuyển
    center2 = [200, 200] # Tâm hình tròn đứng yên
    radius2 = 30 # Bán kính hình tròn đứng yên

    center1[0], center1[1] = pygame.mouse.get_pos() # Lấy vị trí của chuột

    pygame.draw.circle(DISPLAYSURF, (255, 255, 0), center2, radius2)
    if collision.circleCollision(center1, radius1, center2, radius2):
        pygame.draw.circle(DISPLAYSURF, (255, 0, 0), center1, radius1)
    else:
        pygame.draw.circle(DISPLAYSURF, (0, 255, 0), center1, radius1)

def objPlay():
    # surf = surface
    # pos = [x, y]
    surf1 = pygame.image.load('./img/star1.png') # Sao di chuyển
    surf1 = pygame.transform.scale(surf1, (50, 50))
    pos1 = [0, 0] # Vị trí sao di chuyển
    surf2 = pygame.image.load('./img/star2.png') # Sao đứng yên
    surf2 = pygame.transform.scale(surf2, (50, 50))
    pos2 = [180, 180] # Vị trí sao đứng yên

    pos1 = pygame.mouse.get_pos() # Lấy vị trí của chuột

    DISPLAYSURF.blit(surf2, pos2)
    DISPLAYSURF.blit(surf1, pos1)
    if collision.objCollision(surf1, pos1, surf2, pos2):
        pygame.draw.rect(DISPLAYSURF, (255, 0, 0), (50, 350, 300, 40))

### MAIN ###

option = int(input('''
1. Rectangle - Rectangle
2. Circle - Circle
3. Object - Object
'''))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    DISPLAYSURF.fill((0, 0, 0))

    if option == 1:
        rectPlay()
    elif option == 2:
        circlePlay()
    elif option == 3:
        objPlay()

    pygame.display.update()
    fpsClock.tick(FPS)