'''
Given a array of numbers, and a single number n, return an 
extracted array of unique numbers that are 
evenly divisible by n recursivley. Your extracted array should be 
sorted in ascending numerical order.
'''
def extract_even_numbers(numbers, n):
    if len(numbers) == 0:
        return []
    if numbers[0] % n != 0:
        return extract_even_numbers(numbers[1:], n)
    return [numbers[0]] + extract_even_numbers(numbers[1:], n)

print(extract_even_numbers([1,9,3,4,3,6,7,8,9], 3))