class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        
        i = len(nums) - 1
        nums = sorted(nums)
        
        sum_at_point = []
        carry_sum = 0
        
        for i, num in enumerate(nums):
            if i < 2:
                sum_at_point.append(0)
                carry_sum += num
            else:
                sum_at_point.append(carry_sum)
                carry_sum +=num
            
        
        for i in range(i, -1, -1):
            print(sum_at_point[i], nums[i])
            if sum_at_point[i] > nums[i] and i > 1:
                return sum_at_point[i] + nums[i]
        return -1


x = Solution().largestPerimeter([5,5,50])
print(x)