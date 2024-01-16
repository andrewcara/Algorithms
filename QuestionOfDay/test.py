class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        
        rooms_keys = [0]
        room_set = {0}
        
        while rooms_keys:
            
            for j in rooms[rooms_keys.pop()]:
                if j not in room_set:
                    room_set.add(j)
                    rooms_keys.append(j)
        
        return len(room_set) == len(rooms)
                
        
        
        
        


x = Solution().canVisitAllRooms([[1,3],[1,4],[2,3,4,1],[],[4,3,2]])

print(x)