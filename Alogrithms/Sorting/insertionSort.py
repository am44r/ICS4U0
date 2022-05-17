def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i].grade

        j = i - 1
        while j >= 0 and key < arr[j].grade:
            arr[j+1].grade = arr[j].grade
            j -= 1
        arr[j+1].grade = key
