

class Solution:
    def compress(self, chars: list[str]) -> list[str]:
        dic = {}
        if len(chars) == 1:
            return 1
        for character in chars:
            if character in dic:
                dic[character]+=1
            else:
                dic[character] = 1
        chars = ['1,2,3,4,5']
        return chars


x = Solution().compress(chars = ["a","a","b","b","c","c","c"])

chars  = ["a","a","b","b","c","c","c"]
print(chars)
chars  = ['a','2']

print(chars)
print(x)