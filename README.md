# Collision Pygame

Collision Pygame library

## How to use

```py
import collision
```

## Functions

```py
collision.rectCollision(rect1, rect2)
collision.circleCollision(center1, radius1, center2, radius2)
collision.objCollision(surf1, pos1, surf2, pos2)
```

## Principles

### Rectangle

```
# x1 = x
# y1 = y
# x2 = x + width
# y2 = y + height

# x1 of rect1 is smaller x2 of rect2
# x1 of rect2 is smaller x2 of rect1
# y1 of rect1 is smaller y2 of rect2
# y1 of rect2 is smaller y2 of rect1

# rect = [x, y, width, height]
```

### Circle

```
# distance between two centers is less than the sum of the two radii

# center = [x, y]
# radius = r
```

### OBJECT

```
# collision between any two shapes
# check if obj1's position corresponds to obj2

# surf = surface
# pos = [x, y]
```
