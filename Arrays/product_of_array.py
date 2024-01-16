# class Solution:
#     def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        
lis = [1,2,3,4]

prefix = [1]
prefix_sum = 1

for i in range(1,len(lis)):
    prefix_sum *= lis[i-1]
    prefix.append(prefix_sum)

post_sum = 1
post = [1]

for i in range(len(lis),1,-1):
    post_sum *= lis[i-1]
    post.insert(0, post_sum)


output = [a*b for a,b in zip(post,prefix)]
print(output)