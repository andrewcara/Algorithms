import math
def minimumHours(k: int, piles: list[int]) -> int:
    hours = 0
    for i in piles:
        hours+= math.ceil(i/k)
    return hours

piles = [3,6,7,11]
h = 9
low = 1
hi = max(piles)
currentMin = hi


while low <= hi:
    mid = (hi+low)//2
    hours = minimumHours(mid, piles)
    if hours > h:
        low = mid +1
    elif hours<=h:
        currentMin = min(currentMin, mid)
        hi = mid -1

        
print(currentMin,mid)

