class Solution:
    def find_shortest_repeating(self, str2:str) -> str:
        shortest_substring = ''
        length_of_string2 = len(str2)
            
        for letter in range(1,length_of_string2):
            
            if str2[0:letter] * (length_of_string2//(letter)) == str2:
                shortest_substring = str2[0:letter]
                return shortest_substring
            
            
        return str2
            
    
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        longest_substring = ''
        length_of_string1 = len(str1)
        
        shortest_repeating = self.find_shortest_repeating(str2)
        
        while len(shortest_repeating) <= length_of_string1//2:
            print(shortest_repeating, longest_substring)
            
            if shortest_repeating * (length_of_string1//len(shortest_repeating)) == str1:
                
                longest_substring = shortest_repeating
            
            shortest_repeating += shortest_repeating
            
        
        if longest_substring:
            return longest_substring
        return ''
        
        
    


x = Solution()

print(x.gcdOfStrings('abcabc', 'abc'))

print(len('NLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGM'))
print(len('NLZGMNLZGMNLZGMNLZGM'))