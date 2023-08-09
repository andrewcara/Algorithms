
def dailyTemperatures(temperatures: list[int]) -> list[int]:
    stack = []
    output = [0]*(len(temperatures))

    for i,j in enumerate(temperatures):


        
        while stack and j > stack[-1][1]:
            output[stack[-1][0]] = i - stack[-1][0]
            stack.pop()    
        
        
        stack.append((i,j))
        
    return output


print(dailyTemperatures([73,74,75,71,69,72,76,73]))