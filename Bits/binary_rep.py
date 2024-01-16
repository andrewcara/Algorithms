n = 5
ones_counted = 0
remainder = 0
result = n
output = [0]

for i in range(1, n+1):
    result = i
    while result > 0:
        if result % 2 == 1:
            ones_counted +=1
        
        result = result //2
        
    output.append(ones_counted)
    ones_counted = 0
    
print(output)
        
        
    