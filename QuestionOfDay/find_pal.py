class Solution:

    def findPalindrome(self, word:str) -> bool:
        
        length_word = len(word)//2
        
        for i in range(length_word):
            print(word[i], word[-1-i])
            if word[i] != word [-1-i]:
                return False
            
        return True

    def firstPalindrome(self, words: list[str]) -> str:
        for word in words:
            if self.findPalindrome(word):
                return word
        return ''
            

Solution().firstPalindrome(["abc","car","ada","racecar","cool"])