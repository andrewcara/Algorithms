class Solution:
    
    def findPalindrome(self, word:str) -> bool:
        
        length_word = len(word)//2
        if length_word == 0:
            return True
        for i in range(length_word):
            if word[i] != word [-1-i]:
                return False
            
        return True

    def countSubstrings(self, s: str) -> int:
        i, j = 0, 0
        output = []
        while i < len(s):

            for j in range (i, len(s)):
                print(s[i:j+1])
                if self.findPalindrome(s[i:j+1]):
                    output.append(s[i:j+1])
            i+=1
        print(output)
Solution().countSubstrings("abc")