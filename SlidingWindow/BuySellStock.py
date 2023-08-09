
def maxProfit(prices: list[int]) -> int:
    l = 0
    r = l + 1
    if len(prices) < 2:
        return 0
    current_max = max(0, (prices[r]-prices[l]))
    
    while r < len(prices):
        
        if prices[r] > prices[l]:
            current_max = max(current_max, (prices[r]-prices[l]))
            r+=1
        else:
            l=r
            r+=1
    return current_max

