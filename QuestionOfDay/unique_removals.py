class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        
        val_dict = {}
        for value in arr:
            if value in val_dict:
                val_dict[value] +=1
            else:
                val_dict[value] = 1
        
        sort_arrr = sorted(val_dict.items(), key=lambda x:x[1])
        
        decrement_count = sort_arrr[0][1]
        for _ in range(k):
            if decrement_count > 1:
                decrement_count-=1
            else:
                del sort_arrr[0]
                decrement_count = sort_arrr[0][1]
            
        return(len(sort_arrr))
        
x = Solution().findLeastNumOfUniqueInts([4,3,1,1,3,3,2], 2)

a = b = x

print(b)