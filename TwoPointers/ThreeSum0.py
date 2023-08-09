#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#Notice that the solution set must not contain duplicate triplets.

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.


def threeSum(nums: list[int]) -> list[list[int]]:
    l = 0
    c = 1
    r = 2
    threeSumDic = {}
    dictionary_index = 0
    outputArray = []
    
    while(r<len(nums)):
        sum = nums[l] + nums[c] + nums[r]
        if sum == 0:
            dic_array = [nums[l],nums[c],nums[r]]
            dic_array.sort()
            dic_string = f'{dic_array[0]} {dic_array[1]} {dic_array[2]}'
            if dic_string not in threeSumDic:
                threeSumDic[dic_string] = dictionary_index
                outputArray.append([nums[l],nums[c],nums[r]])
                dictionary_index+=1
            
        if r != len(nums) - 1:
            r+=1
        elif c != len(nums) - 2:
            c+=1
            r = c+1
        else:
            l+=1
            c= l+1
            r = c + 1
        print(l,c,r)
    return outputArray    

threeSum([-1,0,1,2,-1,-4])         