class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minimum = min(len(word1), len(word2))
        output_string = ''
        
        remainder = len(word1) - len(word2)
        
        for i in range(minimum):
            output_string += (word1[i])
            output_string += (word2[i])
        

        if remainder == 0:
            return output_string
            
        elif remainder < 0:
            print(word2[minimum:minimum+(remainder*-1)])
            output_string += word2[minimum:minimum+remainder]
            return output_string

        output_string += word1[minimum:minimum+remainder]
        return output_string
        
        
x = Solution().mergeAlternately('ab', 'pqrs')

print(x)