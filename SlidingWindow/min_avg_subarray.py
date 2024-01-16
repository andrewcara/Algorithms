def findMaxAverage(nums: list[int], k: int) -> float:
    loop_sum = 0
    
    for number in nums[0:k]:
        loop_sum+=number

    output_max = loop_sum/k
    
    l = 1
    r = k
    
    while r < len(nums):
        print(nums[l], nums[r], output_max)
        loop_sum = loop_sum - nums[l-1] + nums[r]
        output_max = max(output_max, loop_sum/k)
        l +=1
        r +=1
    return output_max


x = findMaxAverage([1,12,-5,-6,50,3], 4)

print(x)