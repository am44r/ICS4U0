def doubleCountdown(n, count = 0):
    # Base case - checks if (n) = counter
    # If true returns 0
    if n == count:
        return 0
    # If base case not true log(n - counter) to terminal
    print(n - count)
    # Call the function recursively, passing (n) and incremented counter
    doubleCountdown(n, count+1)
    print(count)
    return 0

# Test cases
doubleCountdown(5)
doubleCountdown(6)
doubleCountdown(3)

# Test cases for you to create
# doubleCountdown(n)
# doubleCountdown(n)
# doubleCountdown(n)

