def linearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i].grade == x:
            return i

    return -1
