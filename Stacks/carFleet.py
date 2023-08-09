def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    
    distance = [target - x for x in position]
    stack = []
    time = []
    stack = []
    for i in range(len(speed)):
        time.append((distance[i]/speed[i], distance[i]))
    
    
    time = sorted(time,key=lambda l:l[1], reverse=False)
    

    
    for i, j in enumerate(time):
        
        if stack and j[0] <= stack[-1]:
            continue
        else:
            stack.append(j[0])
    print(stack)
    return len(stack)

carFleet(target = 10, position = [0,4,2], speed = [2,1,3])