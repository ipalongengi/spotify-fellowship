def sortByStrings(s, t):
    # importing this built-in library is important to ensure that
    # the dictionary remembers the order in which keys are entered
    from collections import OrderedDict

    hash_chars = OrderedDict()
    for char in t:
        hash_chars[char] = 0

    for char in s:
        if hash_chars.get(char) is not None:
            hash_chars[char] += 1

    output = ''
    for char in hash_chars:
        output += hash_chars[char]*char

    return output


print(sortByStrings('weather', 'therapyw'))
print(sortByStrings('good', 'odg'))
