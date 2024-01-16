dict = {5:"Fizz", 3:"Buzz"}
keys = dict.keys()
output_list = []
output_string = ''
for i in range(100):
    for key in keys:
        print(key)
        if i%key==0:
            output_string += dict[key]
    if output_string:
        output_list.append(output_string)
    else:
        output_list.append(i)
    output_string=''

print(output_list)