from student import Student
from names import student_names

import random
import time

trial = 1

for i in range(10):
    # Creating Objects
    arr = []
    for i in range(0, 30000):
        random_name_value = random.randint(0, len(student_names) - 1)
        new_object = Student(
            student_names[random_name_value], random.randint(1, 100))
        arr.append(new_object)




    time_ = time.time_ns()
    arr.sort(key=lambda x: x.grade)
    time_ = (time.time_ns() - time_)/1000000

    print('\n----------------------------------------')
    print(f"Trial: {trial}")
    print('------------------------------------------')
    print(f"{time_}")

    trial += 1
