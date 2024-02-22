class Solution:
    def frequencySort(self, s: str) -> str:
        empty_dic ={}
        for character in s:
            if character in empty_dic:
                empty_dic[character] += 1
            else:
                empty_dic[character]=1
        
        
        output = sorted(empty_dic.items(), key=lambda x: x[1], reverse=True)
        
        str_out = ''
        
        for item in output:
            str_out += item[0] * item[1]

        print(str_out)
Solution().frequencySort('Aabb')
            