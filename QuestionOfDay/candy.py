class Solution:
    def candy(self, ratings: list[int]) -> int:
        current_priority = 0
        output = [1] * len(ratings)
            
        for i,j in enumerate(ratings):
            
            if i == 0 and ratings[i] > ratings[i+1]:
                output[i] +=1

            elif i+1 < len(ratings) and ratings[i-1] > ratings[i] > ratings[i+1]:
                current_priority = ratings[i]
                output[i] +=1
                index = i
                while index > 0:
                    if ratings[index-1] == ratings[index] and output[index-1]<output[index]:
                        output[index-1] = output[index]
                    if current_priority > ratings[index-1]:
                        break
                    else:
                        current_priority = ratings[index-1]
                        output[index-1] +=1
                    index-=1
                    
            elif ratings[i]>ratings[i-1]:
                output[i]+= output[i-1]
                
            elif i+1 > len(ratings) - 1:
                if ratings[i] > ratings[i-1]:
                    output[i] +=1
                elif ratings[i-1] > ratings[i] and output[i-1] == output[i]:
                    output[i-1]+=1
            print(output)
        return sum(output) 
Solution().candy([1,2,87,87,87,2,1])