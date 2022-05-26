"""

Получить сумму кубов натуральных чисел от n до m используя цикл for, числа n и m вводятся с клавиатуры.

"""


n = int(input("Введите число n: "))
m = int(input("Введите число m: "))

result = 0

for element in range (n, m + 1):
    result += element ** 3

print(result)