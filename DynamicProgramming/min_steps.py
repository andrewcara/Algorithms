#Using Recursion

def min_steps(steps:int):
    if steps == 1:
        return 1
    elif steps ==2:
        return 2
    else:
        return min_steps(steps-2) + min_steps(steps-1)
    
x = min_steps(5)
print(x)


#Using Dynamic Programming

def climb_stairs(n:int)-> int:
    one,two = 1, 1
    
    for i in range(n-1):
        temp = one
        one = one + two
        two = temp
    return one