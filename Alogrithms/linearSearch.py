from student import Student
from names import student_names

import random, time


def linearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i].grade == x:
            return i

    return -1


trial = 1
search_for_1 = 70
search_for_2 = 101

for i in range(10):
    # Creating Objects
    arr = []
    for i in range(0, 10):
        random_name_value = random.randint(0, len(student_names) - 1)
        new_object = Student(
            student_names[random_name_value], random.randint(1, 100))
        arr.append(new_object)

    
    # Before Sorting
    # Ele exists
    time_linear_unsorted_exist = time.time()

    unsorted_linearsearch_exist = linearSearch(arr, search_for_1)

    time_linear_unsorted_exist = (time.time() - time_linear_unsorted_exist)*1000

    # Ele doesn't exist
    time_linear_unsorted_not_exist = time.time()
    
    unsorted_linearsearch_not_exist = linearSearch(arr, search_for_2)
    
    time_linear_unsorted_not_exist = (time.time() - time_linear_unsorted_not_exist)*1000


    # After Sorting

    arr.sort(key=lambda x: x.grade)

    # Ele exists
    time_linear_sorted_exist = time.time()
    
    sorted_linearsearch_exist = linearSearch(arr, search_for_1)
    
    time_linear_sorted_exist = (time.time() - time_linear_sorted_exist)*1000

    # Ele doesn't exist
    time_linear_sorted_not_exist = time.time()
    
    sorted_linearsearch_not_exist = linearSearch(arr, search_for_2)
    
    time_linear_sorted_not_exist = (time.time() - time_linear_sorted_not_exist)*1000

    print('\n----------------------------------------')
    print(f'Trial {trial}')
    print('----------------------------------------')
    
    print(f'\n---Linear Searching---')
    
    print(f'Before Sorting:')
    print(f'Element exists: {time_linear_unsorted_exist} ms')
    print(f'Element doesn\'t exist: {time_linear_unsorted_not_exist} ms\n')
    
    print(f'After Sorting:')
    print(f'Element exists: {time_linear_sorted_exist} ms')
    print(f'Element doesn\'t exist: {time_linear_sorted_not_exist} ms')

    trial += 1


    


