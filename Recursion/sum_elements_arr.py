def sum_elements_arr(my_arr:list, length) -> sum:
    if length == 1:
        return my_arr[0]
    else:
        return my_arr[length-1] + sum_elements_arr(my_arr, length-1)
    
    
x = sum_elements_arr([1,2,3,4], len([1,2,3,4]))
print(x)