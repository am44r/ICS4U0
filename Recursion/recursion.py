def extractEvenlyDivisible(array, divisor):
    def helper(arr, index):
        if(len(arr) == index + 1):
            return arr
        elif ((arr[index] % divisor) == 0):
            return helper(arr, index + 1)
        else:
            arr.pop(index)
            return helper(arr, index)
    return sorted(set(helper(array, 0)))


print(extractEvenlyDivisible([1,9,3,4,3,6,7,8,9], 3))