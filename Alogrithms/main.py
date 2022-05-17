from student import Student

import random


arr_75000 = []
for i in range(1, 10):
    new_object = Student(random.randint(1, 10), random.randint(1, 101))
    arr_75000.append(new_object)

for i in range(len(arr_75000)):
    print(
        "Rank: {} - Grade: {}".format(str(arr_75000[i].fight_rank), str(arr_75000[i].grade)))
