from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        output = 0
        l = 0
        r = len(nums) - 1
        nums = sorted(nums)
        print(l,r,nums)
        while r > l:
            if nums[r] + nums[l] == k:
                del nums[l]
                del nums[r -1]

                r = r-2
                output+=1
                
            else:
                l+=1
                r-=1
            
            
        
            
        return output
    
x = Solution().maxOperations([1,2,3,4], k = 5)
print(x)