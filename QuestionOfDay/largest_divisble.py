def largestDivisibleSubset(nums: list[int]) -> list[int]:
    i = len(nums) - 1
    j = i - 1
    longest_set = []
    curr_longest_set = []
    
    nums = sorted(nums)
    
    while i > -1:
        curr_val = nums[i]
        curr_longest_set.append(curr_val)
        
        while j > -1:
            print(curr_longest_set, i, j)
            if curr_val % nums[j] == 0:
                curr_longest_set.append(nums[j])
            j -=1
        
        
        if len(curr_longest_set) > len(longest_set):
            longest_set.clear()
            longest_set = [i for i in curr_longest_set]
        curr_longest_set.clear()
        
        i-=1
        j = i -1
        
    return longest_set


x = largestDivisibleSubset([1,7,14,33,66,132])
print(x)