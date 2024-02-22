class Solution:
    def numSquares(self, n: int) -> int:
        sqrt_n = n ** (1/2)
        sqrt_int = int(sqrt_n)
        possible_arr = []
        
        
        for i in range(sqrt_int):
            possible_arr.append((i+1)**2)
        
        
        if possible_arr[-1] == n:
            return 1

        number_slots = [possible_arr[-1]]
        current_position = len(possible_arr) - 1
        starting_position = current_position
        minimum_length  = n
    
        while starting_position > 0:
            
            if sum(number_slots) > n:
                
                if current_position == 0:
                    number_slots.clear()
                    
                    starting_position -=1
                    current_position = starting_position
                    number_slots.append(possible_arr[starting_position])
                else:
                    number_slots.pop()
                    current_position -=1
                    number_slots.append(possible_arr[current_position])
            else:                    
                number_slots.append(possible_arr[current_position])
            
            if sum(number_slots) == n:
                minimum_length = min(minimum_length, len(number_slots))            
            print(number_slots, current_position, starting_position)
        return minimum_length
        


x = Solution().numSquares(43)
print(x)