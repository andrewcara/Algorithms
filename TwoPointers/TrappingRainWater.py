#Here we are keeping track of the right and left maxes
#We need to find the local maximums on both sides to see how to procede with rain collection
#for Example if the max is 3 on the left and 0 on the right, we cannot rule out that 0 was is stored
#so we have to move from the maximum that is smaller#
#If the maximum on the right is now 1 and the max on the left is 3, we know that water containment is possible moving from the right side if the height is less than MaxRight or 1
#Depending on which side we are moving from we always take the lesser value

class Solution:
    def trap(self, height: list[int]) -> int:
        leftP = 0
        rightP = len(height) - 1
        maxLeft = height[leftP]
        maxRight = height[rightP]
        totalWater = 0
        
        while leftP < rightP:
            
            if maxLeft < maxRight:
                if maxLeft - height[leftP+1] > 0:
                    totalWater += maxLeft - height[leftP+1]
                else:
                    maxLeft = height[leftP+1]
                leftP +=1
            
            else:
                if maxRight - height[rightP-1]>0:
                    totalWater += maxRight - height[rightP-1]
                else:
                    maxRight = height[rightP-1]
                rightP -=1
    
        return totalWater
    
