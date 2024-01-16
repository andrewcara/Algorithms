def guess(num: int) -> int:
    
    number  = 1
    if number == num:
        return 0
    elif number < num:
        return -1
    else: 
        return 1
        
 
def guessNumber(n: int) -> int:

    #nums = [x for x in range(1, n+1)]
    l = 1
    high = n
    mid = ((high - l) // 2) + l
    while mid!=high and mid!=l:
        
        mid = ((high - l) // 2) + l

        output = guess(mid)
        
        if output == 0:
            return mid
        
        elif output < 0:
            high = mid -1
        
        else:
            l = mid +1
        
        print(l, mid, high)


x = guessNumber(1)
print(x)