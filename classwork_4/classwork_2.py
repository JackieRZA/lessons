"""

Написать программу, которая выведет на экран все числа от 1 до 100 которые кратные n (n вводится с клавиатуры).

"""

n = int(input("vvedite chislo: "))

for item in range(100):
    if item % n == 0:
        print(item)
