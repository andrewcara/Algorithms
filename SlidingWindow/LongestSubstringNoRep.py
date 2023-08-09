def lengthOfLongestSubstring( s: str) -> int:
    
    if len(s) < 2:
        return(len(s))

    l = 0
    r = 1
    trackingDic = {}
    longestCount = 0
    trackingDic[s[l]] = longestCount
    
    longestCount =1
    currentLongest = longestCount
    
    while r < len(s):
        if s[r] not in trackingDic:
            trackingDic[s[r]] = longestCount
            longestCount +=1
            r+=1
            currentLongest = max(currentLongest, longestCount)
        else:
            trackingDic.clear()
            longestCount = 0
            l +=1 
            trackingDic[s[l]] = longestCount
            longestCount = 1
            r = l+1
            
    return currentLongest
            
        
        
    