def reverseVowels(s: str) -> str:
        vowels = ['a','e','i','o','u']
        tracking_stack = [letter for letter in s if letter in vowels]
        output_string = ''
        for letter in s:
            if letter.lower() in vowels: 
                letter = tracking_stack.pop()
                output_string +=letter
            else:
                output_string +=letter
        print(output_string)
reverseVowels('hello')