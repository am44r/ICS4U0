from student import Student
from names import student_names

import random, time


def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i].grade

        j = i - 1
        while j >= 0 and key < arr[j].grade:
            arr[j+1].grade = arr[j].grade
            j -= 1
        arr[j+1].grade = key


trial = 1

for i in range(10):
    # Creating Objects
    arr = []
    for i in range(0, 1000):
        random_name_value = random.randint(0, len(student_names) - 1)
        new_object = Student(
            student_names[random_name_value], random.randint(1, 100))
        arr.append(new_object)

    print("\n-------------------------------------------------------")
    print(f"Trial: {trial} ")
    print("-------------------------------------------------------")
    print("Before Sorting")

    # Print first & last 20 objects in the arr_75000
    # if len(arr) > 20:
    #     print("\nFirst 20 objects:")
    #     for i in range(20):
    #         print(
    #             "Name: {} - Grade: {}".format(arr[i].name, str(arr[i].grade)))
    # else:
    #     print("\nFirst " + str(len(arr)) + " objects: ")
    #     for i in range(len(arr)):
    #         print(
    #             "Name: {} - Grade: {}".format(arr[i].name, str(arr[i].grade)))

    
    # Print last 20 objects in the arr_75000
    # if len(arr) > 20:
    #     print("\nLast 20 objects:")
    #     for i in range(len(arr) - 20, len(arr)):
    #         print(
    #             "Name: {} - Grade: {}".format(arr[i].name, str(arr[i].grade)))

    # else:
    #     print("\nLast " + str(len(arr)) + " Objects:")
    #     for i in range(len(arr)):
    #         print(
    #             "Name: {} - Grade: {}".format(arr[i].name, str(arr[i].grade)))

    time_taken = time.time()
    insertionSort(arr)
    time_taken = (time.time() - time_taken)*1000
    
    print("\n-------------------------------------------------------")
    print("After Sorting")

    # if len(arr) > 20:
    #     print("\nFirst 20 objects:")
    #     for i in range(20):
    #         print(
    #             "Name: {} - Grade: {}".format(arr[i].name, str(arr[i].grade)))
    # else:
    #     print("\nFirst " + str(len(arr)) + " objects: ")
    #     for i in range(len(arr)):
    #         print(
    #             "Name: {} - Grade: {}".format(arr[i].name, str(arr[i].grade)))

    # Print last 20 objects in the arr_75000
    # if len(arr) > 20:
    #     print("\nLast 20 objects:")
    #     for i in range(len(arr) - 20, len(arr)):
    #         print(
    #             "Name: {} - Grade: {}".format(arr[i].name, str(arr[i].grade)))

    # else:
    #     print("\nLast " + str(len(arr)) + " Objects:")
    #     for i in range(len(arr)):
    #         print(
    #             "Name: {} - Grade: {}".format(arr[i].name, str(arr[i].grade)))

    print("-------------------------------------------------------\n")
    print(f"Time taken to sort: {str(time_taken)} ms")
    trial+=1
