class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        cities_visited = set()
        next_city = []
        provinces = 0
        l = 0
        
        while l < len(isConnected):
            
            if l in cities_visited:
                pass
            
            else:
                next_city.append(l)
                cities_visited.add(l)
                
                while next_city:
                    city = next_city.pop()
                    print(isConnected[city], l)
                    
                    for i,j  in enumerate(isConnected[city]):
                        if j ==1 and i not in cities_visited:
                            cities_visited.add(i)
                            next_city.append(i)
                
               
                provinces +=1
                
            l+=1

            
        
        return provinces
            


x = Solution().findCircleNum([[1,1,0],[1,1,0],[0,0,1]])
print(x)