import math
asteroids = [-2, -1, 1, 2]

l = len(asteroids) - 1

while l > 0:
    
    if asteroids[l] < 0 and asteroids[l-1] > 0:
        
        if abs(asteroids[l]) > abs(asteroids[l-1]):
            asteroids.pop(l-1)
            l = len(asteroids) -1
        
        elif abs(asteroids[l]) < abs(asteroids[l-1]):
            asteroids.pop(l)
            l = len(asteroids) -1
        
        else:
            asteroids.pop(l)
            asteroids.pop(l-1)
            l = len(asteroids) -1
    else:
        l -= 1
    