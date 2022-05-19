from student import Student
from names import student_names

import random
import time


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


trial = 1

for i in range(10):
    # Creating Objects
    arr = []
    for i in range(0, 500000):
        random_name_value = random.randint(0, len(student_names) - 1)
        new_object = Student(
            student_names[random_name_value], random.randint(1, 100))
        arr.append(new_object)
        
    
    search_for_1 = arr[-1].grade
    search_for_2 = 101

    arr.sort(key=lambda x: x.grade)


    # Ele exists
    time_binary_exist = time.time_ns()
    binary_search_exist = binary_search(arr, 0, len(arr) - 1, search_for_1)
    time_binary_exist = (time.time_ns() - time_binary_exist)/1000000

    # Ele doesn't exist
    time_binary_not_exist = time.time_ns()
    binary_search_not_exist = binary_search(arr, 0, len(arr) - 1, search_for_2)
    time_binary_not_exist = (time.time_ns() - time_binary_not_exist)/1000000

    print("\n-------------------------------------------------------")
    print(f"Trial: {trial}")
    print("-------------------------------------------------------")

    print(f"Element exists: {time_binary_exist} ms")
    
    print(f"Element doesn't exist: {time_binary_not_exist} ms")

    trial+=1