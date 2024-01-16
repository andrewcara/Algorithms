def longestOnes(nums: list[int], k: int) -> int:
    r = 0
    last_one = []
    maximum_ones = 0
    l =0
    while r < len(nums):
        
        if nums[r] == 0:
            if k == 0:
                l+=1
            if len(last_one) == k:
                l = last_one.pop(0) +1
                last_one.append(r)
            else:
                last_one.append(r)
        r +=1
        
        maximum_ones = max(maximum_ones, len(nums[l:r]))
    
    return maximum_ones
        
            
        
        
        
x = longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)
print(x)