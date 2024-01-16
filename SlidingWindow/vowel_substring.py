def maxVowels(s: str, k: int) -> int:
        vowel_dict = {'a':0,'e':0,'i':0,'o':0,'u':0}
        vowel_count = 0
        max_vowels = 0
        for window in s[0:k]:
            if window in vowel_dict:
                vowel_count+=1
           
        max_vowels = vowel_count
        for i, j in enumerate(s[k:]):
            
            if j in vowel_dict:
                vowel_count +=1
            if s[i-1] in vowel_dict:
                vowel_count -=1
            max_vowels = max(max_vowels, vowel_count)
            print(s[i-1], j, max_vowels, i)
        print(max_vowels)
        
maxVowels("weallloveyou", 7)