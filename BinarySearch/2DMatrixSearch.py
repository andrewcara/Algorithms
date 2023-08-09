
def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    verticalHigh = len(matrix)-1
    verticalLow = 0


    horizontalHigh = len(matrix[0])-1
    horizontalLow = 0


    while verticalLow<=verticalHigh:
        
        verticalMid = (verticalHigh+verticalLow)//2
        if target > matrix[verticalMid][horizontalHigh]:
            verticalLow = verticalMid +1
        elif target < matrix[verticalMid][horizontalLow]:
            verticalHigh = verticalMid -1
        else:
            break
    searchRow = verticalMid
    
    while horizontalLow<=horizontalHigh:
        horizontalMid = (horizontalHigh + horizontalLow)//2
        print(matrix[searchRow][horizontalMid])
        if matrix[searchRow][horizontalMid] == target:
            return True
        elif matrix[searchRow][horizontalMid] < target:
            horizontalLow = horizontalMid + 1
        elif  matrix[searchRow][horizontalMid] > target:
            horizontalHigh = horizontalMid -1
    return False


l = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

target = 23
print(searchMatrix(l,target))

