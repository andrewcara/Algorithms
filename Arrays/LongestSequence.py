def longestConsecutive(nums: list[int]) -> int:
    longest_int = 1
    nums.sort()
    max = 1
    if not nums:
        return 0
    for i in range(len(nums)-1):
        
        if nums[i] + 1 == nums[i+1]:
            longest_int +=1
            if longest_int > max:
                max = longest_int
        elif nums[i]==nums[i+1]:
            continue
        else:
            longest_int = 1
    return max
            
longestConsecutive([0,3,7,2,5,8,4,6,0,1])