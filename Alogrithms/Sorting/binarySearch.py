def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if arr[mid].grade == x:
            return mid

        elif arr[mid].grade > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        return -1
