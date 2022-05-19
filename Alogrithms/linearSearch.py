from student import Student
from names import student_names

import random, time


def linearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i].grade == x:
            return i
    

    return -1


trial = 1

for i in range(10):
    
    # Creating Objects
    arr = []
    for i in range(0, 75000):
        random_name_value = random.randint(0, len(student_names) - 1)
        new_object = Student(
            student_names[random_name_value], random.randint(1, 100))
        arr.append(new_object)


    search_for_1 = arr[-1].grade
    search_for_2 = 101

    # Before Sorting
    # Ele exists
    time_linear_unsorted_exist = time.time_ns()
    unsorted_linearsearch_exist = linearSearch(arr, search_for_1)
    time_linear_unsorted_exist = (time.time_ns() - time_linear_unsorted_exist)

    # Ele doesn't exist
    time_linear_unsorted_not_exist = time.time_ns()
    unsorted_linearsearch_not_exist = linearSearch(arr, search_for_2)
    time_linear_unsorted_not_exist = (time.time_ns() - time_linear_unsorted_not_exist)


    # After Sorting

    arr.sort(key=lambda x: x.grade)

    # Ele exists
    time_linear_sorted_exist = time.time_ns()
    sorted_linearsearch_exist = linearSearch(arr, search_for_1)
    time_linear_sorted_exist = (time.time_ns() - time_linear_sorted_exist)

    # Ele doesn't exist
    time_linear_sorted_not_exist = time.time_ns()
    sorted_linearsearch_not_exist = linearSearch(arr, search_for_2)
    time_linear_sorted_not_exist = (time.time_ns() - time_linear_sorted_not_exist)

    print('\n----------------------------------------')
    print(f'Trial {trial}')
    print('----------------------------------------')
    
    print(f'\n---Linear Searching---')
    
    print(f'Before Sorting:')
    print(f'Element exists: {time_linear_unsorted_exist/1000000} ms')
    print(f'Element doesn\'t exist: {time_linear_unsorted_not_exist/1000000} ms\n')
    
    print(f'After Sorting:')
    print(f'Element exists: {time_linear_sorted_exist/1000000} ms')
    print(f'Element doesn\'t exist: {time_linear_sorted_not_exist/1000000} ms')

    trial += 1


    


