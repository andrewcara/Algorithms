def climb_stairs(cost:list)-> int:
    one,two = cost[-1], cost[-2]
    maximum = one
    l = len(cost) -3
    while l >= 0:
        temp = cost[l] + max(one, maximum)
        maximum = max(one, maximum)
        one = two
        two = temp
        l-=1
    return max(one, two)


x = climb_stairs([9,5,2,4])
print(x)