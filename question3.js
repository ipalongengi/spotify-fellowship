/**
 * @param {number} amount 
 * @param {number[]} denominations 
 * @returns {number} 
 */
function changePossibilities(amount, denominations){
    // Create an array with size equal to the amount of money plus one
    // The value in each element will be updated to reflect the number
    // of combinations possible for that amount given the list of
    // denominations
    combinations = new Array(amount + 1);

    // Fill up the array with zeroes, except the zeroth element.
    // The zeroth element is initialized to 1 as seed/starting value
    combinations.fill(0);
    combinations[0] = 1;

    // Loop through every denominations
    for (let denom of denominations){
        // Loop through every integer upto the amount that
        // we want to get change from
        for (let amt = 1; amt <= amount + 1; amt++){
            if (amt >= denom) {
                combinations[amt] += combinations[amt-denom];
            }
        }
    }

    return combinations[amount];
}

console.log(changePossibilities(4, [1, 2, 3, 4]));
console.log(changePossibilities(100, [1, 5, 10, 25, 50]));

