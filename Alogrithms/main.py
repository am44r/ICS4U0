from student import Student
from insertionSort import insertionSort
from names import student_names

import random

# Code for 75000 objects
arr_75000 = []
for i in range(0, 75000):
    random_name_value = random.randint(0, len(student_names) - 1)
    new_object = Student(
        student_names[random_name_value], random.randint(1, 100))
    arr_75000.append(new_object)

# # Print all 75000 generated objects formatted to the console
# for i in range(len(arr_75000)):
#     print(
#         "Rank: {} - Grade: {}".format(str(arr_75000[i].isGraduating), str(arr_75000[i].grade)))

print('______________________________________________________________')
print("Before sorting (75000):")

# Print first & last 20 objects in the arr_75000
print("\nFirst 20 objects:")
for i in range(20):
    print(
        "Name: {} - Grade: {}".format(arr_75000[i].name, str(arr_75000[i].grade)))


# Print last 20 objects in the arr_75000
print("\nLast 20 objects:")
for i in range(len(arr_75000) - 20, len(arr_75000)):
    print(
        "Name: {} - Grade: {}".format(arr_75000[i].name, str(arr_75000[i].grade)))

print('______________________________________________________________')

# Sorting the array by grade
insertionSort(arr_75000)

# Print first 20 objects in the sorted array
print("\nAfter sorting (75000):")
print("\nFirst 20 objects:")
for i in range(20):
    print(
        "Name: {} - Grade: {}".format(arr_75000[i].name, str(arr_75000[i].grade)))

# Print last 20 objects in the sorted array
print("\nLast 20 objects:")
for i in range(len(arr_75000) - 20, len(arr_75000)):
    print(
        "Name: {} - Grade: {}".format(arr_75000[i].name, str(arr_75000[i].grade)))

print('______________________________________________________________')
