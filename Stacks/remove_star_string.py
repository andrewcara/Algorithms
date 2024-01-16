s = "leet**cod*e"

string_stack = []
output_string = ''
for letter in s:
    string_stack.append(letter)
    
    if letter == '*':
        string_stack.pop()
        if string_stack:
            string_stack.pop()

for letter in string_stack:
    output_string +=letter 

print(output_string)