from student import Student
from insertionSort import insertionSort
from names import student_names

import random, time

start_time = time.time()

# Code for 75000 objects
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

print('______________________________________________________________')
print("Before sorting (10):")

# Print first & last 20 objects in the arr_75000
if len(arr) > 20:
    print("\nFirst 20 objects:")
    for i in range(20):
        print(
            "Name: {} - Grade: {}".format(arr[i].name, str(arr[i].grade)))

# Print last 20 objects in the arr_75000

if len(arr) > 20:
    print("\nLast 20 objects:")
    for i in range(len(arr) - 20, len(arr)):
        print(
            "Name: {} - Grade: {}".format(arr[i].name, str(arr[i].grade)))

if len(arr) < 20:
    print("\nLast " + str(len(arr)) + " Objects:")
    for i in range(len(arr)):
        print(
            "Name: {} - Grade: {}".format(arr[i].name, str(arr[i].grade)))

print('______________________________________________________________')

# Sorting the array by grade
insertionSort(arr)

# Print first 20 objects in the sorted array
print("\nAfter sorting (10):")

if len(arr) > 20:
    print("\nFirst 20 objects:")
    for i in range(20):
        print(
            "Name: {} - Grade: {}".format(arr[i].name, str(arr[i].grade)))

# Print last 20 objects in the sorted array


if len(arr) > 20:
    print("\nLast 20 objects:")
    for i in range(len(arr) - 20, len(arr)):
        print(
            "Name: {} - Grade: {}".format(arr[i].name, str(arr[i].grade)))

if len(arr) < 20:
    print("\nFirst " + str(len(arr)) + " Objects:")
    for i in range(len(arr)):
        print(
            "Name: {} - Grade: {}".format(arr[i].name, str(arr[i].grade)))


print('______________________________________________________________')

time_taken_milliseconds = round((time.time() - start_time)*1000, 5)

print("\n--- %s milliseconds ---" % (str((time_taken_milliseconds))))
