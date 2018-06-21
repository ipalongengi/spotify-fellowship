def decodeString(s):
    from re import findall

    string_stack = []
    count_stack = []
    result = ''
    temp = ''
    prev_elem = ''

    
    # extract all digits from the string
    count_stack = list(map(int, findall(r'\d+',s)))

    for char in s:
        if char.isdigit():
            prev_elem = char

        elif char == ']':
            temp = ''
            count = 0

            if len(count_stack) > 0:
                count = count_stack[-1]
                count_stack.pop()
            while len(string_stack) > 0 and string_stack[-1] != '[':
                temp = string_stack[-1] + temp
                string_stack.pop()
            if len(string_stack) > 0 and string_stack[-1] == '[':
                string_stack.pop()

            result = count * (result + temp)

            for char in result:
                string_stack.append(char)

        elif char == '[':
            if prev_elem.isdigit():
                string_stack.append(char)
            else:
                string_stack.append(char)
                count_stack.append(1)

        else:
            string_stack.append(char)
            prev_elem = char

    while len(string_stack) > 0:
        result = string_stack.pop() + result
        string_stack.pop()

    return result

print(decodeString('2[ab]'))
print(decodeString('2[b3[a]]'))

