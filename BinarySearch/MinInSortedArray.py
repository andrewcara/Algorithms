def findMin(nums: list[int]) -> int:
    l = 0
    r = len(nums)-1
    
    minimum =nums[(l+r)//2] 
    while l<=r:
        mid = (l+r)//2  
        if nums[r]>nums[mid] and nums[mid] >= nums[l]:
            r = mid -1
        elif nums[l] > nums[r] and nums[r] >nums[mid]:
            r = mid -1
        elif nums[mid] >=nums[l] and nums[l] > nums[r]:
            l = mid + 1       
        else:
            minimum = min(nums[mid],minimum)
            print(nums[mid])
            break
        minimum = min(nums[mid],minimum)

findMin([11,13,15,17])