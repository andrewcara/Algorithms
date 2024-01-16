
senate = "RDDRRRR"
senate_length = len(senate)
radiant_dict = []
dire_dict = []


for i,j in enumerate(senate):
    if j == 'D':
        dire_dict.append(i)
    else:
        radiant_dict.append(i)


dire_length = len(dire_dict)
radiant_length = len(radiant_dict)

while dire_dict and radiant_dict:
    
    if dire_dict[0] < radiant_dict[0]:
        radiant_dict.pop(0)
        dire_dict.append(dire_dict[0] + senate_length)
        dire_dict.pop(0)
    
    else:
        dire_dict.pop(0)
        radiant_dict.append(radiant_dict[0] + senate_length)
        radiant_dict.pop(0)
    
    
print(radiant_dict, dire_dict)   

 