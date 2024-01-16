input_list = list(range(100))



filtered_list = [i for i in input_list if i%5==0]

filtered_list1 = list(filter(lambda x: x%5==0, input_list))


filtered_list2 = list(map(lambda x: x**5, input_list))

filtered_list2 = [x for x in reversed(filtered_list2)]

print(filtered_list2)