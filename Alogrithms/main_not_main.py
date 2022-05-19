from student import Student
from insertionSort import insertionSort
from binarySearch import binary_search
from linearSearch import linearSearch

from names import student_names

import random, time

for i in range(10):
    start_time = time.time()

    # Code for objects generation
    arr = []
    for i in range(0, 5):
        random_name_value = random.randint(0, len(student_names) - 1)
        new_object = Student(
            student_names[random_name_value], random.randint(1, 100))
        arr.append(new_object)

    # # Print all 75000 generated objects formatted to the console
    # for i in range(len(arr_75000)):
    #     print(
    #         "Rank: {} - Grade: {}".format(str(arr_75000[i].isGraduating), str(arr_75000[i].grade)))

    # print('______________________________________________________________')
    # print("Before sorting (10):")

    # # Print first & last 20 objects in the arr_75000
    # if len(arr) > 20:
    #     print("\nFirst 20 objects:")
    #     for i in range(20):
    #         print(
    #             "Name: {} - Grade: {}".format(arr[i].name, str(arr[i].grade)))

    # # Print last 20 objects in the arr_75000

    # if len(arr) > 20:
    #     print("\nLast 20 objects:")
    #     for i in range(len(arr) - 20, len(arr)):
    #         print(
    #             "Name: {} - Grade: {}".format(arr[i].name, str(arr[i].grade)))

    # if len(arr) < 20:
    #     print("\nLast " + str(len(arr)) + " Objects:")
    #     for i in range(len(arr)):
    #         print(
    #             "Name: {} - Grade: {}".format(arr[i].name, str(arr[i].grade)))

    # print('______________________________________________________________')

    # Searching the array using linear search (before sorting)
    search_for = 50

    time_start_linear = time.time()

    unsorted_arr_linear = linearSearch(arr, search_for)

    print(str((time.time() - time_start_linear)*1000))

    if unsorted_arr_linear == -1:
        print("\nLinear search: No student found with grade: {}".format(search_for))
    else:
        print("\nLinear search: Student found with grade: {}".format(
            search_for) + " at index: {}".format(unsorted_arr_linear))

    # Sorting the array by grade using insersion sort
    insertionSort(arr)

    # #Print first 20 objects in the sorted array
    # print("\nAfter sorting (10):")

    # if len(arr) > 20:
    #     print("\nFirst 20 objects:")
    #     for i in range(20):
    #         print(
    #             "Name: {} - Grade: {}".format(arr[i].name, str(arr[i].grade)))

    # # Print last 20 objects in the sorted array


    # if len(arr) > 20:
    #     print("\nLast 20 objects:")
    #     for i in range(len(arr) - 20, len(arr)):
    #         print(
    #             "Name: {} - Grade: {}".format(arr[i].name, str(arr[i].grade)))

    # if len(arr) < 20:
    #     print("\nFirst " + str(len(arr)) + " Objects:")
    #     for i in range(len(arr)):
    #         print(
    #             "Name: {} - Grade: {}".format(arr[i].name, str(arr[i].grade)))


    # print('______________________________________________________________')


    

    
    
    # Sorting the array using binary search
    search_for = 50
    arr.sort(key=lambda x: x.grade)

    time_start_binary = time.time()

    sorted_arr_binary = binary_search(arr, 0, len(arr) - 1, search_for)

    print(str((time.time() - time_start_binary)*1000))

    if sorted_arr_binary != -1:
        print("Element at index", str(sorted_arr_binary))
    else:
        print("Element not in array")

    # Searching the arry using linear search (post-sorting)
    search_for = 50
    time_start_linear_sorted = time.time()
    sorted_arr_linear = linearSearch(arr, search_for)
    print(str((time.time() - time_start_linear_sorted)*1000))
   
    if sorted_arr_linear == -1:
        print("\nLinear search: No student found with grade: {}".format(search_for))
    else:
        print("\nLinear search: Student found with grade: {}".format(
            search_for) + " at index: {}".format(sorted_arr_linear))

    

    # time_taken_milliseconds = (time.time() - start_time)*1000

    # print("\n%s ms" % (str((time_taken_milliseconds))))
