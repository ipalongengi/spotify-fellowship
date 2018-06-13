def decodeString(s):
    count_stack = []
    string_stack = []
    temp = ''
    result = ''

    for i in range(len(s)):
        count = 0
        if s[i].isdigit():
            while s[i].isdigit():
                count = count * 10 + ord(s[i]) - ord('0')
                i += 1

            i -= 1
            count_stack.append(count)

        elif s[i] == ']':
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

        elif s[i] == '[':
            if s[i-1].isdigit():
                string_stack.append(s[i])

            else:
                string_stack.append(s[i])
                count_stack.append(1)

        else:
            string_stack.append(s[i])

    while len(string_stack) > 0:
        result = string_stack.pop() + result;
        string_stack.pop()

    print (result)

decodeString('2[ab]')
decodeString('2[b3[a]]')


