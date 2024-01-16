
def numTilings(n: int) -> int:
    domino_one, domino_two = 1, 2
    for i in range(n-1):
        temp = domino_one + domino_two
        domino_one = domino_two
        domino_two = temp
    
    if n > 2:
        tromino_one, tromino_two = 0, 2
    
    for i in range(n-2):
        temp = tromino_one + tromino_two
        tromino_one = tromino_two
        tromino_two = temp
        print(tromino_one, tromino_two)
    
    return tromino_two + domino_one
        


x = numTilings(4)
print(x)
    
