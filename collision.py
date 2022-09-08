# Conllision Pygame library

'''
# collision between two square objects
collision.rectCollision(rect1, rect2)

# collision between two circular objects
collision.circleCollision(center1, radius1, center2, radius2)

# collision between any two objects
collision.objCollision(surf1, pos1, surf2, pos2)
'''

import pygame, math

### Rectangle ###

# x1 = x
# y1 = y
# x2 = x + width
# y2 = y + height

# x1 of rect1 is smaller x2 of rect2
# x1 of rect2 is smaller x2 of rect1
# y1 of rect1 is smaller y2 of rect2
# y1 of rect2 is smaller y2 of rect1

# rect = [x, y, width, height]
def rectCollision(rect1, rect2):
    if rect1[0] <= rect2[0] + rect2[2] \
        and rect2[0] <= rect1[0] + rect1[2] \
        and rect1[1] <= rect2[1] + rect2[3] \
        and rect2[1] <= rect1[1] + rect1[3]:
        return True
    return False

### Circle ###

# distance between two centers is less than the sum of the two radii

# center = [x, y]
# radius = r
def circleCollision(center1, radius1, center2, radius2):
    delta = math.sqrt((center1[0]-center2[0])**2 + (center1[1]-center2[1])**2) # Khoảng cách hai tâm
    if delta <= radius1 + radius2:
        return True
    return False

### OBJECT ###

# Va chạm giữa hai hình bất kì
# kiểm tra vị trí của obj1 có tỉ lệ với obj2 không

# surf = surface
# pos = [x, y]
def objCollision(surf1, pos1, surf2, pos2):
    mask1 = pygame.mask.from_surface(surf1)
    mask2 = pygame.mask.from_surface(surf2)
    x = int(pos2[0] - pos1[0])   # xác định vị trí x2 với x1
    y = int(pos2[1] - pos1[1])   # xác định vị trí y2 với y1
    if mask1.overlap(mask2, (x, y)) != None:    # nếu pixel obj2 thuộc obj1
        return True
    return False
