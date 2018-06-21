/**
 * @param {string} s 
 * @returns {string} 
 */
function decodeString(s) {
    let digit_stack = [];
    let char_stack = [];
    let result = '';

    for (let i = 0; i < s.length; i++) {
        if (s[i] >= '0' && s[i] <= '9') {
           digit_stack.push(s[i] - '0');
        }

        else if (s[i] === ']') {
            let popped_char = char_stack.pop();
            let temp = '';
            while (popped_char !== '[') {
                temp = popped_char + temp;
                popped_char = char_stack.pop();
            }

            let k = digit_stack.pop();
            temp = temp.repeat(k);

            for (let j of temp) {
                char_stack.push(j);
            }
        }

        else {
            char_stack.push(s[i]);
        }

    }

    while (char_stack.length > 0) {
        result = char_stack.pop() + result;
    }

    console.log('The original input is: ' + s);
    return result;
}

console.log(decodeString('2[a3[bc]]'));
console.log(decodeString('2[a3[5[b]c]]'));

