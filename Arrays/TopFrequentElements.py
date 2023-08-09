def topKFrequent(nums: list[int], k: int):
    
    output_list = []
    
    tracking_numbers_dict = {}
    
    unique_num_index = 0
    
    
    for number in nums:
        
        if number not in tracking_numbers_dict:
            tracking_numbers_dict[number] = unique_num_index
        if number in tracking_numbers_dict:
            tracking_numbers_dict[number] += 1

    tracking_numbers_dict = dict(sorted(tracking_numbers_dict.items(), key=lambda item: item[1]))
    return(list(tracking_numbers_dict)[-k::])
        
        

topKFrequent([1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,3],2)