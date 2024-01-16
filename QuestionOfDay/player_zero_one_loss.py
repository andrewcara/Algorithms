loser_dict = {}
output =[[],[]]
matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]

for result in matches:
    if result[1] in loser_dict:
        loser_dict[result[1]] +=1
    else:
        loser_dict[result[1]] = 1
    if result[0] not in loser_dict:
        loser_dict[result[0]] = 0

for k,v in loser_dict.items():
    if v == 0:
        output[0].append(k)
    elif v ==1:
        output[1].append(k)
        
output[0].sort()
output[1].sort()
print(output)