

def recursive_func(x) -> int:
    if x==0:
        return 0
    else:
       return x + recursive_func(x-1)
        

x = recursive_func(5)

print(x)
