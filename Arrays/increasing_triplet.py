class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        
        length_of_list = len(nums)

        if length_of_list < 3:
            return False
        
        i = 0
        while i < length_of_list - 2:

            if nums[i] < nums [i+1] and nums[i+1] < nums[i+2]:
                return True
            i+=1
        return False