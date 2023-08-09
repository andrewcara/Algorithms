def isPalindrome(s: str) -> bool:
    s = s.lower()
    s = ''.join(filter(str.isalnum, s))
    
    rightPointer = len(s) - 1
    lefPointer = 0
    while rightPointer > lefPointer:
        if s[rightPointer] == s [lefPointer]:
            rightPointer -= 1
            lefPointer +=1
            print(s[rightPointer], s[lefPointer])
        else:
            return False
        
    
    return True
    

x = isPalindrome(" ")

print(x)