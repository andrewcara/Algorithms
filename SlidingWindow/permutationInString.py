def checkInclusion(s1: str, s2: str) -> bool:
    l = 0
    r = len(s1)
    windowStr = ''
    s1 = ''.join(sorted(s1))
    
    while r < len(s2)+1:
        
        windowStr = ''.join(sorted(s2[l:r]))
        
        if windowStr == s1:
            return True
        else:
            l+=1
            r+=1
    
    return False



print(checkInclusion('llb','lolololba'))