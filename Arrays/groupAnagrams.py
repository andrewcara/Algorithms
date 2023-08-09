def groupAnagrams(strs: list[str]) -> list[list[str]]:

    anagram = {}
    anagram_index = 0
    output_list = [[]]
    
    
    for string in strs:
        
        sorted_string = ''.join(sorted(string))
        
        if sorted_string not in anagram:
            anagram[sorted_string] = anagram_index
            output_list.append([string])
            anagram_index +=1
        else:
            output_list[anagram[sorted_string]].append(string)
    
    return output_list

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))          