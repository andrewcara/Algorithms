

def reverse(string, length):
    if length < 1:
        return ""
     
    # Base case
    if length == 1:
        return string[0]
    
    print(string[length -1])
    return string[length - 1] + reverse(string, length - 1)
 
x = reverse("hello", len("hello"))
print(x)