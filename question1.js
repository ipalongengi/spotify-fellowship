/**
 * Create something 
 *
 * @param {string} s
 * @param {string} t
 * @returns {string} The string s sorted by occurrence of t
 *
 */
function sortByStrings(s, t){
    let t_map = new Map();

    for (let ch of t) {
        t_map.set(ch, 0);
    }

    for (let ch of s) {
        if (t_map.has(ch)){
            t_map.set(ch, t_map.get(ch) + 1);
        }
    }

    let output = '';
    for (let ch of t_map) {
        output += ch[0].repeat(ch[1]);
    }

    return output;
}

console.log(sortByStrings('weather', 'therapyw'));
console.log(sortByStrings('good', 'odg'));

