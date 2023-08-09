def twoSum(nums: list[int], target: int) -> list[int]:
    rightPointer = 1
    leftPointer = 0
    finalPosition = []
    while(rightPointer <= len(nums)):
        print(leftPointer,rightPointer)
        if nums[leftPointer] + nums[rightPointer] == target:
            finalPosition.append(leftPointer)
            finalPosition.append(rightPointer)
            return finalPosition

        elif rightPointer < len(nums)-1:
            rightPointer += 1
        else:
            leftPointer += 1 
            rightPointer = leftPointer + 1
       


x = twoSum([0,4,3,0],0)
print(x)