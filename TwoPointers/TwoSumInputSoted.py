#Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.
#Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
#The tests are generated such that there is exactly one solution. You may not use the same element twice.
#Your solution must use only constant extra space.


#Here it makes mroe sense to start from the end. And work out way inwards. that Way we don't even have to acknowledge the end condition
#If the sum is larger than the target we move the right pointer left
#otherwise we move the left pointer right


def twoSum(numbers: list[int], target: int) -> list[int]:
    l, r = 0, len(numbers)-1
        
    while(r>l):
        if numbers[l] + numbers[r] == target:
            return([l+1,r+1])
        elif numbers[l] + numbers[r] < target:
            l +=1
        else:
            r-=1


print(twoSum([1,3,7,8], 10))