def climb_stairs(cost:list)-> int:
    one,two = cost[-1], cost[-2]
    l = len(cost) -3
    while l >= 0:
        
        temp = cost[l] + min(one, two)
        one = two
        two = temp
        l-=1
        print(one,two, cost[l])
    return min(one, two)


x = climb_stairs([1,100,1,1,1,100,1,1,100,1])


        
    
    