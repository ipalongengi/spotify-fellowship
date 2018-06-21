def changePossibilities(amount, denominations):
    # create a list with size equal to the amount of money plus one
    # the value in each element will be updated to represent the number
    # of combinations possible given the denominations
    combinations = [0] * (amount + 1)

    # set the value of the zeroth element to 1 as starting/seed value
    combinations[0] = 1
    
    # loop through every denomination
    for denom in denominations:
        # loop through every amount of money upto 'amount' 
        for amount in range (1, amount + 1):
            if amount >= denom:
                combinations[amount] += combinations[amount - denom]
                
    return combinations[amount]


print(changePossibilities(4, [1, 2, 3]))
print(changePossibilities(100, [1, 5, 10, 25, 50]))
