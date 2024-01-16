def decodeString(s: str) -> str:
        bracket_dict = {']':'['}
        bracket_stack = []
        current_string = ''
        output_string = ''
        
        for i in reversed(s):
            
            if i in bracket_dict:
                bracket_stack.append(i)
            
            elif i == bracket_dict[']']:
                bracket_stack.pop()
            
            elif i.isdigit():
                current_string *= int(i)
                output_string = current_string + output_string
                current_string = ''
            
            else:
                current_string = i + current_string
                
            
            print(bracket_stack, output_string)

decodeString('3[a]2[bc]')