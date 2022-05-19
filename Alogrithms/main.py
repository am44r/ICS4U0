from student import Student
from insertionSort import insertionSort
from binarySearch import binary_search
from linearSearch import linearSearch

from names import student_names

import random
import time

trial = 1

for i in range(1):
    
    # Generating the objects at random
    arr = []
    for i in range(0, 75000):
        random_name_value = random.randint(0, len(student_names) - 1)
        new_object = Student(
            student_names[random_name_value], random.randint(1, 100))
        arr.append(new_object)

    
    # Linear Searching the array using linear search (before sorting) (element exists)
    time_linear_unsorted_exist = time.time()
    
    search_for_1 = 70
    unsorted_linearsearch_exist = linearSearch(arr, search_for_1)
    
    time_linear_unsorted_exist = (time.time() - time_linear_unsorted_exist)*1000

    # if unsorted_linearsearch_exist == -1:
    #     print("Element does not exist")
    # else:
    #     print("Element exists at element: " + str(unsorted_linearsearch_exist))

    
    # Linear Searching the array using linear search (before sorting) (element does not exist)
    time_linear_unsorted_not_exist = time.time()
    
    search_for_2 = 101
    unsorted_linearsearch_not_exist = linearSearch(arr, search_for_2)

    time_linear_unsorted_not_exist = (time.time() - time_linear_unsorted_not_exist)*1000

    # if unsorted_linearsearch_not_exist == -1:
    #     print("Element does not exist")
    # else:
    #     print("Element exists at element: " + str(unsorted_linearsearch_not_exist))


    
    # Insertion Sorting the array
    time_insertion_sort = time.time()

    insertionSort(arr)

    time_insertion_sort = (time.time() - time_insertion_sort)*1000

    
    
    # Linear Searching the array using linear search (after sorting) (element exists)
    time_linear_sorted_exist = time.time()

    sorted_linearsearch_exist = linearSearch(arr, search_for_1)

    time_linear_sorted_exist = (time.time() - time_linear_sorted_exist)*1000

    # if sorted_linearsearch_exist == -1:
    #     print("Element does not exist")
    # else:
    #     print("Element exists at element: " + str(sorted_linearsearch_exist))

    
    # Linear Searching the array using linear search (after sorting) (element does not exist)
    time_linear_sorted_not_exist = time.time()

    sorted_linearsearch_not_exist = linearSearch(arr, search_for_2)

    time_linear_sorted_not_exist = (time.time() - time_linear_sorted_not_exist)*1000

    # if sorted_linearsearch_not_exist == -1:
    #     print("Element does not exist")
    # else:
    #     print("Element exists at element: " + str(sorted_linearsearch_not_exist))



    # Binary Searching the array using binary search (element exists)
    time_binary_search_exist = time.time()

    binary_search_exist = binary_search(arr, 0, len(arr) - 1, search_for_1)

    time_binary_search_exist = (time.time() - time_binary_search_exist)*1000

    # if binary_search_exist == -1:
    #     print("Element does not exist")
    # else:
    #     print("Element exists at element: " + str(binary_search_exist))

    # Binary Searching the array using binary search (element does not exist)
    time_binary_search_not_exist = time.time()

    binary_search_not_exist = binary_search(arr, 0, len(arr) - 1, search_for_2)

    time_binary_search_not_exist = (time.time() - time_binary_search_not_exist)*1000

    # if binary_search_not_exist == -1:
    #     print("Element does not exist")
    # else:
    #     print("Element exists at element: " + str(binary_search_not_exist))

    
    # Printing the times
    print("\n")

    print("----------------------------------------------------")
    print("Trial: " + str(trial))
    print("----------------------------------------------------")

    print("--- Linear Search ---")
    print("Before sorting:")
    print(f"Element exists: {str(time_linear_unsorted_exist)} ms")
    print(
        f"Element does not exist: {str(time_linear_unsorted_not_exist)} ms")
    print("\nAfter sorting:")
    print(f"Element exists: {str(time_linear_sorted_exist)} ms")
    print(f"Element does not exist: {str(time_linear_sorted_not_exist)} ms")\
    
    print("----------------------------------------------------")
    
    print("\n--- Binary Search ---")
    print(f"Element exists: {str(time_binary_search_exist)} ms")
    print(f"Element does not exist: {str(time_binary_search_not_exist)} ms")

    print("----------------------------------------------------")
    
    print("\n--- Insertion Sort ---")
    print(f"Time: {str(time_insertion_sort)} ms")

    trial+=1

    
    