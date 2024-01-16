class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        
        dict = {}
        for number in arr:
            
            if number in dict:
                dict[number] +=1
            else:
                dict[number] = 1
        
        print(set(dict.values()), set(dict.values()))
        return set(dict.values()) == (dict.values())
        

x = Solution().uniqueOccurrences([1,2,2,1,1,3])