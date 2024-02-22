class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        
        trust_dict = {}
        vote_dict = {}
        
        for element in trust:
            if element[1] in trust_dict:
                trust_dict[element[1]]+=1
            else:
                trust_dict[element[1]] = 1
            
            if element[0] in vote_dict:
                vote_dict[element[0]] +=1
            else:
                vote_dict[element[0]] = 1
        
        
        max_value = sorted(trust_dict.items(), key=lambda x : x[1])[-1][0]
        
        print(vote_dict, trust_dict, max_value)
        if trust_dict[max_value] == n -1 and max_value not in vote_dict:
            return max_value
        else:
            return -1
        
        
x = Solution().findJudge(2,[[1,2]])
print(x)

        