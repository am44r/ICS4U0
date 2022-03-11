def extractEvenlyDivisible(numbers, n):
    if len(numbers) == 0 or n == 0:
        return []

    if numbers[0] % n != 0:
        return extractEvenlyDivisible(numbers[1:], n)

    return [set([numbers[0]]+extractEvenlyDivisible(numbers[1:], n)).sort()]


print(extractEvenlyDivisible([1, 9, 3, 4, 3, 6, 7, 8, 9], 3))
