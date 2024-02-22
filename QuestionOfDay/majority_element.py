def majorityElement(nums: list[int]) -> int:

    output = 0
    curr_max = 0
    track_nums = {}

    for element in nums:

        if element in track_nums:
            track_nums[element]+=1
            if track_nums[element] > curr_max:
                curr_max = track_nums[element]
                output = element
        else:
            track_nums[element] = 1
            if track_nums[element] > curr_max:
                curr_max = track_nums[element]
                output = element
    return output

    


majorityElement([6,5,5])