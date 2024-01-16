n = 4


r = n
d = n -1
l = n -1
u = n - 2

my_matrix = [([0]*n) for i in range(n)]
count=1
x,y = 0,0

turns = (2*n) -1

for turn in range(turns):
    number = turn%4
    
    if number ==0:
        for i in range(r):
            my_matrix[x][y] = count
            y+=1
            count+=1
        y -=1
        x+=1
        r-=2 
         
    elif number == 1:
        for i in range(d):
            my_matrix[x][y] = count
            x +=1
            count+=1
        x-=1
        y-=1
        d-=2
        
        
    elif number == 2:
        print(x,y)
        for i in range(l):
            my_matrix[x][y] = count
            y -=1
            count+=1
            print(x,y,count)
        y +=1
        x-=1
        l-=2
    
    else:
        for i in range(u):
            my_matrix[x][y] = count
            x-=1
            count+=1
        x +=1
        y+=1
        u-=2

print(my_matrix)